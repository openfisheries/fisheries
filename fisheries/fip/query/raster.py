"""
The `raster` module is responsible for getting results from raster queries.

The Class knows about the tables. you can then ask it for tables, totals, weighted sums etc.

"""

# Not implemented...
class FromRasters():
    def __init__(self):
        """
        I know about the database connection, avaialable tables etc.
        """
        pass

    def summary(self):
        """I give you a complete summary table for a given geom"""
        pass

    def from_point(self):
        pass

    def from_polygon(self):
        pass


from geoalchemy2.shape import from_shape
from shapely.geometry import Point, Polygon, shape
from sqlalchemy import func

from sqlalchemy import text
from geoalchemy2 import WKTElement

from fisheries.fip.tools import transform_geojson


def from_polygon(session, table_name, polygon_coordinates):
    nad83_lonlat = 'EPSG:4269'
    texas_centric_xy = 'EPSG:3083'

    polygon_coordinates = {
        "type": "Polygon",
        "coordinates": polygon_coordinates
    }

    # Transform the Polygon from received lon, lat to Texas Centric x, y
    polygon_transformed = transform_geojson(
        polygon_coordinates, input_crs=nad83_lonlat, output_crs=texas_centric_xy)

    # Assuming exterior ring only
    # polygon = from_shape(Polygon(polygon_transformed), srid=3083)
    polygon = Polygon(polygon_transformed)

    # test value
    # wkt = 'POLYGON((2975206.2278075265 7305263.57216,3005159.353245655 7305197.212714661,3005555.7820766345 7274098.9,2974811.9170059203 7274773.793788631,2975206.2278075265 7305263.57216))'

    '''
    # Original version (only select centroid within polygon and provides non-weighted totals)
    sql_query = text(f"""
        SELECT sum(ST_Value(rast, geom)) AS value
        FROM {table_name},
        LATERAL ST_PixelAsCentroids(rast) AS geom
        WHERE ST_Intersects(
            geom,
            ST_GeomFromText('{polygon.wkt}', 3083)
        );
    """)
    '''

    # Update version to calc proportion of cell inside polygon and return weighted totals
    # NOTE: not using bind params because table_name comes from dict lookup and WKT is generated from our code
    sql_query = text(f"""
        WITH query AS (
            SELECT ST_GeomFromText('{polygon.wkt}', 3083) AS geom
        ),
        squares AS (
            SELECT
                (ST_DumpAsPolygons(rast)).*  -- geom, val
            FROM
                {table_name}
        ),
        interim AS (
            SELECT
                ST_Intersection(squares.geom, query.geom) AS geom,
                ST_Area(  (ST_Intersection(squares.geom, query.geom))  ) AS new_area,
                squares.val AS original_value,
                ST_Area(squares.geom) AS original_area
            FROM
                squares, query
            WHERE
                ST_Intersects(squares.geom, query.geom)
        ),
        result AS (
            SELECT
                -- geom,
                -- original_value,
                -- new_area / original_area AS proportion,
                original_value * (new_area / original_area) AS weighted_value
            FROM interim
        )
        SELECT sum(weighted_value) FROM result;
    """)

    # result = session.execute(sql_query, {'geom': geom, 'srs_id': 3083})
    result = session.execute(sql_query)

    # Result contains a single row where the first column contains the (weighted) sum
    return(result.fetchone()[0])

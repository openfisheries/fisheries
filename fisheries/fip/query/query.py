import json
import re

from shapely.geometry import Polygon
from sqlalchemy import text


# TODO: Move to .vector
def from_polygon(session, table_name, column_name, polygon_coordinates):
    """ This version queries vector layers """
    # Polygon coordinates in WGS84
    polygon_coordinates = {
        "type": "Polygon",
        "coordinates": polygon_coordinates
    }

    # Create a Polygon object using Shapely
    polygon = Polygon(polygon_coordinates["coordinates"][0])

    sql_query = text(f"""
        WITH query AS (
            SELECT ST_GeomFromText('{polygon.wkt}', 4326) AS geom
        ),
        input_polygons AS (
            SELECT
                wkb_geometry AS geom,
                {column_name} AS value
            FROM
                {table_name}
        ),
        intersected AS (
            SELECT
                ST_Intersection(input_polygons.geom, query.geom) AS geom,
                ST_Area(ST_Intersection(input_polygons.geom, query.geom)) AS intersection_area,
                input_polygons.value AS original_value,
                ST_Area(input_polygons.geom) AS original_area
            FROM
                input_polygons, query
            WHERE
                ST_Intersects(input_polygons.geom, query.geom)
        ),
        result AS (
            SELECT
                original_value * (intersection_area / original_area) AS weighted_value
            FROM intersected
        )
        SELECT sum(weighted_value) FROM result;
    """)

    # Execute the query and fetch the result
    result = session.execute(sql_query)

    # Result contains a single row where the first column contains the (weighted) sum
    return result.fetchone()[0]


class Query():
    def __init__(self, geojson):
        """ Create a query object for a given GeoJSON feature """
        self.geojson = self._clean_geojson(geojson)
        self.values = {}

    def __call__(self, session, fields):
        """
        Run the query on a specified database session to find specified values
        Where values can be a list (or dict keys for legacy reasons)
        """
        for field in fields:
            value = self._get_value(session, field)
            # Store the rounded number as string (with comma as thousands separater)
            self.values[field] = '-' if value is None else f"{round(value):,}"

    def _clean_geojson(self, geojson):
        if isinstance(geojson, str):
            # TODO: handle variants of GeoJSON (feature, featurecollection)
            return json.loads(geojson)
        else:
            return geojson

    def _get_value(self, session, variable):
        # TODO: treat variable as a vector layer if it contains `.` (table_name.column_name) and
        # otherwise treat as raster layer (table_name) with single raster value
        if self.geojson['type'] == 'Point':
            if '.' in variable:
                return self.value_from_point(session, variable)
            else:
                raise ValueError('This implementation of report_by_feature is expecting a variable with vector table')
                return get_raster_value(geojson, variable)  # variable is just table name

        elif self.geojson['type'] == 'Polygon':
            if '.' in variable:
                # equiv of from_polygon
                return self.value_from_polygon(session, variable)
            else:
                # Generate a query to extract all raster values that intersect with the polygon
                raise ValueError('This implementation of report_by_feature is expecting a variable with vector table')
                return from_polygon(session, variable, polygon_coordinates)

    def value_from_point(self, session, variable):
        """Query a vector layer to get the value of a specified variable at a given GeoJSON point."""
        
        try:
            # Extract longitude and latitude from GeoJSON
            lon, lat = self.geojson['coordinates']
        except (KeyError, ValueError) as e:
            raise ValueError("Invalid GeoJSON format") from e
        
        # Split variable into table and column names
        try:
            table_name, column_name = variable.split('.')
        except ValueError as e:
            raise ValueError("Variable should be in the format 'table_name.column_name'") from e
        
        # Sanitize table and column names to prevent SQL injection
        if not re.match(r'^[a-zA-Z_][a-zA-Z0-9_]*$', table_name):
            raise ValueError("Invalid table name")
        if not re.match(r'^[a-zA-Z_][a-zA-Z0-9_]*$', column_name):
            raise ValueError("Invalid column name")
        
        # SQL query to find the value at the given point
        # Assuming the lon, lat below is WGS84 (4326) but it could be NAD83 lon, lat 'EPSG:4269'
        query = text(f"""
            SELECT {column_name}
            FROM {table_name}
            WHERE ST_Intersects({table_name}.wkb_geometry, ST_SetSRID(ST_MakePoint(:lon, :lat), 4326))
            LIMIT 1;
        """)

        try:
            # Execute query and fetch result
            result = session.execute(query, {'lon': lon, 'lat': lat}).fetchone()
            return result[0] if result else None
        except Exception as e:
            # Handle database exceptions
            raise RuntimeError("Database query failed") from e

    def value_from_polygon(self, session, variable):
        polygon_coordinates = self.geojson['coordinates']

        # Check and adjust the format of polygon_coordinates to ensure it's a list of lists
        if isinstance(polygon_coordinates[0][0], float):
            # This means the coordinates are in the simple format and need to be wrapped in another list
            polygon_coordinates = [polygon_coordinates]  # Correct the format by wrapping in a list

        table_name, column_name = variable.split('.')
        return from_polygon(session, table_name, column_name, polygon_coordinates)

import json

from geoalchemy2.shape import from_shape
import numpy as np
from shapely.geometry import Point, Polygon
from sqlalchemy import func

from fisheries.fip.models import CountiesEdited
from fisheries.fip.models import Rf10LandT20072014
from fisheries.fip.db import Session


def report_by_feature(geojson, variable):
    if isinstance(geojson, str):
        # FIXME: json requires keys and values in double quotes
        geojson = json.loads(geojson.replace("'", '"'))

    with Session() as session:
        geometry_type = geojson['type']

        if geometry_type == 'Point':
            # return f"{variable}"
            lon, lat = geojson['coordinates']
            point = from_shape(Point(lon, lat), srid=4269)
            point = func.ST_Transform(point, 3083)

            # Assuming 'rast' is the raster column in the raster data tables
            # and 1 is the band number of the raster
            raster_value_query = session.query(
                func.ST_Value(Rf10LandT20072014.rast, 1, point)
            ).filter(
                func.ST_Intersects(Rf10LandT20072014.rast, point)
            )
    
            raster_values = raster_value_query.all()

            result = [value[0] for value in raster_values]
            return f"{int(result[0]):,}"

        elif geometry_type == 'Polygon':
            return f"-{variable}-"
            # Shapely requires input that supports __array_interface__ (like a NumPy array) instead of a list of lists
            coordinates = np.array(geojson['coordinates'])
            polygon = from_shape(Polygon(coordinates), srid=4269)
            intersecting_counties = session.query(
                CountiesEdited,
                # Calculate the proportion of the county intersecting with the polygon
                (func.ST_Area(func.ST_Intersection(CountiesEdited.wkb_geometry, polygon)) /
                func.ST_Area(CountiesEdited.wkb_geometry)).label('proportion_in_polygon')
            ).filter(
                func.ST_Intersects(CountiesEdited.wkb_geometry, polygon)
            ).all()

            # This will return a list of tuples, with each tuple containing a CountiesEdited object 
            # and the proportion of its area that is within the polygon.
            return [(county.countyname, proportion) for county, proportion in intersecting_counties]

        else:
            raise ValueError("Invalid GeoJSON type. Must be 'Point' or 'Polygon'.")

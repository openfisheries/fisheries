import json

from geoalchemy2.shape import from_shape
import numpy as np
from shapely.geometry import Point, Polygon
from sqlalchemy import func

from fisheries.fip.models import CountiesEdited
from fisheries.fip.db import Session



"""
def select_county(geojson): 
    if isinstance(geojson, str):
        geojson = json.loads(geojson)

    with Session() as session:
        geometry_type = geojson['type']

        if geometry_type == 'Point':
            lon, lat = geojson['coordinates']
            point = from_shape(Point(lon, lat), srid=4269)
            counties_containing_point = session.query(CountiesEdited).filter(
                func.ST_Contains(CountiesEdited.wkb_geometry, point)
            ).all()
            return [county.countyname for county in counties_containing_point]

        elif geometry_type == 'Polygon':
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
"""
import json

from geoalchemy2.shape import from_shape
import numpy as np
from shapely.geometry import Point, Polygon
from sqlalchemy import func

from fisheries.fip.models import CountiesEdited
from fisheries.fip.models import *
from fisheries.fip.db import Session


# Beware the depluralization of the class names
table_lookup = {
    'RF10_land_e_RS': Rf10LandER,
    'RF10_rev_e_RS': Rf10RevER,
    'RF10_land_e_MS': Rf10LandEM,
    'RF10_rev_e_MS': Rf10RevEM,
    'RF10_land_e_SS': Rf10LandES,
    'RF10_rev_e_SS': Rf10RevES,
    'RF10_land_e_SG': Rf10LandESg,
    'RF10_rev_e_SG': Rf10RevESg,
    'RF10_land_e_DG': Rf10LandEDg,
    'RF10_rev_e_DG': Rf10RevEDg,
    'RF10_land_e_TF': Rf10LandETf,
    'RF10_rev_e_TF': Rf10RevETf,
    'RF10_land_e_JA': Rf10LandEJa,
    'RF10_rev_e_JA': Rf10RevEJa,
    'RF10_land_e_TR': Rf10LandETr,
    'RF10_rev_e_TR': Rf10RevETr,
    'RF10_land_e_GP': Rf10LandEGp,
    'RF10_rev_e_GP': Rf10RevEGp,
    'RF10_land_e_CP': Rf10LandECp,
    'RF10_rev_e_CP': Rf10RevECp,
    'RF10_land_t_2007_2014': Rf10LandT20072014,
    'RF10_rev_t_2007_2014': Rf10RevT20072014,
    'RF10_land_t_2015_2021': Rf10LandT20152021,
    'RF10_rev_t_2015_2021': Rf10RevT20152021,
    'RF10_land_s_FL': Rf10LandSFl,
    'RF10_rev_s_FL': Rf10RevSFl,
    'RF10_land_s_AL': Rf10LandSAl,
    'RF10_rev_s_AL': Rf10RevSAl,
    'RF10_land_s_MS': Rf10LandSM,
    'RF10_rev_s_MS': Rf10RevSM,
    'RF10_land_s_LA': Rf10LandSLa,
    'RF10_rev_s_LA': Rf10RevSLa,
    'RF10_land_s_TX': Rf10LandSTx,
    'RF10_rev_s_TX': Rf10RevSTx,
}



def report_by_feature(geojson, variable):
    if isinstance(geojson, str):
        geojson = json.loads(geojson)

    with Session() as session:
        geometry_type = geojson['type']

        if geometry_type == 'Point':
            lon, lat = geojson['coordinates']
            point = from_shape(Point(lon, lat), srid=4269)
            point = func.ST_Transform(point, 3083)

            # Assuming 'rast' is the raster column in the raster data tables
            # and 1 is the band number of the raster
            raster_value_query = session.query(
                func.ST_Value(table_lookup[variable].rast, 1, point)
            ).filter(
                func.ST_Intersects(table_lookup[variable].rast, point)
            )
    
            raster_values = raster_value_query.all()

            result = [value[0] for value in raster_values]
            try:
                return result[0]
            except:
                return None

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

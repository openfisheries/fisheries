import json
import logging

from geoalchemy2.shape import from_shape
import numpy as np
from shapely.geometry import Point, Polygon
from sqlalchemy import func

from fisheries.fip.models import CountiesEdited
from fisheries.fip.models import *
from fisheries.fip.db import Session

from fisheries.fip.query.raster import from_polygon


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


def temp_output():
    return {'Report': '<p align="center"><img src="/mapstore/dist/themes/load-35_128.gif"/></p><h1><center>Please wait...</center></h1><h2><center>Generating report</center></h2>'}


def report_by_feature(geojson, variable):
    if isinstance(geojson, str):
        # TODO: handle variants of GeoJSON (feature, featurecollection)
        geojson = json.loads(geojson)

    with Session() as session:
        geometry_type = geojson['type']

        # TODO: refactor into separate functions
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
            polygon_coordinates = geojson['coordinates']

            # Check and adjust the format of polygon_coordinates to ensure it's a list of lists
            if isinstance(polygon_coordinates[0][0], float):
                # This means the coordinates are in the simple format and need to be wrapped in another list
                polygon_coordinates = [polygon_coordinates]  # Correct the format by wrapping in a list

            # Generate a query to extract all raster values that intersect with the polygon
            return from_polygon(session, variable, polygon_coordinates)


if __name__ == '__main__':
    # Run `report_by_feature(geojson, variable)` with example geojson and variable
    # Currently texting this inside the pygeoapi container with:
    # docker exec fip-pygeoapi-1 python3 /fisheries/fisheries/fip/report.py

    # An input like the following is currently coming from the front end
    geojson = '{"feature":"{\"type\":\"Polygon\",\"coordinates\":[[-84.71269813091097,28.847503496854813],[-84.61483069420395,28.835827809755813],[-84.6293112701231,28.747982590431548],[-84.72844093762872,28.757855812612746],[-84.71269813091097,28.847503496854813]]}"}'

    # Manually removed outer dict to allow json.loads to work without 'missing ,' error
    # note geometry type is 'Polygon'
    geojson = '{\"type\":\"Polygon\",\"coordinates\":[[-84.71269813091097,28.847503496854813],[-84.61483069420395,28.835827809755813],[-84.6293112701231,28.747982590431548],[-84.72844093762872,28.757855812612746],[-84.71269813091097,28.847503496854813]]}'
    variable = 'RF10_land_e_RS'

    report_by_feature(geojson, variable)

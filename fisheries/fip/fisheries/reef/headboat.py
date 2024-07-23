import json

from geoalchemy2.shape import from_shape
import numpy as np
from shapely.geometry import Point, Polygon
from sqlalchemy import func

from fisheries.fip.db import Session
from fisheries.fip.models import *
from fisheries.fip.query.raster import from_polygon

from fisheries.fip.templates.headboat import headboat_template, headboat_csv
from fisheries.fip.templates.nodata import nodata_template


headboad_values = {'hb': ""}


def get_raster_value(geojson, variable):
    # Extract longitude and latitude from GeoJSON
    lon, lat = geojson['coordinates']
    
    query = text(f"""
        WITH point_geom AS (
            SELECT ST_Transform(ST_SetSRID(ST_MakePoint(:lon, :lat), 4269), 3083) AS geom
        )
        SELECT ST_Value({variable}.rast, 1, point_geom.geom)
        FROM {variable}, point_geom
        WHERE ST_Intersects({variable}.rast, point_geom.geom);
    """)

    # Start a session
    session = Session()
    try:
        # Execute the SQL query
        result = session.execute(query, {'lon': lon, 'lat': lat}).fetchone()
    finally:
        # Close the session
        session.close()

    return result[0] if result else None


def report_by_feature(geojson, variable):
    if isinstance(geojson, str):
        # TODO: handle variants of GeoJSON (feature, featurecollection)
        geojson = json.loads(geojson)

    with Session() as session:
        geometry_type = geojson['type']

        # TODO: refactor into separate functions
        if geometry_type == 'Point':
            return get_raster_value(geojson, variable)

        elif geometry_type == 'Polygon':
            polygon_coordinates = geojson['coordinates']

            # Check and adjust the format of polygon_coordinates to ensure it's a list of lists
            if isinstance(polygon_coordinates[0][0], float):
                # This means the coordinates are in the simple format and need to be wrapped in another list
                polygon_coordinates = [polygon_coordinates]  # Correct the format by wrapping in a list

            # Generate a query to extract all raster values that intersect with the polygon
            return from_polygon(session, variable, polygon_coordinates)



def report(feature, report_type):
    comment = f'Feature: {feature}'
    report_values = {}
    values = headboad_values

    for k in values:
        values[k] = report_by_feature(feature, k)
        report_values[k] = '-' if values[k] is None else f"{round(values[k]):,}"

    if all(v == '-' for v in report_values.values()):
        content = nodata_template.format(
            title='Head Boat Fisheries',
            name='',
            type="",
        )
    else:
        if report_type == 'csv':
            # Remove thousands separators
            values = {k: v.replace(',', '') if isinstance(v, str) else v for k, v in values.items()}

            content = headboat_csv.format(
                name='',
                tot_rev=report_values['hb'].replace(',', '') if isinstance(report_values['hb'], str) else report_values['hb'],
            )
        else:
            content = headboat_template.format(
                comments=comment,
                feature=feature,
                name='',
                tot_rev = report_values['hb'],
            )

    return { 'Report': content }

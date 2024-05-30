import json

from geoalchemy2.shape import from_shape
import numpy as np
from shapely.geometry import Point, Polygon
from sqlalchemy import func

from fisheries.fip.db import Session
from fisheries.fip.models import *
from fisheries.fip.query.raster import from_polygon

from ..templates.shrimp_report import shrimp_template, javascript, csv_text
from ..templates.nodata import nodata_template


## NOTE: We're currently using calc_totals below, but presumably we could use the existing provided
#        overall totals instead because we don't have the same issue as in the RF10 (reef bottom line) totals

shrimp_values = {
    'SF10_land_e_BS': "",
    'SF10_land_e_PS': "",
    'SF10_land_e_RRS': "",
    'SF10_land_e_RS': "",
    'SF10_land_e_S': "",
    'SF10_land_e_T': "",
    'SF10_land_e_WS': "",
#    'SF10_land_overall': "",
    'SF10_land_s_AL': "",
    'SF10_land_s_FL': "",
    'SF10_land_s_LA': "",
    'SF10_land_s_MS': "",
    'SF10_land_s_TX': "",
    'SF10_land_t_2007_2014': "",
    'SF10_land_t_2015_2021': "",
    'SF10_rev_e_BS': "",
    'SF10_rev_e_PS': "",
    'SF10_rev_e_RRS': "",
    'SF10_rev_e_RS': "",
    'SF10_rev_e_S': "",
    'SF10_rev_e_T': "",
    'SF10_rev_e_WS': "",
#    'SF10_rev_overall': "",
    'SF10_rev_s_AL': "",
    'SF10_rev_s_FL': "",
    'SF10_rev_s_LA': "",
    'SF10_rev_s_MS': "",
    'SF10_rev_s_TX': "",
    'SF10_rev_t_2007_2014': "",
    'SF10_rev_t_2015_2021': "",
}


species_landings = ['SF10_land_e_BS', 'SF10_land_e_PS', 'SF10_land_e_RRS', 'SF10_land_e_RS', 'SF10_land_e_S', 'SF10_land_e_T', 'SF10_land_e_WS']
species_revenues = ['SF10_rev_e_BS', 'SF10_rev_e_PS', 'SF10_rev_e_RRS', 'SF10_rev_e_RS', 'SF10_rev_e_S', 'SF10_rev_e_T', 'SF10_rev_e_WS']

########
# NOTE #
########
# This is a rewrite of ..report.report_by_feature for shrimp fisheries
# using direct SQL queries for point (as well as polygon) reports because
# SQLAlchemy models weren't generated and aren't really needed.
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


def calc_totals(values, total_type):
    """ total_type = 'land' or 'rev' """
    # Note: Red snapped is included in mid-depth snapper total
    #       therefore is is not included in species_landings and species_revenues
    actual_total = None
    other_species_total = None

    # actual total
    if (values[f'SF10_{total_type}_t_2007_2014'] is not None and
        values[f'SF10_{total_type}_t_2015_2021'] is not None):

        actual_total = (
            values[f'SF10_{total_type}_t_2007_2014'] +
            values[f'SF10_{total_type}_t_2015_2021']
        )

    # calculate "other species" total (as actutal_total - species_total)
    lookup = species_landings if total_type=='land' else species_revenues

    species_total = None
    for k, v in values.items():
        if k in lookup:
            if v is not None:
                species_total = species_total + v if species_total is not None else v

    if species_total and actual_total is not None:
        other_species_total = actual_total - species_total 

    return (
        f'{round(actual_total):,}' if actual_total is not None else '-',
        f'{round(other_species_total):,}' if other_species_total is not None else '-', 
    )


def shrimp_report(feature):
    comment = f'Feature: {feature}'
    report_values = {}
    values = shrimp_values

    for k in values:
        values[k] = report_by_feature(feature, k)
        report_values[k] = '-' if values[k] is None else f"{round(values[k]):,}"

    if all(v == '-' for v in report_values.values()):
        content = nodata_template.format(
            title='Shrimp Fisheries',
            name='',
            type="shrimp fisheries ",
        )
    else:
        tot_land, other_species_land = calc_totals(values, total_type='land')
        tot_rev, other_species_rev = calc_totals(values, total_type='rev')
        '''
        csv_populated = csv_text.format(
            name='',
            tot_land=tot_land,
            other_species_land=other_species_land,
            tot_rev=tot_rev,
            other_species_rev=other_species_rev,
            **report_values,
        )
        '''
        content = shrimp_template.format(
            comments=comment,
            csv_text='', #csv_populated,
            javascript=javascript,
            name='',
            tot_land=tot_land,
            other_species_land=other_species_land,
            tot_rev=tot_rev,
            other_species_rev=other_species_rev,
            **report_values,
        )

    # FIXME: client has to parse as json to extract the text for the Report value
    return {
        'Report': content,
    }


if __name__ == '__main__':
    # Copied from RF10 (reef.bottom). It's not clear this is necessary for shrimp data...
    # Can we just use the provided overall total instead?

    # species_landings = ['SF10_land_e_BS', 'SF10_land_e_PS', 'SF10_land_e_RRS', 'SF10_land_e_RS', 'SF10_land_e_S', 'SF10_land_e_T', 'SF10_land_e_WS']
    # species_revenues = ['SF10_rev_e_BS', 'SF10_rev_e_PS', 'SF10_rev_e_RRS', 'SF10_rev_e_RS', 'SF10_rev_e_S', 'SF10_rev_e_T', 'SF10_rev_e_WS']
    values = shrimp_values
    species_landings = [v for v in values if 'land_e' in v]
    species_revenues = [v for v in values if 'rev_e' in v]

    print(species_landings)
    print(species_revenues)





"""
The `vector` module is responsible for getting results from vector tables.

"""
from sqlalchemy import text


def territories_by_county(session, county):
    # FIXME: SQL injection risk, replace '{county}' with %s and params
    rf_query = text(f'''
        SELECT ST_AsGeoJSON(ST_Transform(ST_SetSRID(wkb_geometry, 3083), 3857)) AS geojson
        FROM reeffish_territories_locoh
        WHERE county = '{county}';
    ''')

    # Temporary fix for typo in shrimp_allyears_kde layer
    county_fixed = 'TX-GALVESTN' if county == 'TX-GALVESTON' else county

    sf_query = text(f'''
        SELECT ST_AsGeoJSON(ST_Transform(ST_SetSRID(wkb_geometry, 3083), 3857)) AS geojson
        FROM shrimp_allyears_kde
        WHERE county='{county_fixed}';
    ''')

    try:
        rf = session.execute(rf_query)
        rf = rf.fetchone()[0]
    except:
        rf = ''

    try:
        sf = session.execute(sf_query)
        sf = sf.fetchone()[0]
    except:
        sf = ''

    return rf, sf

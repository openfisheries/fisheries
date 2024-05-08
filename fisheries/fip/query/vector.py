from sqlalchemy import text

def territories_by_county(session, county):
    # FIXME: SQL injection risk
    rf_query = text(f'''
        SELECT ST_AsGeoJSON(wkb_geometry) AS geojson
        FROM reeffish_territories_locoh
        WHERE county='{county}';
    ''')

    # Temporary fix for typo in shrimp_allyears_kde layer
    county = 'TX-GALVESTN' if county == 'TX-GALVESTON' else county

    sf_query = text(f'''
        SELECT ST_AsGeoJSON(wkb_geometry) AS geojson
        FROM shrimp_allyears_kde
        WHERE county='{county}';
    ''')

    result = session.execute(rf_query)

    # Result contains a single row where the first column contains the (weighted) sum
    try:
        return(result.fetchone()[0])
    except:
        return('{"county": "{}')

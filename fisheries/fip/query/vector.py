

def territories_by_county(county):
    '''
    Let's start by return RF territory

    SELECT ST_AsGeoJSON(wkb_geometry) AS geojson
    FROM reeffish_territories_locoh
    WHERE county='TX-CAMERON';

    SELECT ST_AsGeoJSON(wkb_geometry) AS geojson
    FROM shrimp_allyears_kde
    WHERE county='TX-CAMERON';
    '''
    return 'the ' + county

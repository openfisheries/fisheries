# test_transform_geojson.py

import json
import pytest

from fisheries.fip.tools import transform_geojson

def test_transform_geojson():
    input_geojson = json.loads('''
    {
        "type": "Polygon",
        "coordinates": [
            [
                [-10049074.04612728, 3592479.247758552],
                [-10049100.04612728, 3592490.247758552],
                [-10049080.04612728, 3592460.247758552],
                [-10049074.04612728, 3592479.247758552]
            ]
        ]
    }
    ''')

    expected_output_geojson = json.loads('{"type": "Polygon", "coordinates": [[[-90.27236806884936, 30.689416001247864], [-90.27260163082325, 30.689500976556417], [-90.2724219677664, 30.68926922553875], [-90.27236806884936, 30.689416001247864]]]}')

    transformed_geometry = transform_geojson(input_geojson)
    transformed_geojson = json.loads(json.dumps(transformed_geometry.__geo_interface__))

    assert transformed_geojson == expected_output_geojson

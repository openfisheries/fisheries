from pygeoapi.process.base import ProcessorExecuteError

from fisheries.fip.db import Session
from fisheries.fip.query.vector import territories_by_county


def return_territory(data):
    mimetype = 'application/json'
    county = data.get('county')

    if county is None:
        raise ProcessorExecuteError('Cannot return territory without input county id')

    with Session() as session:
        rf, sf = territories_by_county(session, county)
        outputs = {
            'county': county,
            'reef_territory': rf,
            'shrimp_territory': sf,
        }

    return mimetype, outputs
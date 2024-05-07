from pygeoapi.process.base import ProcessorExecuteError

from fisheries.fip.query.raster import territories_by_county


def return_territory(data):
    mimetype = 'application/json'
    county = data.get('county')

    if county is None:
        raise ProcessorExecuteError('Cannot return territory without input county id')

    outputs = {
        'county': territories_by_county(county)
    }

    return mimetype, outputs
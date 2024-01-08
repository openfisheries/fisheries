import logging

from pygeoapi.process.base import BaseProcessor, ProcessorExecuteError

from fisheries.fip import select_county


LOGGER = logging.getLogger(__name__)


# Process metadata and description
PROCESS_METADATA = {
    'version': '0.1.0',
    'id': 'select-county',
    'title': {
        'en': 'Select County',
    },
    'description': {
        'en': 'An example process for FIP that takes a GeoJSON Point of Polygon as input '
              'and returns the corresponding county name(s).',
    },
    'jobControlOptions': ['sync-execute', 'async-execute'],
    'keywords': ['select', 'county'],
    'links': [{
        'type': 'text/html',
        'rel': 'about',
        'title': 'information',
        'href': 'https://example.org/process',
        'hreflang': 'en-US'
    }],
    'inputs': {
        'geojson': {
            'title': 'GeoJSON',
            'description': 'GeoJSON Point of Polygon',
            'schema': {
                'type': 'string'
            },
            'minOccurs': 1,
            'maxOccurs': 1,
            'metadata': None,
            'keywords': ['geojson',]
        },
    },
    'outputs': {
        'county': {
            'title': 'County name',
            'description': 'The name of the count(ies) found (if any)',
            'schema': {
                'type': 'object',
                'contentMediaType': 'text/plain'
            }
        }
    },
    'example': {
        'inputs': {
            'geojson': '{"type": "Point", "coordinates": []}',
        }
    }
}


class SelectCountyProcessor(BaseProcessor):
    """Select County Processor"""

    def __init__(self, processor_def):
        """
        Initialize object

        :param processor_def: provider definition

        :returns: pygeoapi.process.fip.selectcountyprocess.SelectCountyProcessor
        """

        super().__init__(processor_def, PROCESS_METADATA)

    def execute(self, data):
        mimetype = 'application/json'
        geojson = data.get('geojson')

        value = f'{select_county(geojson)}'

        outputs = {
            'county': value
        }

        return mimetype, outputs

    def __repr__(self):
        return f'<SelectCountyProcessor> {self.name}'


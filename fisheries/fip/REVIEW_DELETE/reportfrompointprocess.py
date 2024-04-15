""" DEPRECIATED - this module is being replaced by report.py """
import logging

from pygeoapi.process.base import BaseProcessor, ProcessorExecuteError


LOGGER = logging.getLogger(__name__)

#: Process metadata and description
PROCESS_METADATA = {
    'version': '0.1.0',
    'id': 'report-from-point',
    'title': {
        'en': 'Report from point',
    },
    'description': {
        'en': 'Generate report from stats grid cell at a given point',
    },
    'jobControlOptions': ['sync-execute', 'async-execute'],
    'keywords': ['report', 'point'],
    'links': [{
        'type': 'text/html',
        'rel': 'about',
        'title': 'information',
        'href': 'https://example.org/process',
        'hreflang': 'en-US'
    }],
    'inputs': {
        'latitude': {
            'title': 'Latitude',
            'description': 'The search latitude',
            'schema': {
                'type': 'float'
            },
            'minOccurs': 1,
            'maxOccurs': 1,
            'metadata': None,
            'keywords': ['latitude',]
        },
        'longitude': {
            'title': 'Longitude',
            'description': 'The search longitude',
            'schema': {
                'type': 'float'
            },
            'minOccurs': 0,
            'maxOccurs': 1,
            'metadata': None,
            'keywords': ['longitude']
        }
    },
    'outputs': {
        'report': {
            'title': 'Report',
            'description': 'Report generated from stats grid for given point',
            'schema': {
                'type': 'object',
                'contentMediaType': 'application/json'
            }
        }
    },
    'example': {
        'inputs': {
            'latitude': 28.5,
            'longitude': -84.5,
        }
    }
}


class ReportFromPointProcessor(BaseProcessor):
    """Report From point Processor"""

    def __init__(self, processor_def):
        """
        Initialize object

        :param processor_def: provider definition

        :returns: pygeoapi.process.fip.reportfrompointprocess.ReportFromPointProcessor
        """

        super().__init__(processor_def, PROCESS_METADATA)

    def execute(self, data):

        mimetype = 'application/json'
        latitude = data.get('latitude')
        longitude = data.get('longitude')

        if latitude is None or longitude is None:
            raise ProcessorExecuteError('Cannot process without latitude and longitude')

        value = f'Latitude: {latitude}, Longitude: {longitude}'

        outputs = {
            'Report': value
        }

        return mimetype, outputs

    def __repr__(self):
        return f'<ReportFromPointProcessor> {self.name}'

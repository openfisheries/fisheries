""" DEPRECIATED - this module is being replaced by report.py """
import logging

from pygeoapi.process.base import BaseProcessor, ProcessorExecuteError


LOGGER = logging.getLogger(__name__)

#: Process metadata and description
PROCESS_METADATA = {
    'version': '0.1.0',
    'id': 'report-from-polygon',
    'title': {
        'en': 'Report from polygon',
    },
    'description': {
        'en': 'Generate report from stats grid cells for given polygon',
    },
    'jobControlOptions': ['sync-execute', 'async-execute'],
    'keywords': ['report', 'polygon'],
    'links': [{
        'type': 'text/html',
        'rel': 'about',
        'title': 'information',
        'href': 'https://example.org/process',
        'hreflang': 'en-US'
    }],
    'inputs': {
        'polygon': {
            'title': 'Polygon',
            'description': 'The search polygon as GeoJSON',
            'schema': {
                'type': 'string'
            },
            'minOccurs': 1,
            'maxOccurs': 1,
            'metadata': None,
            'keywords': ['polygon',]
        }
    },
    'outputs': {
        'report': {
            'title': 'Report',
            'description': 'Report generated from stats grid for given polygon',
            'schema': {
                'type': 'object',
                'contentMediaType': 'application/json'
            }
        }
    },
    'example': {
        'inputs': {
            'polygon': '{"type": "Feature", "properties": {}, "geometry": {"type": "Polygon", "coordinates": [[[-85.0, 28.0], [-84.0, 28.0], [-84.0, 29.0], [-85.0, 29.0], [-85.0, 28.0]]]}}'
        }
    }
}


class ReportFromPolygonProcessor(BaseProcessor):
    """Report From Polygon Processor"""

    def __init__(self, processor_def):
        """
        Initialize object

        :param processor_def: provider definition

        :returns: pygeoapi.process.fip.reportfrompolygonprocess.ReportFromPolygonProcessor
        """

        super().__init__(processor_def, PROCESS_METADATA)

    def execute(self, data):

        mimetype = 'application/json'
        polygon = data.get('polygon')

        if polygon is None:
            raise ProcessorExecuteError('Cannot process without polygon input data')

        value = f'Polygon: {polygon}'

        outputs = {
            'Report': value
        }

        return mimetype, outputs

    def __repr__(self):
        return f'<ReportFromPolygonProcessor> {self.name}'

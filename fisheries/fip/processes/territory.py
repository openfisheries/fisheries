from collections import OrderedDict
import logging

from pygeoapi.process.base import BaseProcessor

from ..territory import return_territory


LOGGER = logging.getLogger(__name__)


# Process metadata and description
PROCESS_METADATA = {
    'version': '0.1.0',
    'id': 'return-territory',
    'title': {
        'en': 'Return territory as GeoJSON',
    },
    'description': {
        'en': 'Returns GeoJSON of fishing territory for given county ID',
    },
    'jobControlOptions': ['sync-execute', 'async-execute'],
    'keywords': ['fisheries', 'territory'],
    'links': [{
        'type': 'text/html',
        'rel': 'about',
        'title': 'information',
        'href': 'https://fisheries.us.org/api/process',
        'hreflang': 'en-US'
    }],
    'inputs': {
        'county': {
            'title': 'County',
            'description': 'The ID of the county of interest',
            'schema': {
                'type': 'string'
            },
            'minOccurs': 1,
            'maxOccurs': 1,
            'metadata': None,
            'keywords': ['county',]
        }
    },
    'outputs': {
        'county': {
            'title': 'County GeoJSON',
            'description': 'GeoJSON of county',
            'schema': {
                'type': 'object',
                'contentMediaType': 'application/json'  # FIXME: different content types?
            }
        }
    },
    'example': {
        'inputs': {
            'county': '1'
        }
    }
}


class TerritoryProcessor(BaseProcessor):
    """GeoJSON terrirory for given county id"""

    def __init__(self, processor_def):
        """
        Initialize object

        :param processor_def: provider definition

        :returns: pygeoapi.process.fip.fisheries_report.ReturnTerritoryProcessor
        """

        super().__init__(processor_def, PROCESS_METADATA)

    def execute(self, data):
        mimetype, outputs = return_territory(data)
        return mimetype, outputs

    def __repr__(self):
        return f'<ReturnTerritoryProcessor> {self.name}'

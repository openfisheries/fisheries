import logging

from pygeoapi.process.base import BaseProcessor, ProcessorExecuteError

from ..fisheries.shrimp import shrimp_report
from ..fisheries.reef.bottom import reef_report
from ..fisheries.reef.diving import report as diving_report
from ..fisheries.reef.buoys import report as buoys_report
from ..fisheries.reef.gillnet import report as gill_net_report
from ..fisheries.reef.trolling import report as trolling_report


LOGGER = logging.getLogger(__name__)


# Process metadata and description
PROCESS_METADATA = {
    'version': '0.1.0',
    'id': 'fisheries-report',
    'title': {
        'en': 'Fisheries report. Requires point or polygon as GeoJSON',
    },
    'description': {
        'en': 'Generate a fisheries report from stats grid cell for a given point or polygon',
    },
    'jobControlOptions': ['sync-execute', 'async-execute'],
    'keywords': ['fisheries', 'report'],
    'links': [{
        'type': 'text/html',
        'rel': 'about',
        'title': 'information',
        'href': 'https://fisheries.us.org/api/process',
        'hreflang': 'en-US'
    }],
    'inputs': {
        'feature': {
            'title': 'Feature',
            'description': 'The search point or polygon as GeoJSON',
            'schema': {
                'type': 'string'
            },
            'minOccurs': 1,
            'maxOccurs': 1,
            'metadata': None,
            'keywords': ['feature',]
        },
        'fishery': {
            'title': 'Fishery',
            'description': 'Specify "reef" or "shrimp" fisheries (default "None" returns both)',
            'schema': {
                'type': 'string',
                'enum': ['reef', 'shrimp']
            },
            'minOccurs': 0,
            'maxOccurs': 1,
            'metadata': None,
            'keywords': ['fishery',]
        },      
    },
    'outputs': {
        'report': {
            'title': 'Report',
            'description': 'Report generated from stats grid for given point or polygon',
            'schema': {
                'type': 'object',
                'contentMediaType': 'application/json'  # FIXME: different content types?
            }
        }
    },
    'example': {
        'inputs': {
            'feature': '{"type": "Feature", "properties": {}, "geometry": {"type": "Polygon", "coordinates": [[[-85.0, 28.0], [-84.0, 28.0], [-84.0, 29.0], [-85.0, 29.0], [-85.0, 28.0]]]}}'
        }
    }
}


class ReportProcessor(BaseProcessor):
    """Fisheries Report From Feature Processor"""

    def __init__(self, processor_def):
        """
        Initialize object

        :param processor_def: provider definition

        :returns: pygeoapi.process.fip.report.ReportProcessor
        """

        super().__init__(processor_def, PROCESS_METADATA)

    def execute(self, data):
        # FIXME: report_type: 'json', 'html', 'csv', 'pdf'
        mimetype = 'application/json'
        feature = data.get('feature')
        #fishery = data.get('fishery')

        if feature is None:
            raise ProcessorExecuteError('Cannot process without GeoJSON feature input data')

        '''
        if fishery == 'shrimp':
            LOGGER.debug('Generating report for shrimp fisheries')
            outputs = shrimp_report(feature)
        else:
            LOGGER.debug('Generating report for reef fisheries')
            outputs = shrimp_report(feature)
            #outputs = reef_report(feature)
        '''
        outputs = {'Report': (
            '<h2 class="text-center"><b>Landings and Revenues (2007-2021)</b></h2><br>'
            + shrimp_report(feature)['Report']
            + reef_report(feature)['Report']
            + diving_report(feature)['Report']
            + buoys_report(feature)['Report']
            + gill_net_report(feature)['Report']
            + trolling_report(feature)['Report']
        )}

        return mimetype, outputs


    def __repr__(self):
        return f'<FisheriesReportProcessor> {self.name}'

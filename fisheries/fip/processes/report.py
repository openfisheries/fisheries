import logging
from collections import OrderedDict

from pygeoapi.process.base import BaseProcessor, ProcessorExecuteError

from ..fisheries.shrimp import shrimp_report
from ..fisheries.reef.bottom import reef_report
from ..fisheries.reef.diving import report as diving_report
from ..fisheries.reef.buoys import report as buoys_report
from ..fisheries.reef.gillnet import report as gill_net_report
from ..fisheries.reef.trolling import report as trolling_report
from ..fisheries.reef.headboat import report as headboat_report


LOGGER = logging.getLogger(__name__)

CSV = 'csv'
HTML = 'html'

# Dictionaries retain order since Python 3.7
FISHERY = {
    'shrimp': shrimp_report,
    'reef': reef_report,
    'diving': diving_report,
    'buoys': buoys_report,
    'gill_net': gill_net_report,
    'trolling': trolling_report,
    'headboat': headboat_report,
}

FISHERY_KEYS = FISHERY.keys()  # not sufficient for eager evaluation (returns a view object)
FISHERY_KEYS = list(FISHERY.keys())  # see FISHERY_KEYS usage below

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
            'description': "Specify 'shrimp', 'reef', 'diving', 'buoys', 'gill_net', 'trolling' or 'headboat' (default if not specified returns all)",
            'schema': {
                'type': 'string',
#                'enum': FISHERY_KEYS,  # Cannot eval `FISHERY.keys()` here, causes pygeoapi: "TypeError: cannot pickle 'dict_keys' object"
            },
            'minOccurs': 0,
            'maxOccurs': 1,
            'metadata': None,
            'keywords': ['fishery',]
        },
        'format': {
            'title': 'File format determining report type',
            'description': "Specify 'html' or 'csv' (default 'html'). When choosing 'csv' you must also specify a single fishery",  # add 'xlsx' and 'pdf'
            'schema': {
                'type': 'string',
                'enum': [HTML, CSV]
            },
            'minOccurs': 0,
            'maxOccurs': 1,
            'metadata': None,
            'keywords': ['format',]
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
        mimetype = 'application/json'
        feature = data.get('feature')
        fishery = data.get('fishery')
        report_type = data.get('format', HTML)
        report_func = FISHERY[fishery] if fishery is not None else None

        if feature is None:
            raise ProcessorExecuteError('Cannot process without GeoJSON feature input data')

        if report_type == CSV:
            outputs = {'Report': (
                report_func(feature, report_type)['Report']
            )}
        else:
            output = '<h2 class="text-center"><b>Landings and Revenues (2007-2021)</b></h2><br>'
            for func in FISHERY.values():
                output += func(feature, report_type)['Report']
            
            outputs = {'Report': output}

            '''OLD (remove)
            outputs = {'Report': (
                '<h2 class="text-center"><b>Landings and Revenues (2007-2021)</b></h2><br>'
                + shrimp_report(feature, report_type)['Report']
                + reef_report(feature, report_type)['Report']
                + diving_report(feature, report_type)['Report']
                + buoys_report(feature, report_type)['Report']
                + gill_net_report(feature, report_type)['Report']
                + trolling_report(feature, report_type)['Report']
                + headboat_report(feature)['Report']
            )}
            '''

        return mimetype, outputs


    def __repr__(self):
        return f'<FisheriesReportProcessor> {self.name}'

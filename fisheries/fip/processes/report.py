import logging
from collections import OrderedDict

from pygeoapi.process.base import BaseProcessor, ProcessorExecuteError

from ..format.excel import return_xlsx
from .shared import CSV, HTML, XLSX, FISHERY, FISHERY_KEYS

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
            'description': "Specify 'csv', 'html' or 'xlsx' (default 'html'). When choosing 'csv' you must also specify a single fishery",  # add 'pdf'
            'schema': {
                'type': 'string',
                'enum': [CSV, HTML, XLSX]
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

        if fishery and report_type == CSV:
            outputs = {'Report': (
                report_func(feature, report_type)['Report']
            )}
        elif fishery is None and report_type == XLSX:
            #mimetype = 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
            outputs = return_xlsx(feature)
        else:
            # Note: default behaviour ignores fishery type (if specified)
            output = '<h2 class="text-center"><b>Landings and Revenues (2007-2021)</b></h2><br>';
            output += f"""<p style="display: flex; justify-content: center; align-items: center;">Download <button style="margin-left: 5px; font-size: 8px;" id="download-xlsx" onclick='window.fipXlsxReport({feature});'>XLSX</button></p>""";
            for func in FISHERY.values():
                output += func(feature, report_type)['Report']    
            outputs = {'Report': output}

        return mimetype, outputs


    def __repr__(self):
        return f'<FisheriesReportProcessor> {self.name}'

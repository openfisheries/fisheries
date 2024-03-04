"""
FIXME: Accept point or polygon as GeoJSON
"""
import logging

from pygeoapi.process.base import BaseProcessor, ProcessorExecuteError


output = """
<table class="table fip-table">
  <thead>
    <tr><th class="col-1"><b>{name}</b></th><th>Landings</th><th>Revenues</th></tr>
  </thead>
  <tbody>
    <tr><th class="col-1"><b>Total</b></td><td></td><td></td></tr>

    <tr><th colspan=3 class="col-1"><b>Species</b></td></tr>
    <tr><td>Red Snapper</td><td></td><td></td></tr>
    <tr><td>Mid-depth snappers</td><td></td><td></td></tr>
    <tr><td>Shallow-water snappers</td><td></td><td></td></tr>
    <tr><td>Shallow-water groupers</td><td></td><td></td></tr>
    <tr><td>Deep-water groupers</td><td></td><td></td></tr>
    <tr><td>Tilefishes</td><td></td><td></td></tr>
    <tr><td>Jacks</td><td></td><td></td></tr>
    <tr><td>Triggerfishes</td><td></td><td></td></tr>
    <tr><td>Grunts and porgies</td><td></td><td></td></tr>
    <tr><td>Coastal pelagic</td><td></td><td></td></tr>

    <tr><th colspan=3 class="col-1"><b>Time period</b></td></tr>
    <tr><td>2007-2014</td><td></td><td></td></tr>
    <tr><td>2015-2021</td><td></td><td></td></tr>

    <tr><th colspan=3 class="col-1"><b>State</b></td></tr>
    <tr><td>Florida</td><td></td><td></td></tr>
    <tr><td>Alabama</td><td></td><td></td></tr>
    <tr><td>Mississippi</td><td></td><td></td></tr>
    <tr><td>Louisiana</td><td></td><td></td></tr>
    <tr><td>Texas</td><td></td><td></td></tr>
  </tbody>
</table>
"""


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
        }
    },
    'outputs': {
        'report': {
            'title': 'Report',
            'description': 'Report generated from stats grid for given polygon',
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


class FisheriesReportProcessor(BaseProcessor):
    """Fisheries Report From Feature Processor"""

    def __init__(self, processor_def):
        """
        Initialize object

        :param processor_def: provider definition

        :returns: pygeoapi.process.fip.fisheries_report.FisheriesReportProcessor
        """

        super().__init__(processor_def, PROCESS_METADATA)

    def execute(self, data):
        # FIXME: report_type: 'json', 'html', 'csv', 'pdf'
        mimetype = 'application/json'
        feature = data.get('feature')

        if feature is None:
            raise ProcessorExecuteError('Cannot process without GeoJSON feature input data')

        value = f'Feature: {feature}'

        # FIXME: client has to parse as json to extract the text for the Report value
        outputs = {
            # 'Report': value
            'Report': output.format(name="e.g. Point")  # FIXME
        }

        return mimetype, outputs

    def __repr__(self):
        return f'<FisheriesReportProcessor> {self.name}'

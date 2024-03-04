"""
FIXME: Accept point or polygon as GeoJSON
"""
import logging

from pygeoapi.process.base import BaseProcessor, ProcessorExecuteError


output = """
<table>
    <tr><td><b>{name}</b></td><td>Landings</td><td>Revenues</td></tr>
    <tr><td><b>Total</b></td><td></td><td></td></tr>

    <tr><td rowspan=2><b>Species</b></td></tr>
    <tr><td>Red Snapper</td><td></td><td></td></tr>
    <tr><td>Mid-depth snappers</td><td></td></tr>
    <tr><td>Shallow-water snappers</td><td></td></tr>
    <tr><td>Shallow-water groupers</td><td></td></tr>
    <tr><td>Deep-water groupers</td><td></td></tr>
    <tr><td>Tilefishes</td><td></td></tr>
    <tr><td>Jacks</td><td></td></tr>
    <tr><td>Triggerfishes</td><td></td></tr>
    <tr><td>Grunts and porgies</td><td></td></tr>
    <tr><td>Coastal pelagic</td><td></td></tr>

    <tr><td rowspan=2><b>Time period</b></td></tr>
    <tr><td>2007-2014</td><td></td></tr>
    <tr><td>2015-2021</td><td></td></tr>

    <tr><td rowspan=2><b>State</b></td></tr>
    <tr><td>Florida</td><td></td></tr>
    <tr><td>Alabama</td><td></td></tr>
    <tr><td>Mississippi</td><td></td></tr>
    <tr><td>Louisiana</td><td></td></tr>
    <tr><td>Texas</td><td></td></tr>
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

        outputs = {
            # 'Report': value
            'Report': output.format(name="e.g. Point")  # FIXME
        }

        return mimetype, outputs

    def __repr__(self):
        return f'<FisheriesReportProcessor> {self.name}'

"""
FIXME: Accept point or polygon as GeoJSON
"""
from collections import OrderedDict
import logging

from pygeoapi.process.base import BaseProcessor, ProcessorExecuteError


output = """
<h2 class="text-center">Fisheries Report</h2>
<br/>
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

<br/>
<span class="text-center">Download: 
  <a href="" style="color: grey; pointer-events: none; cursor: default;">CSV</a>, 
  <a href="" style="color: grey; pointer-events: none; cursor: default;">PDF</a>
</span>

"""


OrderedDict([
    ('Red Snapper', ['RF10_land_e_RS', 'RF10_rev_e_RS']),
    ('Mid-depth snappers', ['RF10_land_e_MS.R', 'RF10_rev_e_MS']),
    ('[Shallow-water snappers]', ['RF10_land_e_SS', 'RF10_rev_e_SS']),
    ('Shallow-water groupers', ['RF10_land_e_SG', 'RF10_rev_e_SG']),
    ('Deep-water groupers', ['RF10_land_e_DG', 'RF10_rev_e_DG']),
    ('Tilefishes', ['RF10_land_e_TF', 'RF10_rev_e_TF']),
    ('Jacks', ['RF10_land_e_JA', 'RF10_rev_e_JA']),
    ('Triggerfishes', ['RF10_land_e_TR', 'RF10_rev_e_TR']),
    ('Grunts and porgies', ['RF10_land_e_GP', 'RF10_rev_e_GP']),
    ('Coastal pelagic', ['RF10_land_e_CP', 'RF10_rev_e_CP']),
    ('2007-2014', ['RF10_land_t_2007_2014', 'RF10_rev_t_2007_2014']),
    ('2015-2021', ['RF10_land_t_2015_2021', 'RF10_rev_t_2015_2021']),
    ('Florida', ['RF10_land_s_FL', 'RF10_rev_s_FL']),
    ('Alabama', ['RF10_land_s_AL', 'RF10_rev_s_AL']),
    ('Mississippi', ['RF10_land_s_MS', 'RF10_rev_s_MS']),
    ('Louisiana', ['RF10_land_s_LA', 'RF10_rev_s_LA']),
    ('Texas', ['RF10_land_s_TX', 'RF10_rev_s_TX'])
])


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

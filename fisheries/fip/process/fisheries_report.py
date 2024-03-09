from collections import OrderedDict
import logging

from pygeoapi.process.base import BaseProcessor, ProcessorExecuteError

from ..reportbyfeature import report_by_feature


LOGGER = logging.getLogger(__name__)


output = """
<h2 class="text-center">Reef Fish Landings and Revenues (2007-2021)</h2>
<br/>
<table class="table fip-table">
  <thead>
    <tr><th class="col-1"><b>{name}</b></th><th><b>Landings</b></th><th><b>Revenues</b></th></tr>
  </thead>
  <tbody>
    <tr><th class="col-1"><b>Total</b></td><td>{tot_land}</td><td>{tot_rev}</td></tr>

    <tr><th colspan=3 class="col-1"><b>Species</b></td></tr>
    <tr>
        <td>Mid-depth snappers<br/> &nbsp; (of which Red Snapper)</td>
        <td>{RF10_land_e_MS}<br/>({RF10_land_e_RS})</td>
        <td>{RF10_rev_e_MS}<br/>({RF10_rev_e_RS})</td>
    </tr>
    <tr><td>Shallow-water snappers</td><td>{RF10_land_e_SS}</td><td>{RF10_rev_e_SS}</td></tr>
    <tr><td>Shallow-water groupers</td><td>{RF10_land_e_SG}</td><td>{RF10_rev_e_SG}</td></tr>
    <tr><td>Deep-water groupers</td><td>{RF10_land_e_DG}</td><td>{RF10_rev_e_DG}</td></tr>
    <tr><td>Tilefishes</td><td>{RF10_land_e_TF}</td><td>{RF10_rev_e_TF}</td></tr>
    <tr><td>Jacks</td><td>{RF10_land_e_JA}</td><td>{RF10_rev_e_JA}</td></tr>
    <tr><td>Triggerfishes</td><td>{RF10_land_e_TR}</td><td>{RF10_rev_e_TR}</td></tr>
    <tr><td>Grunts and porgies</td><td>{RF10_land_e_GP}</td><td>{RF10_rev_e_GP}</td></tr>
    <tr><td>Coastal pelagic</td><td>{RF10_land_e_CP}</td><td>{RF10_rev_e_CP}</td></tr>

    <tr><th colspan=3 class="col-1"><b>Time period</b></td></tr>
    <tr><td>2007-2014</td><td>{RF10_land_t_2007_2014}</td><td>{RF10_rev_t_2007_2014}</td></tr>
    <tr><td>2015-2021</td><td>{RF10_land_t_2015_2021}</td><td>{RF10_rev_t_2015_2021}</td></tr>

    <tr><th colspan=3 class="col-1"><b>State</b></td></tr>
    <tr><td>Florida</td><td>{RF10_land_s_FL}</td><td>{RF10_rev_s_FL}</td></tr>
    <tr><td>Alabama</td><td>{RF10_land_s_AL}</td><td>{RF10_rev_s_AL}</td></tr>
    <tr><td>Mississippi</td><td>{RF10_land_s_MS}</td><td>{RF10_rev_s_MS}</td></tr>
    <tr><td>Louisiana</td><td>{RF10_land_s_LA}</td><td>{RF10_rev_s_LA}</td></tr>
    <tr><td>Texas</td><td>{RF10_land_s_TX}</td><td>{RF10_rev_s_TX}</td></tr>
  </tbody>
</table>

<br/>
<span class="text-center">Download: 
  <a href="" style="color: grey; pointer-events: none; cursor: default;">CSV</a>, 
  <a href="" style="color: grey; pointer-events: none; cursor: default;">PDF</a>
</span>

<!-- {comments} -->

"""

''' unused:
OrderedDict([
    ('Red Snapper', ['RF10_land_e_RS', 'RF10_rev_e_RS']),
    ('Mid-depth snappers', ['RF10_land_e_MS', 'RF10_rev_e_MS']),
    ('Shallow-water snappers', ['RF10_land_e_SS', 'RF10_rev_e_SS']),
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
'''

values = {
    'RF10_land_e_RS': "",
    'RF10_rev_e_RS': "",
    'RF10_land_e_MS': "",
    'RF10_rev_e_MS': "",
    'RF10_land_e_SS': "",
    'RF10_rev_e_SS': "",
    'RF10_land_e_SG': "",
    'RF10_rev_e_SG': "",
    'RF10_land_e_DG': "",
    'RF10_rev_e_DG': "",
    'RF10_land_e_TF': "",
    'RF10_rev_e_TF': "",
    'RF10_land_e_JA': "",
    'RF10_rev_e_JA': "",
    'RF10_land_e_TR': "",
    'RF10_rev_e_TR': "",
    'RF10_land_e_GP': "",
    'RF10_rev_e_GP': "",
    'RF10_land_e_CP': "",
    'RF10_rev_e_CP': "",
    'RF10_land_t_2007_2014': "",
    'RF10_rev_t_2007_2014': "",
    'RF10_land_t_2015_2021': "",
    'RF10_rev_t_2015_2021': "",
    'RF10_land_s_FL': "",
    'RF10_rev_s_FL': "",
    'RF10_land_s_AL': "",
    'RF10_rev_s_AL': "",
    'RF10_land_s_MS': "",
    'RF10_rev_s_MS': "",
    'RF10_land_s_LA': "",
    'RF10_rev_s_LA': "",
    'RF10_land_s_TX': "",
    'RF10_rev_s_TX': "-",
}


# species_landings = [v for v in values if 'land_e' in v]
# species_revenues = [v for v in values if 'rev_e' in v]
# LOGGER.debug(species_landings)
# LOGGER.debug(species_revenues)

# Manually remove Red Snapper (because it is included in mid-depth snappers)
# - 'RF10_land_e_RS'
# - 'RF10_rev_e_RS'
species_landings = ['RF10_land_e_MS', 'RF10_land_e_SS', 'RF10_land_e_SG', 'RF10_land_e_DG', 'RF10_land_e_TF', 'RF10_land_e_JA', 'RF10_land_e_TR', 'RF10_land_e_GP', 'RF10_land_e_CP']
species_revenues = ['RF10_rev_e_MS', 'RF10_rev_e_SS', 'RF10_rev_e_SG', 'RF10_rev_e_DG', 'RF10_rev_e_TF', 'RF10_rev_e_JA', 'RF10_rev_e_TR', 'RF10_rev_e_GP', 'RF10_rev_e_CP']



def calc_totals(values, total_type):
    """ total_type = 'land' or 'rev' """
    # Note: Red snapped is included in mid-depth snapper total
    #       therefore is is not included in species_landings and species_revenues
    actual_total = None
    other_species_total = None

    # actual total
    if (values[f'RF10_{total_type}_t_2007_2014'] is not None and
        values[f'RF10_{total_type}_t_2015_2021'] is not None):

        actual_total = (
            values[f'RF10_{total_type}_t_2007_2014'] +
            values[f'RF10_{total_type}_t_2015_2021']
        )

    # calculate "other species" total (as actutal_total - species_total)
    lookup = species_landings if total_type=='land' else species_revenues

    species_total = None
    for k, v in values.items():
        if k in lookup:
            if v is not None:
                species_total = species_total + v if species_total is not None else v

    if species_total and actual_total is not None:
        other_species_total = actual_total - species_total 

    return (
        f'{round(actual_total):,}' if actual_total is not None else '-',
        f'{round(other_species_total):,}' if other_species_total is not None else '-', 
    )


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
        comment = f'Feature: {feature}'
        report_values = {}

        for k in values:
            values[k] = report_by_feature(feature, k)
            report_values[k] = '-' if values[k] is None else f"{round(values[k]):,}"

        tot_land, other_species_land = calc_totals(values, total_type='land')
        tot_rev, other_species_rev = calc_totals(values, total_type='rev')

        # FIXME: client has to parse as json to extract the text for the Report value
        outputs = {
            # 'Report': value
            'Report': output.format(
                name="",
                comments=comment,
                tot_land=tot_land,
                other_species_land=other_species_land,
                tot_rev=tot_rev,
                other_species_rev=other_species_rev,
                **report_values,
            )
        }

        return mimetype, outputs


    def __repr__(self):
        return f'<FisheriesReportProcessor> {self.name}'


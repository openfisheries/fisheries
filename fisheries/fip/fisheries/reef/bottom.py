from ...report import report_by_feature
from ...templates.reef.bottom import reef_bottom_template, reef_csv
from ...templates.nodata import nodata_template


# For RF10 layers, red snapper is also already included in the mid-depth snapper total
# Beware double counting (see calc_totals below for more details).
reef_values = {
    'RF10_land_overall': "",
    'RF10_rev_overall': "",
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


# Note: Red snapper is included in mid-depth snapper total and therefore it is
# not included in species_landings and species_revenues totals
species_landings = ['RF10_land_e_MS', 'RF10_land_e_SS', 'RF10_land_e_SG', 'RF10_land_e_DG', 'RF10_land_e_TF', 'RF10_land_e_JA', 'RF10_land_e_TR', 'RF10_land_e_GP', 'RF10_land_e_CP']
species_revenues = ['RF10_rev_e_MS', 'RF10_rev_e_SS', 'RF10_rev_e_SG', 'RF10_rev_e_DG', 'RF10_rev_e_TF', 'RF10_rev_e_JA', 'RF10_rev_e_TR', 'RF10_rev_e_GP', 'RF10_rev_e_CP']


def calc_totals(values, total_type, layer_type='RF10'):
    """ total_type = 'land' or 'rev' """

    overall_total = values[f'{layer_type}_{total_type}_overall']
    other_species_total = None

    # calculate "other species" total (as actutal_total - species_total)
    lookup = species_landings if total_type=='land' else species_revenues

    species_total = None
    for k, v in values.items():
        if k in lookup:
            if v is not None:
                species_total = species_total + v if species_total is not None else v

    if species_total is not None and overall_total is not None:
        other_species_total = overall_total - species_total

    # TODO: Calling function no longer needs to use a calculated total ("actual_total")
    # instead they should use the overall total from the values dictionary directly
    actual_total = overall_total

    return (
        f'{round(actual_total):,}' if actual_total is not None else '-',
        f'{round(other_species_total):,}' if other_species_total is not None else '-', 
    )


def reef_report(feature, report_type):
    comment = f'Feature: {feature}'
    report_values = {}
    values = reef_values

    for k in values:
        values[k] = report_by_feature(feature, k)
        report_values[k] = '-' if values[k] is None else f"{round(values[k]):,}"

    if all(v == '-' for v in report_values.values()):
        content = nodata_template.format(
            title='Reef fish fisheries – bottom longline, bandit and handline',
            name='',
            type="reef fisheries ",
        )
    else:
        # In the HTML version, if red snapper values exist they are in parenthesis
        red_snappers_exist = values['RF10_land_e_RS'] is not None and \
            values['RF10_rev_e_RS'] is not None
        left_bracket,right_bracket='()' if red_snappers_exist else ('', '')

        tot_land, other_species_land = calc_totals(values, total_type='land')
        tot_rev, other_species_rev = calc_totals(values, total_type='rev')

        if report_type == 'csv':
            # Remove thousands separators
            values = {k: v.replace(',', '') if isinstance(v, str) else v for k, v in report_values.items()}

            content = reef_csv.format(
                name='',
                tot_land=tot_land.replace(',', '') if isinstance(tot_land, str) else tot_land,
                other_species_land=other_species_land.replace(',', '') if isinstance(other_species_land, str) else other_species_land,
                tot_rev=tot_rev.replace(',', '') if isinstance(tot_rev, str) else tot_rev,
                other_species_rev=other_species_rev.replace(',', '') if isinstance(other_species_rev, str) else other_species_rev,
                **values,
            )
        else:
            content = reef_bottom_template.format(
                comments=comment,
                feature=feature,
                left_bracket=left_bracket,
                right_bracket=right_bracket,
                name='',
                tot_land=tot_land,
                other_species_land=other_species_land,
                tot_rev=tot_rev,
                other_species_rev=other_species_rev,
                **report_values,
            )

    return {'Report': content}


if __name__ == '__main__':
    # species_landings = ['RF10_land_e_MS', 'RF10_land_e_SS', 'RF10_land_e_SG', 'RF10_land_e_DG', 'RF10_land_e_TF', 'RF10_land_e_JA', 'RF10_land_e_TR', 'RF10_land_e_GP', 'RF10_land_e_CP']
    # species_revenues = ['RF10_rev_e_MS', 'RF10_rev_e_SS', 'RF10_rev_e_SG', 'RF10_rev_e_DG', 'RF10_rev_e_TF', 'RF10_rev_e_JA', 'RF10_rev_e_TR', 'RF10_rev_e_GP', 'RF10_rev_e_CP']

    values = reef_values
    species_landings = [v for v in values if 'land_e' in v]
    species_revenues = [v for v in values if 'rev_e' in v]

    # **Manually** removed Red Snapper (because it is included in mid-depth snappers)
    # - 'RF10_land_e_RS'
    # - 'RF10_rev_e_RS'

    print(species_landings)
    print(species_revenues)

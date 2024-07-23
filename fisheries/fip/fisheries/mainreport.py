from fisheries.fip.db import Session
from fisheries.fip.query.query import Query
from fisheries.fip.templates.nodata import nodata_template


def main_report(feature, report_type, values, title, type, template, csv_template):
    comment = f'Feature: {feature}'
    query = Query(feature)

    with Session() as session:
        query(session, values)

    if all(v == '-' for v in query.values.values()):
        content = nodata_template.format(
            title=title,
            name='',
            type=type,
        )
    else:
        # Variable names passed to the template cannot contain periods
        cleaned_values = {key.replace('.', '_'): value for key, value in query.values.items()}

        if report_type == 'csv':
            # Remove thousands separators
            values = {k: v.replace(',', '') if isinstance(v, str) else v for k, v in cleaned_values.items()}

            content = csv_template.format(
                name='',
                **values,
            )
        else:
            content = template.format(
                comments=comment,
                feature=feature,
                name='',
                **cleaned_values,
            )

    return { 'Report': content }

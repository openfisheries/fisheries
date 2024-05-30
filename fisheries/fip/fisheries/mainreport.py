from fisheries.fip.db import Session
from fisheries.fip.query.query import Query
from fisheries.fip.templates.nodata import nodata_template


def main_report(feature, values, title, type, template):
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

        content = template.format(
            comments=comment,
            csv_text='', #csv_populated,
            javascript='', #javascript,
            name='',
            **cleaned_values,
        )

    # FIXME: client has to parse as json to extract the text for the Report value
    return { 'Report': content }

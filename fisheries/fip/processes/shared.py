from ..fisheries.shrimp import shrimp_report
from ..fisheries.reef.bottom import reef_report
from ..fisheries.reef.diving import report as diving_report
from ..fisheries.reef.buoys import report as buoys_report
from ..fisheries.reef.gillnet import report as gill_net_report
from ..fisheries.reef.trolling import report as trolling_report
from ..fisheries.reef.headboat import report as headboat_report


CSV = 'csv'
HTML = 'html'
XLSX = 'xlsx'

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

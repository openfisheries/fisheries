from ..processes.report import CSV, FISHERY


def get_sheets(feature):
    """ Returns an ordered dictionary of CSV results """
    results = {}
    for name, func in FISHERY.values():
        results[name] = func(feature, CSV)['Report']
    return results


def return_xlsx(feature):
    # create Excel content, add tables, stream result

    # FIXME: For now - return a normal response
    return {'Report': get_sheets(feature)}

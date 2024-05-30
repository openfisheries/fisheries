def temp_output():
    return {'Report': '<p align="center"><img src="/mapstore/dist/themes/load-35_128.gif"/></p><h1><center>Please wait...</center></h1><h2><center>Generating report</center></h2>'}


def temp_response(feature, mimetype):
    # TEMPORARY: this code is for debugging
    try:
        import json
        geojson = json.loads(feature)
        if geojson['coordinates'][0] > 0:
            return mimetype, temp_output()
    except:
        pass
    # end temporary code

from fisheries.fip.fisheries.mainreport import main_report
from fisheries.fip.templates.reef.gillnet import reef_gillnet_template, javascript, csv_text


# 'RFGNSG' Reef fish fisheries – gill net (statistical grid)

# For raster layers, the keys in the values dict represented individual rasters as individual table names
# Here, for vector layers, the keys represent attributes (column names) in different tables
# therefore we adopt tablename.attribute as the key.
# Also note that previously, for raster layers, we didn't use the 'overall' layers since we calc this ourselves
values = {
    'RFGNSG.lnd_vrl': "",  # Overall Landings
    'RFGNSG.rv_vrll': "",  # Overall Revenues
    'RFGNSG.lnd__rs': "",  # Landings Red Snapper
    'RFGNSG.rev__rs': "",  # Revenues Red Snapper
    'RFGNSG.lnd__ms': "",  # Landings Mid-depth snapper group
    'RFGNSG.rev__ms': "",  # Revenues Mid-depth snapper group
    'RFGNSG.lnd__ss': "",  # Landings Shallow-water snapper group
    'RFGNSG.rev__ss': "",  # Revenues Shallow-water snapper group
    'RFGNSG.lnd__sg': "",  # Landings Shallow-water grouper group
    'RFGNSG.rev__sg': "",  # Revenues Shallow-water grouper group
    'RFGNSG.lnd__dg': "",  # Landings Deep-water grouper group
    'RFGNSG.rev__dg': "",  # Revenues Deep-water grouper group
    'RFGNSG.lnd__tf': "",  # Landings Tilefishes group
    'RFGNSG.rev__tf': "",  # Revenues Tilefishes group
    'RFGNSG.lnd__ja': "",  # Landings Jacks group
    'RFGNSG.rev__ja': "",  # Revenues Jacks group
    'RFGNSG.lnd__tr': "",  # Landings Triggerfishes group
    'RFGNSG.rev__tr': "",  # Revenues Triggerfishes group
    'RFGNSG.lnd__gp': "",  # Landings Grunts and porgies group
    'RFGNSG.rev__gp': "",  # Revenues Grunts and porgies group
    'RFGNSG.lnd__cp': "",  # Landings Coastal pelagics group
    'RFGNSG.rev__cp': "",  # Revenues Coastal pelagics group
    'RFGNSG_t_2007_2014.lnd_vrl': "",  # Landings 2007-2014
    'RFGNSG_t_2007_2014.rv_vrll': "",  # Revenues 2007-2014
    'RFGNSG_t_2015_2021.lnd_vrl': "",  # Landings 2015-2021
    'RFGNSG_t_2015_2021.rv_vrll': "",  # Revenues 2015-2021
    'RFGNSG_s_FL.lnd_vrl': "",  # Landings Florida
    'RFGNSG_s_FL.rv_vrll': "",  # Revenues Florida
}


def report(feature):
    return main_report(
        feature,
        values=values,
        title='Reef fish fisheries - gill net',
        type="reef fisheries ",
        template=reef_gillnet_template,
    )

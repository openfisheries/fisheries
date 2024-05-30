from fisheries.fip.fisheries.mainreport import main_report
from fisheries.fip.templates.reef.diving import reef_diving_template, javascript, csv_text


# 'RFDSG' Reef fish fisheries - diving (statistical grid)

# For raster layers, the keys in the values dict represented individual rasters as individual table names
# Here, for vector layers, the keys represent attributes (column names) in different tables
# therefore we adopt tablename.attribute as the key.
# Also note that previously, for raster layers, we didn't use the 'overall' layers since we calc this ourselves
values = {
    'RFDSG.lnd_vrl': "",  # Overall Landings
    'RFDSG.rv_vrll': "",  # Overall Revenues
    'RFDSG.lnd__rs': "",  # Landings Red Snapper
    'RFDSG.rev__rs': "",  # Revenues Red Snapper
    'RFDSG.lnd__ms': "",  # Landings Mid-depth snapper group
    'RFDSG.rev__ms': "",  # Revenues Mid-depth snapper group
    'RFDSG.lnd__ss': "",  # Landings Shallow-water snapper group
    'RFDSG.rev__ss': "",  # Revenues Shallow-water snapper group
    'RFDSG.lnd__sg': "",  # Landings Shallow-water grouper group
    'RFDSG.rev__sg': "",  # Revenues Shallow-water grouper group
    'RFDSG.lnd__dg': "",  # Landings Deep-water grouper group
    'RFDSG.rev__dg': "",  # Revenues Deep-water grouper group
    'RFDSG.lnd__tf': "",  # Landings Tilefishes group
    'RFDSG.rev__tf': "",  # Revenues Tilefishes group
    'RFDSG.lnd__ja': "",  # Landings Jacks group
    'RFDSG.rev__ja': "",  # Revenues Jacks group
    'RFDSG.lnd__tr': "",  # Landings Triggerfishes group
    'RFDSG.rev__tr': "",  # Revenues Triggerfishes group
    'RFDSG.lnd__gp': "",  # Landings Grunts and porgies group
    'RFDSG.rev__gp': "",  # Revenues Grunts and porgies group
    'RFDSG.lnd__cp': "",  # Landings Coastal pelagics group
    'RFDSG.rev__cp': "",  # Revenues Coastal pelagics group
    'RFDSG_t_2007_2014.lnd_vrl': "",  # Landings 2007-2014
    'RFDSG_t_2007_2014.rv_vrll': "",  # Revenues 2007-2014
    'RFDSG_t_2015_2021.lnd_vrl': "",  # Landings 2015-2021
    'RFDSG_t_2015_2021.rv_vrll': "",  # Revenues 2015-2021
    'RFDSG_s_FL.lnd_vrl': "",  # Landings Florida
    'RFDSG_s_FL.rv_vrll': "",  # Revenues Florida
}


def report(feature):
    return main_report(
        feature,
        values=values,
        title='Reef fish fisheries - diving',
        type="reef fisheries ",
        template=reef_diving_template,
    )

from fisheries.fip.fisheries.mainreport import main_report
from fisheries.fip.templates.reef.trolling import reef_trolling_template, reef_trolling_csv


# 'RFTSG' Reef fish fisheries – trolling (statistical grid)

# For raster layers, the keys in the values dict represented individual rasters as individual table names
# Here, for vector layers, the keys represent attributes (column names) in different tables
# therefore we adopt tablename.attribute as the key.
# Also note that previously, for raster layers, we didn't use the 'overall' layers since we calc this ourselves
values = {
    'RFTSG.lnd_vrl': "",  # Overall Landings
    'RFTSG.rv_vrll': "",  # Overall Revenues
    'RFTSG.lnd__rs': "",  # Landings Red Snapper
    'RFTSG.rev__rs': "",  # Revenues Red Snapper
    'RFTSG.lnd__ms': "",  # Landings Mid-depth snapper group
    'RFTSG.rev__ms': "",  # Revenues Mid-depth snapper group
    'RFTSG.lnd__ss': "",  # Landings Shallow-water snapper group
    'RFTSG.rev__ss': "",  # Revenues Shallow-water snapper group
    'RFTSG.lnd__sg': "",  # Landings Shallow-water grouper group
    'RFTSG.rev__sg': "",  # Revenues Shallow-water grouper group
    'RFTSG.lnd__dg': "",  # Landings Deep-water grouper group
    'RFTSG.rev__dg': "",  # Revenues Deep-water grouper group
    'RFTSG.lnd__tf': "",  # Landings Tilefishes group
    'RFTSG.rev__tf': "",  # Revenues Tilefishes group
    'RFTSG.lnd__ja': "",  # Landings Jacks group
    'RFTSG.rev__ja': "",  # Revenues Jacks group
    'RFTSG.lnd__tr': "",  # Landings Triggerfishes group
    'RFTSG.rev__tr': "",  # Revenues Triggerfishes group
    'RFTSG.lnd__gp': "",  # Landings Grunts and porgies group
    'RFTSG.rev__gp': "",  # Revenues Grunts and porgies group
    'RFTSG.lnd__cp': "",  # Landings Coastal pelagics group
    'RFTSG.rev__cp': "",  # Revenues Coastal pelagics group
    'RFTSG_t_2007_2014.lnd_vrl': "",  # Landings 2007-2014
    'RFTSG_t_2007_2014.rv_vrll': "",  # Revenues 2007-2014
    'RFTSG_t_2015_2021.lnd_vrl': "",  # Landings 2015-2021
    'RFTSG_t_2015_2021.rv_vrll': "",  # Revenues 2015-2021
    'RFTSG_s_FL.lnd_vrl': "",  # Landings Florida
    'RFTSG_s_FL.rv_vrll': "",  # Revenues Florida
    'RFTSG_s_AL.lnd_vrl': "",
    'RFTSG_s_AL.rv_vrll': "",
    'RFTSG_s_LA.lnd_vrl': "",
    'RFTSG_s_LA.rv_vrll': "",
}


def report(feature, report_type):
    return main_report(
        feature,
        report_type,
        values=values,
        title='Reef fish fisheries – trolling',
        type="reef fisheries ",
        template=reef_trolling_template,
        csv_template=reef_trolling_csv,
    )

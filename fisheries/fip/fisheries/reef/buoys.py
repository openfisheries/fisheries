from fisheries.fip.fisheries.mainreport import main_report
from fisheries.fip.templates.reef.buoys import reef_buoys_template, reef_buoys_csv


# 'RFBSG' Reef fish fisheries – buoys (statistical grid)

# For raster layers, the keys in the values dict represented individual rasters as individual table names
# Here, for vector layers, the keys represent attributes (column names) in different tables
# therefore we adopt tablename.attribute as the key.
# Also note that previously, for raster layers, we didn't use the 'overall' layers since we calc this ourselves
values = {
    'RFBSG.lnd_vrl': "",  # Overall Landings
    'RFBSG.rv_vrll': "",  # Overall Revenues
    'RFBSG.lnd__rs': "",  # Landings Red Snapper
    'RFBSG.rev__rs': "",  # Revenues Red Snapper
    'RFBSG.lnd__ms': "",  # Landings Mid-depth snapper group
    'RFBSG.rev__ms': "",  # Revenues Mid-depth snapper group
    'RFBSG.lnd__ss': "",  # Landings Shallow-water snapper group
    'RFBSG.rev__ss': "",  # Revenues Shallow-water snapper group
    'RFBSG.lnd__sg': "",  # Landings Shallow-water grouper group
    'RFBSG.rev__sg': "",  # Revenues Shallow-water grouper group
    'RFBSG.lnd__dg': "",  # Landings Deep-water grouper group
    'RFBSG.rev__dg': "",  # Revenues Deep-water grouper group
    'RFBSG.lnd__tf': "",  # Landings Tilefishes group
    'RFBSG.rev__tf': "",  # Revenues Tilefishes group
    'RFBSG.lnd__ja': "",  # Landings Jacks group
    'RFBSG.rev__ja': "",  # Revenues Jacks group
    'RFBSG.lnd__tr': "",  # Landings Triggerfishes group
    'RFBSG.rev__tr': "",  # Revenues Triggerfishes group
    'RFBSG.lnd__gp': "",  # Landings Grunts and porgies group
    'RFBSG.rev__gp': "",  # Revenues Grunts and porgies group
    'RFBSG.lnd__cp': "",  # Landings Coastal pelagics group
    'RFBSG.rev__cp': "",  # Revenues Coastal pelagics group
    'RFBSG_t_2007_2014.lnd_vrl': "",  # Landings 2007-2014
    'RFBSG_t_2007_2014.rv_vrll': "",  # Revenues 2007-2014
    'RFBSG_t_2015_2021.lnd_vrl': "",  # Landings 2015-2021
    'RFBSG_t_2015_2021.rv_vrll': "",  # Revenues 2015-2021
    'RFBSG_s_FL.lnd_vrl': "",  # Landings Florida
    'RFBSG_s_FL.rv_vrll': "",  # Revenues Florida
}


def report(feature, report_type):
    return main_report(
        feature,
        report_type,
        values=values,
        title='Reef fish fisheries - buoys',
        type="reef fisheries ",
        template=reef_buoys_template,
        csv_template=reef_buoys_csv,
    )

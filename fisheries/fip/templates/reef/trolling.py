reef_trolling_template = """
<p style="text-align: center; font-size: 20px; font-weight: bold;">Reef fish fisheries - trolling</p>
<p style="display: flex; justify-content: center; align-items: center;">Download <button style="margin-left: 5px; font-size: 8px;" id="download-csv" onclick='window.fipCsvReport({feature},"trolling");'>CSV</button></p>
<br/>
<table class="table fip-table">
  <thead>
    <tr><th class="col-1"><b>{name}</b></th><th><b>Landings (pounds)</b></th><th><b>Revenues (USD)</b></th></tr>
  </thead>
  <tbody>
    <tr><th class="col-1"><b>Total</b></td><td>{RFTSG_lnd_vrl}</td><td>{RFTSG_rv_vrll}</td></tr>

    <tr><td>Red Snapper</td><td>{RFTSG_lnd__rs}</td><td>{RFTSG_rev__rs}</td></tr>
    <tr><td>Mid-depth snapper group</td><td>{RFTSG_lnd__ms}</td><td>{RFTSG_rev__ms}</td></tr>
    <tr><td>Shallow-water snapper group</td><td>{RFTSG_lnd__ss}</td><td>{RFTSG_rev__ss}</td></tr>
    <tr><td>Shallow-water grouper group</td><td>{RFTSG_lnd__sg}</td><td>{RFTSG_rev__sg}</td></tr>
    <tr><td>Deep-water grouper group</td><td>{RFTSG_lnd__dg}</td><td>{RFTSG_rev__dg}</td></tr>
    <tr><td>Tilefishes group</td><td>{RFTSG_lnd__tf}</td><td>{RFTSG_rev__tf}</td></tr>
    <tr><td>Jacks group</td><td>{RFTSG_lnd__ja}</td><td>{RFTSG_rev__ja}</td></tr>
    <tr><td>Triggerfishes group</td><td>{RFTSG_lnd__tr}</td><td>{RFTSG_rev__tr}</td></tr>
    <tr><td>Grunts and porgies group</td><td>{RFTSG_lnd__gp}</td><td>{RFTSG_rev__gp}</td></tr>
    <tr><td>Coastal pelagics group</td><td>{RFTSG_lnd__cp}</td><td>{RFTSG_rev__cp}</td></tr>

    <tr><th colspan=3 class="col-1"><b>Time period</b></td></tr>
    <tr><td>2007-2014</td><td>{RFTSG_t_2007_2014_lnd_vrl}</td><td>{RFTSG_t_2007_2014_rv_vrll}</td></tr>
    <tr><td>2015-2021</td><td>{RFTSG_t_2015_2021_lnd_vrl}</td><td>{RFTSG_t_2015_2021_rv_vrll}</td></tr>

    <tr><th colspan=3 class="col-1"><b>State</b></td></tr>
    <tr><td>Florida</td><td>{RFTSG_s_FL_lnd_vrl}</td><td>{RFTSG_s_FL_rv_vrll}</td></tr>
    <tr><td>Alabama</td><td>{RFTSG_s_AL_lnd_vrl}</td><td>{RFTSG_s_AL_rv_vrll}</td></tr>
    <tr><td>Mississippi</td><td colspan=2>Insufficient data for Mississippi</td></tr>
    <tr><td>Louisiana</td><td>{RFTSG_s_LA_lnd_vrl}</td><td>{RFTSG_s_LA_rv_vrll}</td></tr>
    <tr><td>Texas</td><td colspan=2>Insufficient data for Texas</td></tr>
  </tbody>
</table>

<!-- {comments} -->
"""


reef_trolling_csv = """,Landings (pounds),Revenues (USD)
Total,{RFTSG_lnd_vrl},{RFTSG_rv_vrll}

Red Snapper,{RFTSG_lnd__rs},{RFTSG_rev__rs}
Mid-depth snapper group,{RFTSG_lnd__ms},{RFTSG_rev__ms}
Shallow-water snapper group,{RFTSG_lnd__ss},{RFTSG_rev__ss}
Shallow-water grouper group,{RFTSG_lnd__sg},{RFTSG_rev__sg}
Deep-water grouper group,{RFTSG_lnd__dg},{RFTSG_rev__dg}
Tilefishes group,{RFTSG_lnd__tf},{RFTSG_rev__tf}
Jacks group,{RFTSG_lnd__ja},{RFTSG_rev__ja}
Triggerfishes group,{RFTSG_lnd__tr},{RFTSG_rev__tr}
Grunts and porgies group,{RFTSG_lnd__gp},{RFTSG_rev__gp}
Coastal pelagics group,{RFTSG_lnd__cp},{RFTSG_rev__cp}

Time period,,
2007-2014,{RFTSG_t_2007_2014_lnd_vrl},{RFTSG_t_2007_2014_rv_vrll}
2015-2021,{RFTSG_t_2015_2021_lnd_vrl},{RFTSG_t_2015_2021_rv_vrll}

State,,
Florida,{RFTSG_s_FL_lnd_vrl},{RFTSG_s_FL_rv_vrll}
Alabama,{RFTSG_s_AL_lnd_vrl},{RFTSG_s_AL_rv_vrll}
Mississippi,Insufficient data for Mississippi
Louisiana,{RFTSG_s_LA_lnd_vrl},{RFTSG_s_LA_rv_vrll}
Texas,Insufficient data for Texas
"""

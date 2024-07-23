reef_gillnet_template = """
<p style="text-align: center; font-size: 20px; font-weight: bold;">Reef fish fisheries - gill net</p>
<p style="display: flex; justify-content: center; align-items: center;">Download <button style="margin-left: 5px; font-size: 8px;" id="download-csv" onclick='window.fipCsvReport({feature},"gill_net");'>CSV</button></p>
<br/>
<table class="table fip-table">
  <thead>
    <tr><th class="col-1"><b>{name}</b></th><th><b>Landings (pounds)</b></th><th><b>Revenues (USD)</b></th></tr>
  </thead>
  <tbody>
    <tr><th class="col-1"><b>Total</b></td><td>{RFGNSG_lnd_vrl}</td><td>{RFGNSG_rv_vrll}</td></tr>

    <tr><td>Red Snapper</td><td>{RFGNSG_lnd__rs}</td><td>{RFGNSG_rev__rs}</td></tr>
    <tr><td>Mid-depth snapper group</td><td>{RFGNSG_lnd__ms}</td><td>{RFGNSG_rev__ms}</td></tr>
    <tr><td>Shallow-water snapper group</td><td>{RFGNSG_lnd__ss}</td><td>{RFGNSG_rev__ss}</td></tr>
    <tr><td>Shallow-water grouper group</td><td>{RFGNSG_lnd__sg}</td><td>{RFGNSG_rev__sg}</td></tr>
    <tr><td>Deep-water grouper group</td><td>{RFGNSG_lnd__dg}</td><td>{RFGNSG_rev__dg}</td></tr>
    <tr><td>Tilefishes group</td><td>{RFGNSG_lnd__tf}</td><td>{RFGNSG_rev__tf}</td></tr>
    <tr><td>Jacks group</td><td>{RFGNSG_lnd__ja}</td><td>{RFGNSG_rev__ja}</td></tr>
    <tr><td>Triggerfishes group</td><td>{RFGNSG_lnd__tr}</td><td>{RFGNSG_rev__tr}</td></tr>
    <tr><td>Grunts and porgies group</td><td>{RFGNSG_lnd__gp}</td><td>{RFGNSG_rev__gp}</td></tr>
    <tr><td>Coastal pelagics group</td><td>{RFGNSG_lnd__cp}</td><td>{RFGNSG_rev__cp}</td></tr>

    <tr><th colspan=3 class="col-1"><b>Time period</b></td></tr>
    <tr><td>2007-2014</td><td>{RFGNSG_t_2007_2014_lnd_vrl}</td><td>{RFGNSG_t_2007_2014_rv_vrll}</td></tr>
    <tr><td>2015-2021</td><td>{RFGNSG_t_2015_2021_lnd_vrl}</td><td>{RFGNSG_t_2015_2021_rv_vrll}</td></tr>

    <tr><th colspan=3 class="col-1"><b>State</b></td></tr>
    <tr><td>Florida</td><td>{RFGNSG_s_FL_lnd_vrl}</td><td>{RFGNSG_s_FL_rv_vrll}</td></tr>
    <tr><td>Alabama</td><td colspan=2>Insufficient data for Alabama</td></tr>
    <tr><td>Mississippi</td><td colspan=2>No data for Mississippi</td></tr>
    <tr><td>Louisiana</td><td colspan=2>Insufficient data for Louisiana</td></tr>
    <tr><td>Texas</td><td colspan=2>No data for Texas</td></tr>
  </tbody>
</table>

<!-- {comments} -->
"""


reef_gillnet_csv = """,Landings (pounds),Revenues (USD)
Total,{RFGNSG_lnd_vrl},{RFGNSG_rv_vrll}

Red Snapper,{RFGNSG_lnd__rs},{RFGNSG_rev__rs}
Mid-depth snapper group,{RFGNSG_lnd__ms},{RFGNSG_rev__ms}
Shallow-water snapper group,{RFGNSG_lnd__ss},{RFGNSG_rev__ss}
Shallow-water grouper group,{RFGNSG_lnd__sg},{RFGNSG_rev__sg}
Deep-water grouper group,{RFGNSG_lnd__dg},{RFGNSG_rev__dg}
Tilefishes group,{RFGNSG_lnd__tf},{RFGNSG_rev__tf}
Jacks group,{RFGNSG_lnd__ja},{RFGNSG_rev__ja}
Triggerfishes group,{RFGNSG_lnd__tr},{RFGNSG_rev__tr}
Grunts and porgies group,{RFGNSG_lnd__gp},{RFGNSG_rev__gp}
Coastal pelagics group,{RFGNSG_lnd__cp},{RFGNSG_rev__cp}

Time period,,
2007-2014,{RFGNSG_t_2007_2014_lnd_vrl},{RFGNSG_t_2007_2014_rv_vrll}
2015-2021,{RFGNSG_t_2015_2021_lnd_vrl},{RFGNSG_t_2015_2021_rv_vrll}

State,,
Florida,{RFGNSG_s_FL_lnd_vrl},{RFGNSG_s_FL_rv_vrll}
Alabama,Insufficient data for Alabama
Mississippi,No data for Mississippi
Louisiana,Insufficient data for Louisiana
Texas,No data for Texas
"""

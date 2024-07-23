reef_buoys_template = """
<p style="text-align: center; font-size: 20px; font-weight: bold;">Reef fish fisheries - buoys</p>
<p style="display: flex; justify-content: center; align-items: center;">Download <button style="margin-left: 5px; font-size: 8px;" id="download-csv" onclick='window.fipCsvReport({feature},"bouys");'>CSV</button></p>
<br/>
<table class="table fip-table">
  <thead>
    <tr><th class="col-1"><b>{name}</b></th><th><b>Landings (pounds)</b></th><th><b>Revenues (USD)</b></th></tr>
  </thead>
  <tbody>
    <tr><th class="col-1"><b>Total</b></td><td>{RFBSG_lnd_vrl}</td><td>{RFBSG_rv_vrll}</td></tr>

    <tr><td>Red Snapper</td><td>{RFBSG_lnd__rs}</td><td>{RFBSG_rev__rs}</td></tr>
    <tr><td>Mid-depth snapper group</td><td>{RFBSG_lnd__ms}</td><td>{RFBSG_rev__ms}</td></tr>
    <tr><td>Shallow-water snapper group</td><td>{RFBSG_lnd__ss}</td><td>{RFBSG_rev__ss}</td></tr>
    <tr><td>Shallow-water grouper group</td><td>{RFBSG_lnd__sg}</td><td>{RFBSG_rev__sg}</td></tr>
    <tr><td>Deep-water grouper group</td><td>{RFBSG_lnd__dg}</td><td>{RFBSG_rev__dg}</td></tr>
    <tr><td>Tilefishes group</td><td>{RFBSG_lnd__tf}</td><td>{RFBSG_rev__tf}</td></tr>
    <tr><td>Jacks group</td><td>{RFBSG_lnd__ja}</td><td>{RFBSG_rev__ja}</td></tr>
    <tr><td>Triggerfishes group</td><td>{RFBSG_lnd__tr}</td><td>{RFBSG_rev__tr}</td></tr>
    <tr><td>Grunts and porgies group</td><td>{RFBSG_lnd__gp}</td><td>{RFBSG_rev__gp}</td></tr>
    <tr><td>Coastal pelagics group</td><td>{RFBSG_lnd__cp}</td><td>{RFBSG_rev__cp}</td></tr>

    <tr><th colspan=3 class="col-1"><b>Time period</b></td></tr>
    <tr><td>2007-2014</td><td>{RFBSG_t_2007_2014_lnd_vrl}</td><td>{RFBSG_t_2007_2014_rv_vrll}</td></tr>
    <tr><td>2015-2021</td><td>{RFBSG_t_2015_2021_lnd_vrl}</td><td>{RFBSG_t_2015_2021_rv_vrll}</td></tr>

    <tr><th colspan=3 class="col-1"><b>State</b></td></tr>
    <tr><td>Florida</td><td>{RFBSG_s_FL_lnd_vrl}</td><td>{RFBSG_s_FL_rv_vrll}</td></tr>
    <tr><td>Alabama</td><td colspan=2>Insufficient data for Alabama</td></tr>
    <tr><td>Mississippi</td><td colspan=2>No data for Mississippi</td></tr>
    <tr><td>Louisiana</td><td colspan=2>No data for Louisiana</td></tr>
    <tr><td>Texas</td><td colspan=2>No data for Texas</td></tr>
  </tbody>
</table>

<!-- {comments} -->
"""


reef_buoys_csv = """,Landings (pounds),Revenues (USD)
Total,{RFBSG_lnd_vrl},{RFBSG_rv_vrll}

Red Snapper,{RFBSG_lnd__rs},{RFBSG_rev__rs}
Mid-depth snapper group,{RFBSG_lnd__ms},{RFBSG_rev__ms}
Shallow-water snapper group,{RFBSG_lnd__ss},{RFBSG_rev__ss}
Shallow-water grouper group,{RFBSG_lnd__sg},{RFBSG_rev__sg}
Deep-water grouper group,{RFBSG_lnd__dg},{RFBSG_rev__dg}
Tilefishes group,{RFBSG_lnd__tf},{RFBSG_rev__tf}
Jacks group,{RFBSG_lnd__ja},{RFBSG_rev__ja}
Triggerfishes group,{RFBSG_lnd__tr},{RFBSG_rev__tr}
Grunts and porgies group,{RFBSG_lnd__gp},{RFBSG_rev__gp}
Coastal pelagics group,{RFBSG_lnd__cp},{RFBSG_rev__cp}

Time period,,
2007-2014,{RFBSG_t_2007_2014_lnd_vrl},{RFBSG_t_2007_2014_rv_vrll}
2015-2021,{RFBSG_t_2015_2021_lnd_vrl},{RFBSG_t_2015_2021_rv_vrll}

State,,
Florida,{RFBSG_s_FL_lnd_vrl},{RFBSG_s_FL_rv_vrll}
Alabama,Insufficient data for Alabama
Mississippi,No data for Mississippi
Louisiana,No data for Louisiana
Texas,No data for Texas
"""

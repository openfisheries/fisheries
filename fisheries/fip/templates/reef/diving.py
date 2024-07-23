reef_diving_template = """
<p style="text-align: center; font-size: 20px; font-weight: bold;">Reef fish fisheries - diving</p>
<p style="display: flex; justify-content: center; align-items: center;">Download <button style="margin-left: 5px; font-size: 8px;" id="download-csv" onclick='window.fipCsvReport({feature},"diving");'>CSV</button></p>
<br/>
<table class="table fip-table">
  <thead>
    <tr><th class="col-1"><b>{name}</b></th><th><b>Landings (pounds)</b></th><th><b>Revenues (USD)</b></th></tr>
  </thead>
  <tbody>
    <tr><th class="col-1"><b>Total</b></td><td>{RFDSG_lnd_vrl}</td><td>{RFDSG_rv_vrll}</td></tr>

    <tr><td>Red Snapper</td><td>{RFDSG_lnd__rs}</td><td>{RFDSG_rev__rs}</td></tr>
    <tr><td>Mid-depth snapper group</td><td>{RFDSG_lnd__ms}</td><td>{RFDSG_rev__ms}</td></tr>
    <tr><td>Shallow-water snapper group</td><td>{RFDSG_lnd__ss}</td><td>{RFDSG_rev__ss}</td></tr>
    <tr><td>Shallow-water grouper group</td><td>{RFDSG_lnd__sg}</td><td>{RFDSG_rev__sg}</td></tr>
    <tr><td>Deep-water grouper group</td><td>{RFDSG_lnd__dg}</td><td>{RFDSG_rev__dg}</td></tr>
    <tr><td>Tilefishes group</td><td>{RFDSG_lnd__tf}</td><td>{RFDSG_rev__tf}</td></tr>
    <tr><td>Jacks group</td><td>{RFDSG_lnd__ja}</td><td>{RFDSG_rev__ja}</td></tr>
    <tr><td>Triggerfishes group</td><td>{RFDSG_lnd__tr}</td><td>{RFDSG_rev__tr}</td></tr>
    <tr><td>Grunts and porgies group</td><td>{RFDSG_lnd__gp}</td><td>{RFDSG_rev__gp}</td></tr>
    <tr><td>Coastal pelagics group</td><td>{RFDSG_lnd__cp}</td><td>{RFDSG_rev__cp}</td></tr>

    <tr><th colspan=3 class="col-1"><b>Time period</b></td></tr>
    <tr><td>2007-2014</td><td>{RFDSG_t_2007_2014_lnd_vrl}</td><td>{RFDSG_t_2007_2014_rv_vrll}</td></tr>
    <tr><td>2015-2021</td><td>{RFDSG_t_2015_2021_lnd_vrl}</td><td>{RFDSG_t_2015_2021_rv_vrll}</td></tr>

    <tr><th colspan=3 class="col-1"><b>State</b></td></tr>
    <tr><td>Florida</td><td>{RFDSG_s_FL_lnd_vrl}</td><td>{RFDSG_s_FL_rv_vrll}</td></tr>
    <tr><td>Alabama</td><td colspan=2>No data for Alabama</td></tr>
    <tr><td>Mississippi</td><td colspan=2>No data for Mississippi</td></tr>
    <tr><td>Louisiana</td><td colspan=2>Insufficient data for Louisiana</td></tr>
    <tr><td>Texas</td><td colspan=2>No data for Texas</td></tr>
  </tbody>
</table>

<!-- {comments} -->
"""


reef_diving_csv = """,Landings (pounds),Revenues (USD)
Total,{RFDSG_lnd_vrl},{RFDSG_rv_vrll}

Red Snapper,{RFDSG_lnd__rs},{RFDSG_rev__rs}
Mid-depth snapper group,{RFDSG_lnd__ms},{RFDSG_rev__ms}
Shallow-water snapper group,{RFDSG_lnd__ss},{RFDSG_rev__ss}
Shallow-water grouper group,{RFDSG_lnd__sg},{RFDSG_rev__sg}
Deep-water grouper group,{RFDSG_lnd__dg},{RFDSG_rev__dg}
Tilefishes group,{RFDSG_lnd__tf},{RFDSG_rev__tf}
Jacks group,{RFDSG_lnd__ja},{RFDSG_rev__ja}
Triggerfishes group,{RFDSG_lnd__tr},{RFDSG_rev__tr}
Grunts and porgies group,{RFDSG_lnd__gp},{RFDSG_rev__gp}
Coastal pelagics group,{RFDSG_lnd__cp},{RFDSG_rev__cp}

Time period,,
2007-2014,{RFDSG_t_2007_2014_lnd_vrl},{RFDSG_t_2007_2014_rv_vrll}
2015-2021,{RFDSG_t_2015_2021_lnd_vrl},{RFDSG_t_2015_2021_rv_vrll}

State,,
Florida,{RFDSG_s_FL_lnd_vrl},{RFDSG_s_FL_rv_vrll}
Alabama,No data for Alabama
Mississippi,No data for Mississippi
Louisiana,Insufficient data for Louisiana
Texas,No data for Texas
"""



# FIXME: Move csvText and JS into Map.jsx and rebuild ?
reef_trolling_template = """
<p style="text-align: center; font-size: 20px; font-weight: bold;">Reef fish fisheries - trolling</p>
<br/>
<table class="table fip-table">
  <thead>
    <tr><th class="col-1"><b>{name}</b></th><th><b>Landings</b></th><th><b>Revenues</b></th></tr>
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

<br/>
<span class="text-center" style="display:none">
  Download <button id="download-csv" onclick="{javascript}">CSV</button>
  <!--<a href="" style="color: grey; pointer-events: none; cursor: default;">PDF</a>-->
</span>

<!-- {comments} -->

<div id="csvText" style="display: none">{csv_text}</div>
"""

javascript = """
  csvText = document.getElementById('csvText').innerText;
  console.log(csvText);
  var blob = new Blob([csvText], { type: 'text/csv;charset=utf-8;' });
  
  var downloadLink = document.createElement('a');
  downloadLink.href = URL.createObjectURL(blob);
  downloadLink.setAttribute('download', 'report.csv');
  
  document.body.appendChild(downloadLink);
  downloadLink.click();
  
  document.body.removeChild(downloadLink);
"""


# FIXME: Update for Reef fish - trolling
csv_text = """
Reef Fish Landings and Revenues (2007-2021),,
,,
{name},Landings,Revenues
Total,{tot_land},{tot_rev}
Species,,
Mid-depth snappers,{RF10_land_e_MS},{RF10_rev_e_MS}
   (of which Red Snapper),({RF10_land_e_RS}),({RF10_rev_e_RS})
Shallow-water snappers,{RF10_land_e_SS},{RF10_rev_e_SS}
Shallow-water groupers,{RF10_land_e_SG},{RF10_rev_e_SG}
Deep-water groupers,{RF10_land_e_DG},{RF10_rev_e_DG}
Tilefishes,{RF10_land_e_TF},{RF10_rev_e_TF}
Jacks,{RF10_land_e_JA},{RF10_rev_e_JA}
Triggerfishes,{RF10_land_e_TR},{RF10_rev_e_TR}
Grunts and porgies,{RF10_land_e_GP},{RF10_rev_e_GP}
Coastal pelagic,{RF10_land_e_CP},{RF10_rev_e_CP}
Other species,{other_species_land},{other_species_rev}
Time period,,
2007-2014,{RF10_land_t_2007_2014},{RF10_rev_t_2007_2014}
2015-2021,{RF10_land_t_2015_2021},{RF10_rev_t_2015_2021}
State,,
Florida,{RF10_land_s_FL},{RF10_rev_s_FL}
Alabama,{RF10_land_s_AL},{RF10_rev_s_AL}
Mississippi,{RF10_land_s_MS},{RF10_rev_s_MS}
Louisiana,{RF10_land_s_LA},{RF10_rev_s_LA}
Texas,{RF10_land_s_TX},{RF10_rev_s_TX}
"""

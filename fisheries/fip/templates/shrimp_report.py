shrimp_template = """
<p style="text-align: center; font-size: 20px; font-weight: bold;">Shrimp fisheries</p>
<p style="display: flex; justify-content: center; align-items: center;">Download <button style="margin-left: 5px; font-size: 8px;" id="download-csv" onclick='window.fipCsvReport({feature},"shrimp");'>CSV</button></p>
<br/>
<table class="table fip-table">
  <thead>
    <tr><th class="col-1"><b>{name}</b></th><th><b>Landings (pounds)</b></th><th><b>Revenues (USD)</b></th></tr>
  </thead>
  <tbody>
    <tr><th class="col-1"><b>Total</b></td><td>{tot_land}</td><td>{tot_rev}</td></tr>

    <tr><th colspan=3 class="col-1"><b>Species</b></td></tr>
    <tr><td>Brown shrimp</td><td>{SF10_land_e_BS}</td><td>{SF10_rev_e_BS}</td></tr>
    <tr><td>Pink shrimp</td><td>{SF10_land_e_PS}</td><td>{SF10_rev_e_PS}</td></tr>
    <tr><td>Royal red shrimp</td><td>{SF10_land_e_RRS}</td><td>{SF10_rev_e_RRS}</td></tr>
    <tr><td>Rock shrimp</td><td>{SF10_land_e_RS}</td><td>{SF10_rev_e_RS}</td></tr>
    <tr><td>Seabobs</td><td>{SF10_land_e_S}</td><td>{SF10_rev_e_S}</td></tr>
    <tr><td>Trachypenaeus</td><td>{SF10_land_e_T}</td><td>{SF10_rev_e_T}</td></tr>
    <tr><td>White shrimp</td><td>{SF10_land_e_WS}</td><td>{SF10_rev_e_WS}</td></tr>

    <tr><td>Other species</td><td>{other_species_land}</td><td>{other_species_rev}</td></tr>

    <tr><th colspan=3 class="col-1"><b>Time period</b></td></tr>
    <tr><td>2007-2014</td><td>{SF10_land_t_2007_2014}</td><td>{SF10_rev_t_2007_2014}</td></tr>
    <tr><td>2015-2021</td><td>{SF10_land_t_2015_2021}</td><td>{SF10_rev_t_2015_2021}</td></tr>

    <tr><th colspan=3 class="col-1"><b>State</b></td></tr>
    <tr><td>Florida</td><td>{SF10_land_s_FL}</td><td>{SF10_rev_s_FL}</td></tr>
    <tr><td>Alabama</td><td>{SF10_land_s_AL}</td><td>{SF10_rev_s_AL}</td></tr>
    <tr><td>Mississippi</td><td>{SF10_land_s_MS}</td><td>{SF10_rev_s_MS}</td></tr>
    <tr><td>Louisiana</td><td>{SF10_land_s_LA}</td><td>{SF10_rev_s_LA}</td></tr>
    <tr><td>Texas</td><td>{SF10_land_s_TX}</td><td>{SF10_rev_s_TX}</td></tr>
  </tbody>
</table>

<!-- {comments} -->
"""


# Filename: Shrimp Fish Landings and Revenues (2007-2021),, \n ,,
#           or {name} (otherwise unused)
shrimp_csv = reef_csv = """,Landings (pounds),Revenues (USD)
Total,{tot_land},{tot_rev}
Species,,
Brown shrimp,{SF10_land_e_BS},{SF10_rev_e_BS}
Pink shrimp,{SF10_land_e_PS},{SF10_rev_e_PS}
Royal red shrimp,{SF10_land_e_RRS},{SF10_rev_e_RRS}
Rock shrimp,{SF10_land_e_RS},{SF10_rev_e_RS}
Seabobs,{SF10_land_e_S},{SF10_rev_e_S}
Trachypenaeus,{SF10_land_e_T},{SF10_rev_e_T}
White shrimp,{SF10_land_e_WS},{SF10_rev_e_WS}
Other species,{other_species_land},{other_species_rev}

Time period,,
2007-2014,{SF10_land_t_2007_2014},{SF10_rev_t_2007_2014}
2015-2021,{SF10_land_t_2015_2021},{SF10_rev_t_2015_2021}

State,,
Florida,{SF10_land_s_FL},{SF10_rev_s_FL}
Alabama,{SF10_land_s_AL},{SF10_rev_s_AL}
Mississippi,{SF10_land_s_MS},{SF10_rev_s_MS}
Louisiana,{SF10_land_s_LA},{SF10_rev_s_LA}
Texas,{SF10_land_s_TX},{SF10_rev_s_TX}
"""



# ...
reef_csv = """
Species,Landings,Revenues
Total,{tot_land},{tot_rev}
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

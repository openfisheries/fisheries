reef_bottom_template = """
<p style="text-align: center; font-size: 20px; font-weight: bold;">Reef fish fisheries – bottom longline, bandit and handline</p>
<p style="display: flex; justify-content: center; align-items: center;">Download <button style="margin-left: 5px; font-size: 8px;" id="download-csv" onclick='window.fipCsvReport({feature},"reef");'>CSV</button></p>
<br/>
<table class="table fip-table">
  <thead>
    <tr><th class="col-1"><b>{name}</b></th><th><b>Landings (pounds)</b></th><th><b>Revenues (USD)</b></th></tr>
  </thead>
  <tbody>
    <tr><th class="col-1"><b>Total</b></td><td>{tot_land}</td><td>{tot_rev}</td></tr>

    <tr><th colspan=3 class="col-1"><b>Species</b></td></tr>
    <tr>
        <td>Mid-depth snappers<br/> &nbsp; (of which Red Snapper)</td>
        <td>{RF10_land_e_MS}<br/>{left_bracket}{RF10_land_e_RS}{right_bracket}</td>
        <td>{RF10_rev_e_MS}<br/>{left_bracket}{RF10_rev_e_RS}{right_bracket}</td>
    </tr>
    <tr><td>Shallow-water snappers</td><td>{RF10_land_e_SS}</td><td>{RF10_rev_e_SS}</td></tr>
    <tr><td>Shallow-water groupers</td><td>{RF10_land_e_SG}</td><td>{RF10_rev_e_SG}</td></tr>
    <tr><td>Deep-water groupers</td><td>{RF10_land_e_DG}</td><td>{RF10_rev_e_DG}</td></tr>
    <tr><td>Tilefishes</td><td>{RF10_land_e_TF}</td><td>{RF10_rev_e_TF}</td></tr>
    <tr><td>Jacks</td><td>{RF10_land_e_JA}</td><td>{RF10_rev_e_JA}</td></tr>
    <tr><td>Triggerfishes</td><td>{RF10_land_e_TR}</td><td>{RF10_rev_e_TR}</td></tr>
    <tr><td>Grunts and porgies</td><td>{RF10_land_e_GP}</td><td>{RF10_rev_e_GP}</td></tr>
    <tr><td>Coastal pelagic</td><td>{RF10_land_e_CP}</td><td>{RF10_rev_e_CP}</td></tr>
    <tr><td>Other species</td><td>{other_species_land}</td><td>{other_species_rev}</td></tr>

    <tr><th colspan=3 class="col-1"><b>Time period</b></td></tr>
    <tr><td>2007-2014</td><td>{RF10_land_t_2007_2014}</td><td>{RF10_rev_t_2007_2014}</td></tr>
    <tr><td>2015-2021</td><td>{RF10_land_t_2015_2021}</td><td>{RF10_rev_t_2015_2021}</td></tr>

    <tr><th colspan=3 class="col-1"><b>State</b></td></tr>
    <tr><td>Florida</td><td>{RF10_land_s_FL}</td><td>{RF10_rev_s_FL}</td></tr>
    <tr><td>Alabama</td><td>{RF10_land_s_AL}</td><td>{RF10_rev_s_AL}</td></tr>
    <tr><td>Mississippi</td><td>{RF10_land_s_MS}</td><td>{RF10_rev_s_MS}</td></tr>
    <tr><td>Louisiana</td><td>{RF10_land_s_LA}</td><td>{RF10_rev_s_LA}</td></tr>
    <tr><td>Texas</td><td>{RF10_land_s_TX}</td><td>{RF10_rev_s_TX}</td></tr>
  </tbody>
</table>

<!-- {comments} -->
"""


# Filename: Reef Fish Landings and Revenues (2007-2021),,
#           or {name} (otherwise unused)
reef_csv = """,Landings (pounds),Revenues (USD)
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


''' unused:
OrderedDict([
    ('Red Snapper', ['RF10_land_e_RS', 'RF10_rev_e_RS']),
    ('Mid-depth snappers', ['RF10_land_e_MS', 'RF10_rev_e_MS']),
    ('Shallow-water snappers', ['RF10_land_e_SS', 'RF10_rev_e_SS']),
    ('Shallow-water groupers', ['RF10_land_e_SG', 'RF10_rev_e_SG']),
    ('Deep-water groupers', ['RF10_land_e_DG', 'RF10_rev_e_DG']),
    ('Tilefishes', ['RF10_land_e_TF', 'RF10_rev_e_TF']),
    ('Jacks', ['RF10_land_e_JA', 'RF10_rev_e_JA']),
    ('Triggerfishes', ['RF10_land_e_TR', 'RF10_rev_e_TR']),
    ('Grunts and porgies', ['RF10_land_e_GP', 'RF10_rev_e_GP']),
    ('Coastal pelagic', ['RF10_land_e_CP', 'RF10_rev_e_CP']),
    ('2007-2014', ['RF10_land_t_2007_2014', 'RF10_rev_t_2007_2014']),
    ('2015-2021', ['RF10_land_t_2015_2021', 'RF10_rev_t_2015_2021']),
    ('Florida', ['RF10_land_s_FL', 'RF10_rev_s_FL']),
    ('Alabama', ['RF10_land_s_AL', 'RF10_rev_s_AL']),
    ('Mississippi', ['RF10_land_s_MS', 'RF10_rev_s_MS']),
    ('Louisiana', ['RF10_land_s_LA', 'RF10_rev_s_LA']),
    ('Texas', ['RF10_land_s_TX', 'RF10_rev_s_TX'])
])
'''

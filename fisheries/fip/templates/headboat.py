headboat_template = """
<p style="text-align: center; font-size: 20px; font-weight: bold;">Head boat data</p>
<p style="display: flex; justify-content: center; align-items: center;">Download <button style="margin-left: 5px; font-size: 8px;" id="download-csv" onclick='window.fipCsvReport({feature},"headboat");'>CSV</button></p>
<br/>
<table class="table fip-table">
  <thead>
    <tr><th class="col-1"><b>{name}</b></th><th colspan="2"><b>Total Revenues (USD)</b></th></tr>
  </thead>
  <tbody>
    <tr><td class="col-1"><b>Overall Revenues</b></td><td colspan="2">{tot_rev}</td></tr>
  </tbody>
</table>

<br/>

<!-- {comments} -->
"""


headboat_csv = """,Total Revenues (USD)
Overall Revenues (USD),{tot_rev}
"""

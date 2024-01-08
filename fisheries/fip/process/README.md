Locally:
```bash
pip install -r requirements.txt
export POSTGRES_PASSWORD=admin
python3 pyfip/table_read_example.py hb  # (table_name)

```

Or debug inside the fip-pygeoapi-1 container:
```
docker exec -it fip-pygeoapi-1 bash
export POSTGRES_PASSWORD=admin
python3
```

```python
from pygeoapi.process.fip.pyfip.table_read_example import main
# call get_first_row_of_table() via main
main('hb')
```

TODO: Instantiate a pygepoapi process an exectute from Python interpreter
 
Implement the mechanism - send a table name (identifier) and a latitude and longitude to a pygeoapi process and get it to do a spatial query on the named table and return the data.

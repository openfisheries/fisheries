"""
Generate import commands

Currently we're installing PostGIS extensions on the host (and dev machine) in order to import, 220 Mb
Installing PostGIS doesn't install and run Postgres

$ sudo apt install postgis

raster2pgsql -I -C -s <SRID> <your_geotiff_file> <destination_table> | psql -d <database_name> -U <username>

NOTE: Like the RF species tiffs, the SF may all be the same size (and could therefore be loaded into a single table)
      some of the other tiffs have different dimensions and it seems easier at the moment to load one raster
      per table.
"""

species_lookup = {
    'BS': 'Brown shrimp',
    'WS': 'White shrimp',
    'S': 'Seabobs',
    'RS': 'Rock shrimp',
    'T': 'Trachypenaeus',
    'PS': 'Pink shrimp',
    'RRS': 'Royal red shrimp',
}

times_lookup = {
    '2007_2014': '2007-2014',
    '2015_2021': '2015-2021',
}

states_lookup = {
    'FL': 'Florida',
    'AL': 'Alabama',
    'MS': 'Mississippi',
    'LA': 'Louisiana',
    'TX': 'Texas',
}

import_commands = """
raster2pgsql -I -C -s 3083 fip-data/fip-data/fromR/10kmGrids/SF/SF10_land_{type}_{acronym}.tif SF10_land_{type}_{acronym} | psql -h localhost -d fip -U fip
raster2pgsql -I -C -s 3083 fip-data/fip-data/fromR/10kmGrids/SF/SF10_rev_{type}_{acronym}.tif SF10_rev_{type}_{acronym} | psql -h localhost -d fip -U fip
"""


for acronym in species_lookup:
    print(import_commands.format(type='e', acronym=acronym))  # SEE same table import below

for acronym in times_lookup:
    print(import_commands.format(type='t', acronym=acronym))

for acronym in states_lookup:
    print(import_commands.format(type='s', acronym=acronym))


'''
# ---- combined table version ----
# We're not using this code, but species could all be imported into the same table because the rasters are the same size
# The other tables would fail because the rasters are not the same dimensions
import_commands = """
raster2pgsql {append} -I -C -s 3083 fip-data/fip-data/fromR/10kmGrids/RF/RF10_land_{type}_{acronym}.tif RF10_land_{tbl_name} | psql -h localhost -d fip -U fip
raster2pgsql {append} -I -C -s 3083 fip-data/fip-data/fromR/10kmGrids/RF/RF10_rev_{type}_{acronym}.tif RF10_rev_{tbl_name} | psql -h localhost -d fip -U fip
"""

for n, acronym in enumerate(species_lookup):
    append = '-a' if n else ''
    tbl_name = 'e_SPECIES'
    print(import_commands.format(type='e', acronym=acronym, tbl_name=tbl_name, append=append))
'''

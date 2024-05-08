# **IGNORE THIS SCRIPT** - shapefiles are already imported to the database by
# `python3 fip-data/utils/python/ingest_shapefiles.py`

"""
Generate import commands

Follow instructions in pg_raster_import.py to install PostGIS extensions on the host in order to import
Installing PostGIS doesn't install and run Postgres

"""

base_path = '/home/ubuntu/fip-data/fip-data/OutputData/FishingTerritories/'
rf_path = 'ReefFish_Territories/ReefFish_territories_locoh.shp'
sf_path = 'Shrimp_territories/shrimp_allyears_KDE.shp'

rf_shp = base_path + rf_path
sf_shp = base_path + sf_path
rf_table = 'ReefFish_territories_locoh'
sf_table = 'shrimp_allyears_KDE'

for shpfile, tbl in [(rf_shp, rf_table), (rf_table, sf_table)]:
    print(f'shp2pgsql -I -s 3083 {shpfile} {tbl} | psql -h localhost -d fip -U fip')

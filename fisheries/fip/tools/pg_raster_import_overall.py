"""
Overall landings and revenue data were not imported into the database in
`pg_raster_import`, so they were manually added later...

/RF/RF10_land_overall.tif
/RF/RF10_rev_overall.tif
/SF/SF10_land_overall.tif
/SF/SF10_rev_overall.tif

raster2pgsql -I -C -s 3083 fip-data/fip-data/fromR/10kmGrids/RF/RF10_land_overall.tif rf10_land_overall | psql -h localhost -d fip -U fip
raster2pgsql -I -C -s 3083 fip-data/fip-data/fromR/10kmGrids/RF/RF10_rev_overall.tif rf10_rev_overall | psql -h localhost -d fip -U fip
raster2pgsql -I -C -s 3083 fip-data/fip-data/fromR/10kmGrids/SF/SF10_land_overall.tif sf10_land_overall | psql -h localhost -d fip -U fip
raster2pgsql -I -C -s 3083 fip-data/fip-data/fromR/10kmGrids/SF/SF10_rev_overall.tif sf10_rev_overall | psql -h localhost -d fip -U fip

"""

"""
There is a HB shapefile (from StatGrids) and HB.tif (from 10kmGrids) but on the live server
there was only a vector database table called `hb`... so either HB.tif wasn't uploaded or it
was overwritten. Therefore...

ALTER TABLE hb RENAME TO hb_shp;

raster2pgsql -I -C -s 3083 fip-data/fip-data/fromR/10kmGrids/HB/HB.tif HB | psql -h localhost -d fip -U fip

"""

-- Test with local database, e.g.: docker pull timescale/timescaledb-ha:pg16
-- docker run --name devdb -e POSTGRES_PASSWORD=admin -p 5432:5432 -d timescale/timescaledb-ha:pg16
-- docker start devdb
--
-- Given: `pg_dump -U fip -h localhost -d fip -F c -f yyyy-mm-dd_fip_backup.pgdump`
-- and: `scp -i ~/fip/keys/fip-virginia-key.pem ubuntu@fisheries.us.org:/home/ubuntu/2024-04-21_fip_backup.pgdump`
--
-- brew install libpq
-- brew link --force libpq
--
-- psql -h localhost -U postgres -c "CREATE USER fip WITH LOGIN PASSWORD 'admin';"
-- -- psql -h localhost -U postgres -c "ALTER ROLE fip CREATEDB CREATEROLE;"  -- or...
-- psql -h localhost -U postgres -c "ALTER ROLE fip SUPERUSER;"
--
-- export PGPASSWORD='admin'; export PGUSER='fip'; export PGDATABASE='fip'; export PGHOST='localhost'; export PGPORT='5432';
--
-- Uses environment variables except where overridden (e.g. -U postgres)
-- createdb -U postgres fip
-- psql -U postgres -c "CREATE EXTENSION postgis;"
-- pg_restore -d fip 2024-04-21_fip_backup.pgdump

WITH query AS (
  SELECT ST_GeomFromText('POLYGON((2975206.2278075265 7305263.57216,3005159.353245655 7305197.212714661,3005555.7820766345 7274098.9,2974811.9170059203 7274773.793788631,2975206.2278075265 7305263.57216))', 3083) AS geom
),
squares AS (
  SELECT
    (ST_DumpAsPolygons(rast)).*  -- geom, val
  FROM
    RF10_land_e_RS
),
interim AS (
  SELECT
    ST_Intersection(squares.geom, query.geom) AS geom,
	  ST_Area(  (ST_Intersection(squares.geom, query.geom))  ) AS new_area,
	  squares.val AS original_value,
	  ST_Area(squares.geom) AS original_area
  FROM
    squares, query
  WHERE
    ST_Intersects(squares.geom, query.geom)
)
SELECT
    geom,
    original_value,
    new_area / original_area AS proportion,
    original_value * (new_area / original_area) AS weighted_value
FROM interim;








----
-- 1. Create query polygon as tmp_QueryPoly

CREATE TABLE tmp_QueryPoly AS

SELECT ST_GeomFromText(
    'POLYGON((2975206.2278075265 7305263.57216,3005159.353245655 7305197.212714661,3005555.7820766345 7274098.9,2974811.9170059203 7274773.793788631,2975206.2278075265 7305263.57216))',
    3083
) AS geom;


-- 2.

WITH query AS (
  SELECT ST_GeomFromText('POLYGON((2975206.2278075265 7305263.57216,3005159.353245655 7305197.212714661,3005555.7820766345 7274098.9,2974811.9170059203 7274773.793788631,2975206.2278075265 7305263.57216))', 3083) AS geometry
),
squares AS (
  SELECT
    ST_DumpAsPolygons(rast).geom AS geometry,
    ST_DumpAsPolygons(rast).val AS value
  FROM
    RF10_land_e_RS
)
SELECT
  ST_Intersection(squares.geometry, query.geometry) AS geom,
  squares.value AS original_value,
  ST_Area(geom) / ST_Area(squares.geometry) AS proportion,
  original_value * proportion AS weighted_value
FROM
  squares, query
WHERE
  ST_Intersects(squares.geometry, query.geometry);




--
--works..

WITH polygon_geometry AS (
  SELECT ST_GeomFromText('POLYGON((2975206.2278075265 7305263.57216,3005159.353245655 7305197.212714661,3005555.7820766345 7274098.9,2974811.9170059203 7274773.793788631,2975206.2278075265 7305263.57216))', 3083) AS geom
),
all_raster_cells AS (
  SELECT
    (ST_DumpAsPolygons(rast)).*  -- geom, val
  FROM
    RF10_land_e_RS
)
SELECT
  all_raster_cells.geom,
  all_raster_cells.val
FROM
  all_raster_cells, polygon_geometry
WHERE
  ST_Intersects(all_raster_cells.geom, polygon_geometry.geom);



---

CREATE TABLE intersection_result_3 AS

SELECT 
    a.raster_value AS original_value,
    ST_Area(ST_Intersection(a.polygon_geometry, query.geom)) / ST_Area(a.polygon_geometry) AS proportion,
    original_value * proportion AS weighted_value,
    ST_Intersection(a.polygon_geometry, query.geom) AS geom
FROM 
    poly2_RF10_land_e_RS a,
    (SELECT ST_GeomFromText(
        'POLYGON((2975206.2278075265 7305263.57216,3005159.353245655 7305197.212714661,3005555.7820766345 7274098.9,2974811.9170059203 7274773.793788631,2975206.2278075265 7305263.57216))',
        3083
    ) AS geom) AS query
WHERE 
    ST_Intersects(a.polygon_geometry, query.geom);




---------
-- This works (but requires converting all rasters to polygon tables first...)

CREATE TABLE intersection_result2 AS

SELECT 
    a.raster_value AS original_value,
    ST_Area(ST_Intersection(a.polygon_geometry, query.geom)) / ST_Area(a.polygon_geometry) AS proportion,
    original_value * proportion AS weighted_value,
    ST_Intersection(a.polygon_geometry, query.geom) AS geom
FROM 
    poly2_RF10_land_e_RS a,
    (SELECT ST_GeomFromText(
        'POLYGON((2975206.2278075265 7305263.57216,3005159.353245655 7305197.212714661,3005555.7820766345 7274098.9,2974811.9170059203 7274773.793788631,2975206.2278075265 7305263.57216))',
        3083
    ) AS geom) AS query
WHERE 
    ST_Intersects(a.polygon_geometry, query.geom);

--SELECT AddGeometryColumn('intersection_result', 'geom', 3083, 'GEOMETRY', 2);
--CREATE INDEX idx_intersection_geometry ON intersection_result USING GIST (intersection_geom);


-- Using the GDAL tool below only retains the values as integers - not floats
-- QGIS > View > Panels > Processing Toolbox > "Polygonize (Raster to Vector)" (GDAL raster conversion)
-- therefore...

-- clipped raster only selects raster cells where the centre intersects
-- replacing rasters with polygon versions...
CREATE TABLE poly2_RF10_land_e_RS AS
SELECT 
  (ST_DumpAsPolygons(rast)).geom AS polygon_geometry,
  (ST_DumpAsPolygons(rast)).val AS raster_value
FROM 
  RF10_land_e_RS;









-- 2. Create clipped raster as tmp_clippedRaster
CREATE TABLE tmp_clippedRaster AS

WITH QueryPoly AS
    SELECT ST_GeomFromText(
        'POLYGON((2975206.2278075265 7305263.57216,3005159.353245655 7305197.212714661,3005555.7820766345 7274098.9,2974811.9170059203 7274773.793788631,2975206.2278075265 7305263.57216))',
        3083
    ) AS geom

SELECT 
    ST_Clip(rast, geom) AS clipped_rast 
FROM 
    RF10_land_e_RS,
    QueryPoly;


WITH QueryPoly AS (
    SELECT ST_GeomFromText(
        'POLYGON((2975206.2278075265 7305263.57216,3005159.353245655 7305197.212714661,3005555.7820766345 7274098.9,2974811.9170059203 7274773.793788631,2975206.2278075265 7305263.57216))',
        3083
    ) AS geom
)
SELECT 
    ST_Clip(rast, geom) AS clipped_rast 
FROM 
    RF10_land_e_RS,
    QueryPoly;




WITH clipped_raster AS (
    SELECT 
        ST_Clip(rast, ST_GeomFromText('POLYGON((2975206.2278075265 7305263.57216,3005159.353245655 7305197.212714661,3005555.7820766345 7274098.9,2974811.9170059203 7274773.793788631,2975206.2278075265 7305263.57216))', 3083))
        AS clipped_rasters
    FROM 
        raster_info
),

-- Test:
-- SELECT count(*) FROM clipped_rasters  -- (1 row)

-- CTE to extract all raster cell polygons
all_cells AS (
    SELECT
        (ST_PixelAsPolygons(clipped_rast)).*  -- Convert each raster pixel to a polygon
    FROM
        clipped_rasters
)

-- CREATE TABLE all_cells_as_poly AS  -- place this line before CTE WITH
SELECT * FROM all_cells


-- CTE to identify edge cells
edge_cells AS (
    SELECT
        geom,
        val
    FROM
        all_cells
    WHERE
        -- Cells that are not entirely within the original polygon are considered edge cells
        NOT ST_Within(geom, (SELECT geom FROM raster_info))
),

-- CTE to identify non-edge cells by excluding edge cells from all cells
non_edge_cells AS (
    SELECT
        a.geom,
        a.val
    FROM
        all_cells a
    LEFT JOIN
        edge_cells e ON a.geom = e.geom AND a.val = e.val
    WHERE
        e.geom IS NULL
)

-- Final SELECT to return geometry and values of non-edge cells
SELECT
    geom,  -- Geometry of each non-edge cell
    val    -- Value of each non-edge cell
FROM 
    non_edge_cells;


-----------
-- TESTS --
-----------

-- WITH raster_info
-- can be tested with polygons that do/don not intesect and counting the number of returned rows
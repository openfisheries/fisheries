-------------------------------------------------
-- non-null raster values from the whole table --
-------------------------------------------------
SELECT fromraster.values FROM (
    SELECT unnest(ST_DumpValues(rast, 1, true)) AS values
    FROM RF10_land_e_RS WHERE rid = 1 
) AS fromraster
WHERE values IS NOT NULL;

--------------------------------------------------------
-- non-null raster values after clipping with polygon --
--------------------------------------------------------

-- Common Table Expression (CTE) to clip raster using polygon

-- original test_feature returned 0 rows
WITH clipped_raster AS (
    SELECT ST_Clip(
        rast,
        ST_GeomFromText(
            'POLYGON ((2985198.053235203 7294767.685572192, 2994824.5092220223 7294802.009095271, 2994776.0094108097 7284952.735455229, 2985046.574731292 7284703.34408373, 2985198.053235203 7294767.685572192))', 3083)
        ) AS clipped_raster
    FROM RF10_land_e_RS
    WHERE rid = 1
)

-- test_feature2 returns 14 rows

WITH clipped_raster AS (
    SELECT ST_Clip(
        rast,
        ST_GeomFromText(
'POLYGON((2975206.2278075265 7305263.57216,3005159.353245655 7305197.212714661,3005555.7820766345 7274098.9,2974811.9170059203 7274773.793788631,2975206.2278075265 7305263.57216))', 3083)
        ) AS clipped_raster
    FROM RF10_land_e_RS
    WHERE rid = 1
)

SELECT fromraster.values FROM (
    SELECT unnest(ST_DumpValues(clipped_raster, 1, true)) AS values
    FROM clipped_raster
) AS fromraster
WHERE values IS NOT NULL;


--------------------------------------
-- non-null raster values centroids --
--------------------------------------

-- test_feature returns 0 rows
-- test_feature2 returns 14 rows

SELECT ST_Value(rast, geom) AS value, ST_AsText(geom) AS centroid
FROM RF10_land_e_RS,
LATERAL ST_PixelAsCentroids(rast) AS geom
WHERE ST_Intersects(
  geom,
  ST_GeomFromText(
    'POLYGON((2975206.2278075265 7305263.57216,3005159.353245655 7305197.212714661,3005555.7820766345 7274098.9,2974811.9170059203 7274773.793788631,2975206.2278075265 7305263.57216))'
    , 3083)
);

-- Calculate sum instead of listing values (849282.595703125)
SELECT sum(ST_Value(rast, geom)) AS value
FROM RF10_land_e_RS,
LATERAL ST_PixelAsCentroids(rast) AS geom
WHERE ST_Intersects(
  geom,
  ST_GeomFromText(
    'POLYGON((2975206.2278075265 7305263.57216,3005159.353245655 7305197.212714661,3005555.7820766345 7274098.9,2974811.9170059203 7274773.793788631,2975206.2278075265 7305263.57216))'
    , 3083)
);


------------------------------------------------
-- Summary stats after clipping with polygon  --
------------------------------------------------
-- For a single polygon geom (with same SRID) get summary stats:
-- count | sum | mean | stddev | min | max
-- SELECT ST_SummaryStats(ST_Clip(rast, geom)) ...


SELECT 
    (ST_SummaryStats(ST_Clip(rast, geom))).*
FROM 
    RF10_land_e_RS,
    (SELECT ST_GeomFromText('POLYGON ((2985198.053235203 7294767.685572192, 2994824.5092220223 7294802.009095271, 2994776.0094108097 7284952.735455229, 2985046.574731292 7284703.34408373, 2985198.053235203 7294767.685572192))', 3083) AS geom) AS my_polygon
WHERE 
    ST_Intersects(rast, geom);


SELECT 
    ST_Clip(rast, geom) AS clipped_raster
FROM 
    RF10_land_e_RS,
    (SELECT ST_GeomFromText('POLYGON ((2985198.053235203 7294767.685572192, 2994824.5092220223 7294802.009095271, 2994776.0094108097 7284952.735455229, 2985046.574731292 7284703.34408373, 2985198.053235203 7294767.685572192))', 3083) AS geom) AS my_polygon

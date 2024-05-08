-- PHASE II Polygon query
--
-- Description:
-- For performance, we should only calculate the proportion where the cell is on the
-- edge of the polygon and not explicitly calculate that 100% of a non-edge cell falls inside.
--
-- Recommendations:
-- Polygon reports should not have to return real-time
-- DBT could be used to manage the queries


-- Common Table Expression (CTE) to get raster data intersecting with a specific polygon
-- In our case we currently have one raster per table (due to not all rasters having the
-- same properties), therefore this query will return zero of one rows depending on whether
-- the raster overall intersects the polygon. See below for tests
WITH raster_info AS (
    -- Select raster and a manually defined polygon geometry
    SELECT 
        rast, 
        geom
    FROM 
        RF10_land_e_RS,  -- Your raster data table
        -- Define the polygon with specified coordinates and SRID 3083
        (SELECT ST_GeomFromText('POLYGON((2975206.2278075265 7305263.57216,3005159.353245655 7305197.212714661,3005555.7820766345 7274098.9,2974811.9170059203 7274773.793788631,2975206.2278075265 7305263.57216))', 3083) AS geom) AS my_polygon
    WHERE 
        ST_Intersects(rast, geom)  -- Select only rasters that intersect with the polygon
),

-- SELECT count(*) FROM raster_info  -- (1 row)

-- CTE to clip the raster data by the intersecting polygon's geometry
-- note `geom` is available as one of the two columns returned in raster_info
-- This CTE returns a single column called `clipped_rast` (with a single row returned)
clipped_rasters AS (
    SELECT 
        ST_Clip(rast, geom) AS clipped_rast  -- Clip raster to the boundary of the polygon
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
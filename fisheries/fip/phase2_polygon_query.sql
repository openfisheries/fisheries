-- PHASE II Polygon query
--
-- Description:
-- For performance, we should only calculate the proportion where the cell is on the
-- edge of the polygon and not explicitly calculate that 100% of a non-edge cell falls inside.
--
-- Recommendations:
-- Polygon reports should not have to return real-time
-- DBT should be used to manage the queries


-- Common Table Expression (CTE) to get raster data intersecting with a specific polygon
WITH raster_info AS (
    -- Select raster and a manually defined polygon geometry
    SELECT 
        rast, 
        geom
    FROM 
        RF10_land_e_RS,  -- Your raster data table
        -- Define the polygon with specified coordinates and SRID 3083
        (SELECT ST_GeomFromText('POLYGON ((2985198.053235203 7294767.685572192, 2994824.5092220223 7294802.009095271, 2994776.0094108097 7284952.735455229, 2985046.574731292 7284703.34408373, 2985198.053235203 7294767.685572192))', 3083) AS geom) AS my_polygon
    WHERE 
        ST_Intersects(rast, geom)  -- Select only rasters that intersect with the polygon
),

-- CTE to clip the raster data by the intersecting polygon's geometry
clipped_rasters AS (
    SELECT 
        ST_Clip(rast, geom) AS clipped_rast  -- Clip raster to the boundary of the polygon
    FROM 
        raster_info
),

-- CTE to extract all raster cell polygons
all_cells AS (
    SELECT
        (ST_PixelAsPolygons(clipped_rast)).*  -- Convert each raster pixel to a polygon
    FROM
        clipped_rasters
),

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

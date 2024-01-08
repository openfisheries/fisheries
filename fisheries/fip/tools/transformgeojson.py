# Note: transform_geojson is not in use since GeoJSON standard only supports
# EPSG:4326. The transform from Web Mercator is now done by OpenLayers in the client.
from typing import Dict
from shapely.geometry import shape, base
from shapely.ops import transform
from pyproj import Transformer


def transform_geojson(geojson: Dict, 
                      input_crs: str = "EPSG:3857", 
                      output_crs: str = "EPSG:4326") -> base.BaseGeometry:
    """
    Transform the coordinates of a GeoJSON object from one coordinate reference 
    system (CRS) to another, with default transformation from Web Mercator 
    (EPSG:3857) to WGS 84 (EPSG:4326) CRS.

    Parameters:
    geojson : Dict
        A GeoJSON object representing the geographic data to be transformed.
    input_crs : str, optional
        The CRS of the input GeoJSON object. Default is 'EPSG:3857'.
    output_crs : str, optional
        The CRS to which the GeoJSON object's coordinates will be transformed. 
        Default is 'EPSG:4326'.

    Returns:
    shapely.geometry.base.BaseGeometry
        A Shapely geometry object with coordinates transformed to the specified 
        output CRS.

    Example:
    >>> from shapely.geometry import Point
    >>> point_geojson = Point(5000000, 8500000).__geo_interface__
    >>> transformed_point = transform_geojson(point_geojson, "EPSG:3857", "EPSG:4326")
    >>> print(transformed_point)
    POINT (-44.840290651397986 70.61261423801925)

    Note:
    - The function allows specifying both input and output CRS.
    - The default input CRS is 'EPSG:3857', and the default output CRS is 'EPSG:4326'.
    """
    geometry = shape(geojson)
    transformer = Transformer.from_crs(input_crs, output_crs, always_xy=True)
    return transform(lambda x, y: transformer.transform(x, y), geometry)

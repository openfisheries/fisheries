from geoalchemy2.functions import ST_Point, ST_Transform

# Create a WKT point element from the given latitude and longitude with WGS 84 SRID
point_wgs84 = ST_Point(longitude, latitude, srid=4326)

# Transform the point to the SRID of the geometry column in the table (SRID 4269 in this example)
point_transformed = ST_Transform(point_wgs84, 4269)

# Query the CountiesEdited table to find all counties containing the given point
counties_containing_point = session.query(CountiesEdited).filter(
    func.ST_Contains(CountiesEdited.wkb_geometry, point_transformed)
).all()


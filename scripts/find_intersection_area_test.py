from shapely.geometry import Polygon

def intersection_area(rect1_coords, rect2_coords):
    rect1_polygon, rect2_polygon = Polygon(rect1_coords), Polygon(rect2_coords)
    intersection = rect1_polygon.intersection(rect2_polygon)
    return intersection.area
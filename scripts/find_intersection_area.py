import math

def find_intersection_area(rect1, rect2):
    def shoelace_area(vertices):
        n = len(vertices)
        area = 0.0
        for i in range(n):
            j = (i + 1) % n
            area += (vertices[i][0] * vertices[j][1]) - (vertices[j][0] * vertices[i][1])
        return abs(area) / 2.0

    def get_intersection_points(rect1, rect2):
        # Check for intersection between edges of the rectangles
        def intersect(a, b, c, d):
            def ccw(A, B, C):
                return (C[1] - A[1]) * (B[0] - A[0]) > (B[1] - A[1]) * (C[0] - A[0])

            return ccw(a, c, d) != ccw(b, c, d) and ccw(a, b, c) != ccw(a, b, d)

        intersection_points = []

        for i in range(4):
            p1, p2 = rect1[i], rect1[(i + 1) % 4]
            for j in range(4):
                q1, q2 = rect2[j], rect2[(j + 1) % 4]
                if intersect(p1, p2, q1, q2):
                    intersection_points.append((p1, p2, q1, q2))

        return intersection_points

    intersection_points = get_intersection_points(rect1, rect2)

    if not intersection_points:
        return 0.0

    # Function to find polar angle with respect to the reference point
    def polar_angle(point, reference):
        return math.atan2(point[1] - reference[1], point[0] - reference[0])

    # Find the centroid of the intersection polygon to use as the reference point
    centroid_x = sum(point[0] for points in intersection_points for point in points) / len(intersection_points) / 4
    centroid_y = sum(point[1] for points in intersection_points for point in points) / len(intersection_points) / 4
    reference_point = (centroid_x, centroid_y)

    # Sort the intersection points counterclockwise based on polar angle with respect to the reference point
    intersection_points.sort(key=lambda points: polar_angle(points[0], reference_point))

    # Get intersection area using Shoelace formula for each intersection polygon
    total_area = 0.0
    for points in intersection_points:
        intersection_vertices = [points[0], points[2], points[1], points[3]]
        total_area += shoelace_area(intersection_vertices)

    return total_area

if __name__ == "__main__":
    rectangle1 = [(0, 0), (3, 0), (3, 3), (0, 3)]
    rectangle2 = [(1, 1), (4, 1), (4, 4), (1, 4)]
    find_intersection_area(rectangle1, rectangle2)
# -*- coding: utf-8 -*-
import math

def find_intersection_area(rect1, rect2):
    def shoelace_area(vertices):
        n = len(vertices)
        area = 0.0
        for i in range(n):
            j = (i + 1) % n
            area += (vertices[i][0] * vertices[j][1]) - (vertices[j][0] * vertices[i][1])
        return abs(area) / 2.0
    
    def get_line(p1, p2):
        # 선분을 지나는 선을 구하는 함수
        x1, y1 = p1
        x2, y2 = p2
        # Calculate the slope (m) of the line
        if x2 - x1 != 0:
            slope = (y2 - y1) / (x2 - x1)
        else:
            # Handle the case when the line is vertical (infinite slope)
            return x1 # x 값 하나만 있어도 선을 구분할 수 있기에, x 값 하나만 반환한다.

        # Calculate the y-intercept (b) of the line
        intercept = y1 - slope * x1

        # Construct the equation of the line in string format
        return (slope, intercept)

    def get_intersection_points(rect1, rect2):
        

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
    # 테스트 코드
    rectangle1 = [(0, 0), (3, 0), (3, 3), (0, 3)]
    rectangle2 = [(1, 1), (4, 1), (4, 4), (1, 4)]
    area = find_intersection_area(rectangle1, rectangle2)
    print(area)
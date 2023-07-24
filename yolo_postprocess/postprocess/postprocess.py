import os
import glob
import pandas as pd
import numpy as np
from shapely.geometry import Polygon

def get_oriented_bbox(points, scale_factor=0.9):
    # Create a shapely polygon object from the convex hull of the points
    poly = Polygon(points)

    # Find the minimum area bounding rectangle
    min_rect = poly.minimum_rotated_rectangle

    # Downscale the rectangle
    min_rect_coords = np.array(min_rect.exterior.coords[:-1])
    # center = min_rect_coords.mean(axis=0)
    # min_rect_coords = (min_rect_coords - center) * scale_factor + center

    return min_rect_coords

def process_files(directory):
    # Prepare data for the CSV file
    data = []

    # Get all txt files in the directory
    files = glob.glob(os.path.join(directory, "*.txt"))

    for file_path in files:
        # Load the file
        with open(file_path, 'r') as f:
            lines = f.readlines()

        # Parse the file
        instances = []
        for line in lines:
            fields = line.strip().split(' ')
            class_index = fields[0]
            confidence = float(fields[-1])
            coordinates = [float(x) * 1024 for x in fields[1:-1]]  # De-normalizing
            # Group coordinates into pairs
            coordinates = list(zip(coordinates[::2], coordinates[1::2]))
            instances.append({'class_index': class_index, 'confidence': confidence, 'coordinates': coordinates})

        for instance in instances:
            # Check if there are at least 3 points to form a convex hull
            if len(instance['coordinates']) >= 3:
                obb = get_oriented_bbox(instance['coordinates'])
                row = {
                    'File': os.path.basename(file_path),
                    'Confidence': instance['confidence'],
                    'X1': obb[0][0],
                    'Y1': obb[0][1],
                    'X2': obb[1][0],
                    'Y2': obb[1][1],
                    'X3': obb[2][0],
                    'Y3': obb[2][1],
                    'X4': obb[3][0],
                    'Y4': obb[3][1],
                }
                data.append(row)

    # Convert to a DataFrame
    df = pd.DataFrame(data)

    # Modify the "File" column to keep only the first 8 characters
    df['File'] = df['File'].str[:8]

    # Define CSV file path
    csv_file_path = "/root/v8m-665.csv"

    # Save DataFrame to CSV
    df.to_csv(csv_file_path, index=False)

# Call the function with your directory path
process_files("/root/runs/segment/predict7/labels")
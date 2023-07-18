import cv2
import numpy as np
import argparse

def visualize_labels(image_path, label_path):
    # Load the image
    image = cv2.imread(image_path)

    # Read the label file
    with open(label_path, 'r') as file:
        lines = file.readlines()

    # Iterate over the lines and extract label information
    for line in lines:
        line = line.strip().split()
        coordinates = list(map(int, line[:8]))
        label = line[8]
        difficulty = int(line[9])

        # Draw the bounding box
        pts = [(coordinates[i], coordinates[i+1]) for i in range(0, 8, 2)]
        pts = np.array(pts, np.int32).reshape((-1, 1, 2))
        cv2.polylines(image, [pts], True, (0, 255, 0), 2)

        # Add label text
        label_text = f"{label} ({difficulty})"
        x, y = coordinates[:2]
        cv2.putText(image, label_text, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

    # Display the image with labels
    cv2.imshow("Image with Labels", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Draws bounding boxes and labels of objects in an image.')
    # Add arguments
    parser.add_argument('--image', type=int, help='Path to an image.')
    parser.add_argument('--label', type=str, help='Path to the corresponding label.')

    # Parse the arguments
    args = parser.parse_args()

    # Access the values of the arguments
    image_path = args.image
    label_path = args.label

    visualize_labels(image_path, label_path)

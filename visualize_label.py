import cv2
import argparse

def draw_boxes(image, boxes):
    for box in boxes:
        label = box[0]
        confidence = float(box[1])
        coordinates = list(map(float, box[2:]))
        
        # Extract x and y coordinates from the clockwise order
        x_coordinates = coordinates[0::2]
        y_coordinates = coordinates[1::2]
        
        # Reshape the coordinates into pairs
        points = [(int(x), int(y)) for x, y in zip(x_coordinates, y_coordinates)]
        
        # Draw the bounding box polygon on the image
        cv2.polylines(image, [points], isClosed=True, color=(0, 255, 0), thickness=2)
        
        # Add label and confidence text above the bounding box
        text = f'{label}: {confidence:.2f}'
        cv2.putText(image, text, (points[0][0], points[0][1] - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Draws bounding boxes and labels of objects in an image.')
    # Add arguments
    parser.add_argument('--image', type=str, help='Path to an image directory')
    parser.add_argument('--label', type=str, help='Path to a label file')
    parser.add_argument('--dest', type=str, help='Path to save visualization results')

    # Parse the arguments
    args = parser.parse_args()

    # Access the values of the arguments
    image_directory_path = args.image
    label_path = args.label
    dest = args.dest
    with open(label_path, 'r') as file:
        lines = file.readlines()
    labels = [line.strip().split(' ') for line in lines]

    # Read and display the image with bounding boxes
    for label in labels:
        image_name = label[0]
        # Determine the absolute image path
        if os.path.isabs(image_directory_path):
            absolute_image_path = os.path.join(image_directory_path, image_name)
        else:
            current_dir = os.getcwd()
            absolute_image_path = os.path.join(current_dir, image_directory_path, image_name)

        image = cv2.imread(absolute_image_path)
        draw_boxes(image, [label])

        # Determine the absolute output path
        if os.path.isabs(dest):
            absolute_output_path = os.path.join(dest, image_name + '_with_labels.jpg')
        else:
            current_dir = os.getcwd()
            absolute_output_path = os.path.join(current_dir, dest, image_name + '_with_labels.jpg')

        cv2.imwrite(absolute_output_path, image)
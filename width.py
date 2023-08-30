import cv2
import numpy as np
import math
import os

pngImages=os.path.join('./segmentationCLASS_PNG ')

def calculate_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

def find_red_x_coordinates(segmented_image_path, y_coordinate):
    segmented_image = cv2.imread(segmented_image_path)

    hsv_image = cv2.cvtColor(segmented_image, cv2.COLOR_BGR2HSV)

    lower_red = np.array([0, 100, 100])
    upper_red = np.array([10, 255, 255])

    red_mask = cv2.inRange(hsv_image, lower_red, upper_red)

    row = red_mask[y_coordinate]

    red_x_coordinates = np.where(row != 0)[0]

    cv2.line(segmented_image, (red_x_coordinates[0], y_coordinate), (red_x_coordinates[-1], y_coordinate), (0, 255, 0), 2)

    return red_x_coordinates,segmented_image

segmented_image_path = "./segmentationCLASS_PNG/1.png"
y_coordinate = 900  # Replace with the desired Y-coordinate
red_x_coordinates=[0]
while red_x_coordinates[0]<10:
    red_x_coordinates,image_with_coordinates= find_red_x_coordinates(segmented_image_path, y_coordinate)
    if red_x_coordinates[0]<10:
        y_coordinate-=50

image_with_coordinates=cv2.resize(image_with_coordinates,(1200,1200))
cv2.imshow("Image with Coordinates", image_with_coordinates)
cv2.waitKey(0)
cv2.destroyAllWindows()

print(f"The X coordinates of red color pixels at Y = {y_coordinate}: {red_x_coordinates}")


# Example usage:
print(red_x_coordinates[0],red_x_coordinates[1])
x1, y1 = red_x_coordinates[0], y_coordinate
x2, y2 = red_x_coordinates[-1], y_coordinate

distance = calculate_distance(x1, y1, x2, y2)
print(f"The distance between ({x1}, {y1}) and ({x2}, {y2}) is: {distance}")

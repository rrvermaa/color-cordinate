import cv2
import os
import numpy as np
import math
from PIL import Image

no=4
image_path = f'results/mask_{no}.png'


def find_first_red_pixel(image_path):
    image = Image.open(image_path)
    width, height = image.size
    
    for y in range(height):
        pixel = image.getpixel((60, y))
        if pixel[0] == 128 and pixel[1] == 0 and pixel[2] == 0:
            return y  
    return 0  

def calculate_slope(x1, y1, x2, y2):
    slope = (y2 - y1) / (x2 - x1)
    return slope

checkColor = find_first_red_pixel(image_path)


image=cv2.imread(image_path)
red = [0,0,128]
Y, X = np.where(np.all(image==red,axis=2))

y1=Y[0]+50
y2=Y[0]+75
y5=Y[-1]-200

upperlist=[]
lowerlist=[]
middlelist=[]

for i,y in enumerate(Y):

    if y==y1:
        upperlist.append(i)

    if y==y2:
        middlelist.append(i)
    if y==y5:
        lowerlist.append(i)


x1=upperlist[0]
x2=upperlist[-1]

x3=middlelist[0]
x4=middlelist[-1]
print(x2,x4)


if checkColor!=0:

    slop1=calculate_slope(X[x1],y1,X[x3],y2)
    x5=0
    y3=int(y1 - ( X[x1]-  x5) * slop1)

    slop2=calculate_slope(X[x2],y1,X[x4],y2)
    x6=2560
    y4=int(y1 - (X[x2]-x6 ) * slop2)


x7=lowerlist[0]
x8=lowerlist[-1]

if y4>=1600:
    y4=y5-100

if y3>=1600:
    y3=y5-100

cv2.circle(image, (X[x4],y2), 5, (0, 255, 0), -1)
cv2.circle(image, (X[x2],y2), 5, (0, 255, 0), -1)

if checkColor!=0:
    cv2.line(image, (X[x1], y1), (X[x2], y1), (0, 255, 0), 2)

    cv2.line(image, (X[x1], y1), (x5, y3), (0, 255, 0), 2)
    cv2.line(image, (X[x2], y1), (x6, y4), (0, 255, 0), 2)
    cv2.line(image, (x5, y3), (X[x7], y5), (0, 255, 0), 2)
    cv2.line(image, (x6, y4), (X[x8], y5), (0, 255, 0), 2)

    cv2.line(image, (X[x7], y5), (X[x8], y5), (0, 255, 0), 2)


else:
    cv2.line(image, (X[x1], y1), (X[x2], y1), (0, 255, 0), 2)
    
    cv2.line(image, (X[x1], y1), (X[x7], y5), (0, 255, 0), 2)
    cv2.line(image, (X[x2], y1), (X[x8], y5), (0, 255, 0), 2)
    
    
    cv2.line(image, (X[x7], y5), (X[x8], y5), (0, 255, 0), 2)

    

cv2.imwrite(f"image_{no}.jpg",image)




# import cv2
# import numpy as np

# image_path = 'results/mask_5.png'
# image = cv2.imread(image_path)

# x0, y0 = 1825, 456
# slope = 0.242718  

# x1 = 2560
# y1 = int(y0 - (x0 - x1) * slope)
# print(y1)
# print(y0 ,x0,x1 ,slope)
# x2 = 1825
# y2 = 456

# image_with_line = image.copy()

# line_color = (0, 0, 255) 
# line_thickness = 2
# cv2.line(image_with_line, (x1, y1), (x2, y2), line_color, line_thickness)

# cv2.imwrite('Image.png', image_with_line)


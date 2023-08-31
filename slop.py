import cv2
import os
import numpy as np
import math
from PIL import Image

for i in range(1,9):

    def find_first_red_pixel(image_path,y3):
        image = Image.open(image_path)
        width, height = image.size
        y2=y3
        for y in range(height):
            pixel = image.getpixel((10, y))
            if pixel[0] == 128 and pixel[1] == 0 and pixel[2] == 0:
                return y  
        return y2

    def find_last_red_pixel(image_path,y3):
        image = Image.open(image_path)
        width, height = image.size
        y4=y3
        for y in range(height):
            pixel = image.getpixel((2550, y))
            if pixel[0] == 128 and pixel[1] == 0 and pixel[2] == 0:
                return y  
        return y4
    
    def interpolate_x(x1, y1, x2, y2, y):
        x = x1 + ((y - y1) * (x2 - x1)) / (y2 - y1)
        return x


    no=i
    image_path = f'results/mask_{no}.png'

    image=cv2.imread(image_path)
    points=4
    red = [0,0,128]
    Y, X = np.where(np.all(image==red,axis=2))

    y1=Y[0]+ 50
    y3=Y[-1]-250


    y2 = find_first_red_pixel(image_path,y3)
    y4 = find_last_red_pixel(image_path,y3)

    upperlist=[]
    lowerlist=[]
    middlelist=[]
    rightlist=[]
    for i,y in enumerate(Y):

        if y==y1:
            upperlist.append(i)

        if y==y3:
            lowerlist.append(i)

        if y==y2:
            middlelist.append(i)
        if y==y4:
            rightlist.append(i)

    x1=upperlist[0]
    x1=(X[x1])-10
    x2=upperlist[-1]
    x2=(X[x2])+10

    x3=lowerlist[0]
    x3=(X[x3])
    x4=lowerlist[-1]
    x4=(X[x4])

    x5=middlelist[0]
    x5=(X[x5])
    x6=rightlist[-1]
    x6=(X[x6])

    check=0
    while True:
            checkImage=image.copy()
            cv2.line(checkImage, (x1, y1), (x5, y2), (0, 255, 0), 2) 
            green = [0,255,0]
            GY, GX = np.where(np.all(checkImage==green,axis=2))
            i=0
            for y in GY:
                i+=1
                try:
                    if ((image[y,GX[i]])[2]==128):
                        check==0
                        break
                except:
                    check=1
                    break
            
            if check==1:
                break

            if x5>0:
                x5-=3

            if check==0:
                y2-=3
                x1-=8

    x5+=2
    y2+=2
    x1+=6

    rightLowerX=int(interpolate_x(x1,y1,x5,y2,1599))

    check=0
    while True:
            checkImage=image.copy()
            cv2.line(checkImage, (x2, y1), (x6, y4), (0, 255, 0), 2) 
            green = [0,255,0]
            GY, GX = np.where(np.all(checkImage==green,axis=2))
            i=0
            for y in GY:
                i+=1
                try:
                    if ((image[y,GX[i]])[2]==128):
                        check==0
                        break
                    
                except:
                    check=1
                    break
            
            if check==1:
                break
            if x6<2558:
                x6+=3

            if check==0:
                y4-=3
                x2+=8
    
    x6-=2
    y4+=2
    x2-=6

    leftLowerX=int(interpolate_x(x2,y1,x6,y4,1599))

    cv2.line(image, (x1, y1), (x2, y1), (0, 255, 0), 2) #upper

    cv2.line(image, (x1, y1), (rightLowerX, 1599), (0, 255, 0), 2) #right edge 
    cv2.line(image, (x2, y1), (leftLowerX, 1599), (0, 255, 0), 2) #left edge 

    cv2.line(image, (rightLowerX, 1599), (leftLowerX, 1599), (0, 255, 0), 2) #bottom

    cv2.imwrite(f'image_{no}.jpg',image)
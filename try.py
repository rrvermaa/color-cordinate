import cv2
import os
import numpy as np
import math
from PIL import Image

for i in range(1,9):
    no=i
    image_path = f'results/mask_{no}.png'
    requiredRight=False
    requiredLeft=False

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

    # checkColor = find_first_red_pixel(image_path)


    image=cv2.imread(image_path)
    red = [0,0,128]
    Y, X = np.where(np.all(image==red,axis=2))

    y1=Y[0]+50
    y2=Y[0]+275
    y5=Y[-1]-250

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
    x1=(X[x1])
    x2=upperlist[-1]
    x2=(X[x2])

    x3=middlelist[0]
    x3=(X[x3])
    x4=middlelist[-1]
    x4=(X[x4])

    print(x2,x4)
    x7=lowerlist[0]
    x7=(X[x7])
    x8=lowerlist[-1]
    x8=(X[x8])



    # if checkColor!=0:

    slop1=calculate_slope(x1,y1,x3,y2)
    x5=x7
    y3=int(y1 - ( x1-  x5) * slop1)
    while True:
            checkImage=image.copy()
            cv2.line(checkImage, (x1-10, y1), (x5, y2), (0, 255, 0), 2) 
            cv2.imwrite('image.png',checkImage)
            green = [0,255,0]
            GY, GX = np.where(np.all(checkImage==green,axis=2))
            i=0
            for y in GY:
                i+=1
                try:
                    if ((image[y,GX[i]])[2]==128):
                        print(GX[i])
                        check==0
                        break
                except:
                    check=1
                    break
            
            if check==1:
                break

            if x5>0:
                x5-=2

            if check==0:
                y2-=2
                x1-=6

    check=0
    while True:
            checkImage=image.copy()
            cv2.line(checkImage, (x2+10, y1), (x6, y4), (0, 255, 0), 2) 
            cv2.imwrite('image.png',checkImage)
            green = [0,255,0]
            GY, GX = np.where(np.all(checkImage==green,axis=2))
            i=0
            for y in GY:
                i+=1
                try:
                    if ((image[y,GX[i]])[2]==128):
                        print(GX[i])
                        check==0
                        break
                    
                except:
                    check=1
                    break
            
            if check==1:
                break
            if x6<2558:
                x6+=2


            if check==0:
                y4-=2
                x2+=6
            

    slop2=calculate_slope(x2,y1,x4,y2)
    x6=x8
    y4=int(y1 - (x2-x6 ) * slop2)

    if y4>1600:
        y4=y5-10
        requiredRight=True
    if y3>1600:
        y3=y5-10
        requiredLeft=True




        
    check=0
    # if requiredLeft:
    # while True:
    #     checkImage1=image.copy()
    #     cv2.line(checkImage1, ((x1)-50, y1), (x5, y3), (0, 255, 0), 2)
    #     green = [0,255,0]
    #     GY, GX = np.where(np.all(checkImage1==green,axis=2))
    #     i=0
    #     for y in GY:
    #         i+=1
    #         try:
    #             if ((image[y,GX[i]])[2]==128):
    #                 check==0
    #                 break
    #         except:
    #             check=1
    #             break
        
    #     if check==1:
    #         break
    #     if check==0:
    #         y3-=10

    # if checkColor!=0:    


    while True:
        checkImage=image.copy()
        cv2.line(checkImage, (x2+50, y1), (x6, y4), (0, 255, 0), 2)
        green = [0,255,0]
        GY, GX = np.where(np.all(checkImage==green,axis=2))
        i=0
        for y in GY:
            i+=1
            try:
                if ((image[y,GX[i]])[2]==128):
                    print(GX[i])
                    check==0
                    break
            except:
                check=1
                break
        
        if check==1:
            break
        if check==0:
            y4-=10


    # if checkColor!=0:
    cv2.line(image, (x1, y1), (x2, y1), (0, 255, 0), 2)

    cv2.line(image, (x1, y1), (x5, y3), (0, 255, 0), 2)
    cv2.line(image, (x2, y1), (x6, y4), (0, 255, 0), 2)
    cv2.line(image, (x5, y3), (x7, y5), (0, 255, 0), 2)
    cv2.line(image, (x6, y4), (x8, y5), (0, 255, 0), 2)

    cv2.line(image, (x7, y5), (x8, y5), (0, 255, 0), 2)


    # else:
    #     cv2.line(image, (x1, y1), (x2, y1), (0, 255, 0), 2)
        
    #     cv2.line(image, (x1, y1), (x7, y5), (0, 255, 0), 2)
    #     cv2.line(image, (x2, y1), (x8, y5), (0, 255, 0), 2)
        
        
    #     cv2.line(image, (x7, y5), (x8, y5), (0, 255, 0), 2)

        

    cv2.imwrite(f"image_{no}.jpg",image)


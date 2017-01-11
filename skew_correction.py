import cv2
import numpy as np
import collections
import math
from scipy import ndimage
import subprocess
from test import show_skew
import os
def find_angle(path):
    image = cv2.imread(path)

    kernel1=np.ones((5,5),np.uint8)

    im_floodfill_inv = cv2.bitwise_not(image)

    im_floodfill_inv = cv2.dilate(im_floodfill_inv, kernel1, iterations=2)
    edges = cv2.Canny(im_floodfill_inv, 50, 150, apertureSize=3)


    #cv2.imshow("image_inv", cv2.resize((im_floodfill_inv),(500,800)))

    angle=0
    line=[]
    lines = cv2.HoughLines(edges, 1, np.pi / 180, 180)
    for rho, theta in lines[0]:
        a = np.cos(theta)
        b = np.sin(theta)
        x0 = a * rho
        y0 = b * rho
        x1 = int(x0 + 1000 * (-b))
        y1 = int(y0 + 1000 * (a))
        x2 = int(x0 - 1000 * (-b))
        y2 = int(y0 - 1000 * (a))
        if abs(x1-x2)>50:
            line.append([x1,y1,x2,y2])

            cv2.line(image, (x1+1000, y1), (x2+1000, y2), (0, 255, 0), 2)

    #cv2.imshow('image', cv2.resize(image, (500,800)))
    #cv2.imshow('image2',cv2.resize(edges,(500,800)))
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    line=np.array(line)

    for i in range(len(line)):
        if line[i][0] != line[i][2]:
            angle += math.atan2(line[i][3] - line[i][1],(line[i][2] - line[i][0]))
    angle_mean = angle/len(line)
    angle_mean = (angle_mean*180)/math.pi
    return angle_mean



def deskew(path,location):
    name = (os.path.basename(str(path)))

    image = cv2.imread(path)
    image_center = tuple(np.array(image.shape[0:2]) / 2)
    angle = find_angle(path)
    print angle
    rot_mat = cv2.getRotationMatrix2D(image_center, -angle, 1.0)
    result = ndimage.rotate(image, angle)
    new_path= location+name
    print new_path
    cv2.imwrite(new_path,result)
    show_skew(new_path)
def manual_deskew(path,angle,location):
    name = (os.path.basename(str(path)))

    image = cv2.imread(path)
    image_center = tuple(np.array(image.shape[0:2]) / 2)

    #rot_mat = cv2.getRotationMatrix2D(image_center, angle, 1.0)
    result = ndimage.rotate(image, angle)
    new_path = location+ name
    print new_path
    cv2.imwrite(new_path, result)
    show_skew(new_path)
    #cv2.warpAffine(image, rot_mat, image.shape[0:2], flags=cv2.INTER_CUBIC)
    #cv2.imshow('orignal',cv2.resize(image,(800,500)))
    #cv2.imshow('result',cv2.resize(result,(800,850))) #ndimage.rotate(image, angle)
    #cv2.waitKey(0)


#deskew('/home/deepayan/testcase/p24.jpg')
# -*- coding: utf-8 -*-
"""
Created on Tue Nov  5 20:21:25 2019

@author: tatha
"""

import os
import cv2 
import numpy as np

def getBoundaries(image):
    thresh = 240
    image = cv2.threshold(image,thresh,255,cv2.THRESH_BINARY)[1]
    
    bounds = list()
    #Order = [u,l,d,r]
    #1.check upper boundary
    flag1 = False
    flag2 = False
    for i in range(100):
        for j in range(100):
            if image[i,j] == 0:
                flag1 = True
                
            if flag1:
                flag2 = True
                bounds.append([i,j])
                break
        if flag2:
            break
        
    
    #2.check left boundary
    flag1 = False
    flag2 = False
    for j in range(100):
        for i in range(100):
            if image[i,j] == 0:
                flag1 = True
            if flag1:
                flag2 = True
                bounds.append([i,j])
                break
        if flag2:
            break
    #3.check down boundary
    flag1 = False
    flag2 = False
    for i in reversed(range(100)):
        for j in range(100):
            if image[i,j] == 0:
                flag1 = True
            if flag1:
                flag2 = True
                bounds.append([i,j])
                break
        if flag2:
            break
        
    
    #4.check right boundary
    flag1 = False
    flag2 = False
    for j in reversed(range(100)):
        for i in range(100):
            if image[i,j] == 0:
                flag1 = True
            if flag1:
                flag2 = True
                bounds.append([i,j])
                break
        if flag2:
            break
        
        
    return bounds

def getCentroid(bounds):
    x = 0
    y = 0
    for vertices in bounds:
        x += vertices[0]
        y += vertices[1]
    
    return [int(x/4),int(y/4)]

def draw_vertexes(image,bounds):
    for i in range(len(bounds)):
        image = cv2.circle(image,tuple(bounds[i]),1,(255,0,0),2)
    

def getImageinYOLO(image_path):
    image = cv2.imread(image_path,0)
    bounds = getBoundaries(image)
    print(bounds)
    image = cv2.cvtColor(image,cv2.COLOR_GRAY2RGB)
    draw_vertexes(image,bounds)
    centroid = getCentroid(bounds)
    image = cv2.circle(image,tuple(centroid),1,(0,255,0),2)
    cv2.namedWindow("image",cv2.WINDOW_NORMAL)
    cv2.resizeWindow("image",100,100)
    cv2.imshow("image",image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
    return image
    
train_path = 'fruits-360_dataset/fruits-360/Training'
classlist = os.listdir(train_path)
for i in range(len(classlist)):
    #print("class: {} ->".format(i))
    if i == 32:
        images = os.listdir(train_path + '/' + classlist[i] + '/')
        for j in range(5):
            iminfo = getImageinYOLO(train_path + '/' + classlist[i] + '/' + images[j])
    """for image in images:
        #create .txt files for each .jpg files with yolo format input
        text_fname = image.split('.')
        f = open(text_fname[0] + ".txt", "w+")
        impath = train_path + '/' + classlist[i] + '/' + image
        #iminfo = getImageinYOLO(impath)
    """     
        
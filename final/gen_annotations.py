# -*- coding: utf-8 -*-
"""
Created on Sat Nov  9 19:17:40 2019

@author: tatha
"""

import os
import cv2


def eval_image(image):
    image = cv2.resize(image,(416,416))
    return image
    
    
def eval_info(image):
    image = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    thresh,image = cv2.threshold(image,240,255,cv2.THRESH_BINARY)
    dims = 416
    mask = list()
    
    for i in range(dims):
        for j in range(dims):
            if image[i,j] == 0:
                mask.append([i,j])
    
    top_vertex = mask[0]
    down_vertex = mask[0]
    left_vertex = mask[0]
    right_vertex = mask[0]   
        
    for elem in mask:
        if elem[1] > top_vertex[1]:
            top_vertex = elem
        if elem[1] < down_vertex[1]:
            down_vertex = elem
        if elem[0] > right_vertex[0]:
            right_vertex = elem
        if elem[0] < left_vertex[0]:
            left_vertex = elem
            
            
    return [top_vertex,down_vertex,left_vertex,right_vertex]

def gcentroid(iminfo):
    x = 0
    y = 0
    for elem in iminfo:
        x += elem[0]
        y += elem[1]
        
    return [float(x/4),float(y/4)]

path = 'data/obj/fruits-360_dataset/fruits-360/Training'
dims = 416
classlist = os.listdir(path)
for i in range(len(classlist)):
    print(classlist[i])
    classpath = path + "/" + classlist[i]
    images = os.listdir(classpath)
    for image in images:
        if not image.endswith(".txt"):
            impath = classpath + "/" + image
            im = cv2.imread(impath)
            im = eval_image(im)
            iminfo = eval_info(im)
            absolute_height = iminfo[0][1] - iminfo[1][1]
            absolute_width = iminfo[3][0] - iminfo[2][0]
            centroid = gcentroid(iminfo)
            text_path = classpath + "/" + image.split(".")[0] + ".txt"
            f = open(text_path,"w")
            f.write("{} {} {} {} {}\n".format(i,float(centroid[0]/dims), float(centroid[1]/dims),float(absolute_width/dims),float(absolute_height/dims)))
            f.close()
            
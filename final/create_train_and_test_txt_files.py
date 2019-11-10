# -*- coding: utf-8 -*-
"""
Created on Thu Nov  7 21:59:59 2019

@author: tatha
"""

import os

f = open("train.txt","w")

train_path = 'data/obj/fruits-360_dataset/fruits-360/Training'
classlist = os.listdir(train_path)
for classes in classlist:
    images = os.listdir(os.path.join(train_path,classes))
    for image in images:
        if image.endswith(".jpg"):
            wstr = train_path + "/" + classes + "/" + image + "\n" 
            f.write(wstr)
            
            
fo = open("test.txt","w")

train_path = 'data/obj/fruits-360_dataset/fruits-360/Test'
classlist = os.listdir(train_path)
for classes in classlist:
    images = os.listdir(os.path.join(train_path,classes))
    for image in images:
        if image.endswith(".jpg"):
            wstr = train_path + "/" + classes + "/" + image + "\n" 
            fo.write(wstr)
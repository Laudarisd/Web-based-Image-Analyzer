# -*- coding: utf-8 -*-
"""
Created on Mon Jun  8 23:42:49 2020

@author: tatha
"""

import os
import argparse
import pandas as pd

def text_to_csv(path, image_path):
    
    text_list = list()
    for files in os.listdir(path):
        
        file = open(os.path.join(path, files),'r')
        for line in file:
            string = [int(x) for x in line.split(" ")]
    
    column_name = ['filename', 'width', 'height',
                'class', 'xmin', 'ymin', 'xmax', 'ymax']
    
    return text_df    

if __name__ == '__main__':
	parser = argparse.ArgumentParser(description="Text-to-csv Coverter")
	
	parser.add_argument("-a","--AnnotDir",help="Path to the folder where the annotation files are stored",type=str)
	parser.add_argument("-o","--outputFile",help="Path to the folder where the .csv will be stored. The path should end with name of .csv file",type=str)
	parser.add_argument("-i","--imageDir",help="Path to the folder where the corresponding images are stored",type=str)
	args = parser.parse_args()
	text_df = text_to_csv(args.inputDir, args.imageDir)
	
	print('Successfully converted text to csv')
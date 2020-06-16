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
			image_name = files.replace(".txt","_test.jpg")
			filename = os.path.join(image_path,image_name)
			category = 1
			width = 640
			height = 640
			xmin = string[0]
			ymin = string[1]
			xmax = string[2]
			ymax = string[3]
			
			text_list.append([filename, width, height, category, xmin, ymin, xmax, ymax])
			
	column_name = ['filename', 'width', 'height', 'class', 'xmin', 'ymin', 'xmax', 'ymax']
	text_df = pd.DataFrame(text_list, columns = column_name)
	
	return text_df
if __name__ == '__main__':
	parser = argparse.ArgumentParser(description="Text-to-csv Coverter")
	
	parser.add_argument("-a","--AnnotDir",help="Path to the folder where the annotation files are stored",type=str)
	parser.add_argument("-o","--outputFile",help="Path to the folder where the .csv will be stored. The path should end with name of .csv file",type=str)
	parser.add_argument("-i","--imageDir",help="Path to the folder where the corresponding images are stored",type=str)
	args = parser.parse_args()
	
	text_df = text_to_csv(args.AnnotDir, args.imageDir)
	text_df.to_csv(args.outputFile, index = None)
	
	print('Successfully converted text to csv')
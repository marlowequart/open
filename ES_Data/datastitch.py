'''
Use this script to stitch together data.



'''

import pandas as pd
import re
import numpy as np
import csv
import glob


#open csv file, return the data in a pandas dataframe
def import_data(file_name):
	#open the file using pandas, use the first row as the header
	data = pd.read_csv(file_name,header=0)
	
	return data
	
def count_rows(file_name):
	with open(file_name) as f:
		return sum(1 for line in f)
		
def add_header(file_name):
	header = 'Date,Time,Adj Vol,Volume,Open,High,Low,Close\n'
	#Note need to check this is the right order for the header
	
	with open(file_name,'r') as original:
		data=original.read()
	
	with open(file_name,'w') as outfile:
		outfile.write(header + data)
		
def last_date(file_name):
	with open(file_name,'r') as f:
		mycsv = csv.reader(f)
		list_csv = list(mycsv)
		# list_csv[row number][column number]
		date = list_csv[0][0]
		time = list_csv[0][1]
	return date,time
	

		
def main():
	#####
	# Change the file name here
	#####
	# file_name='ESH08_12_01_to_03_30_Copy.csv'
	
	# df=import_data(file_name)
	
	# print(df.head())
	
	# Cycle through all of the files and find the last date listed in the file, make list
	# with file name and last date dates=[[file_name,last_date,last_time]]
	files=[]
	file_end='*.csv'
	for fname in glob.glob(file_end):
		files.append(fname)
	
	file_date_time=[]
	for file in files:
		date,time=last_date(file)
		file_date_time.append([file,date,time])
		
	# sort the files by date
	file_date_time2=sorted(file_date_time,key=lambda file: file[1])
	
	# create a list of the date/time periods to slice from each file
	# format: [[file_name,start_date,start_time,end_date,end_time]]
	slice_list=[['ESH08_12_01_to_03_30.csv','2007-12-20','09:30:00','2008-03-20','09:30:00']]
	for i in range(1,len(file_date_time2)):
		file_name=file_date_time2[i][0]
		start_date,start_time=file_date_time2[i-1][1],file_date_time2[i-1][2]
		end_date,end_time=file_date_time2[i][1],file_date_time2[i][2]
		slice_list.append([file_name,start_date,start_time,end_date,end_time])
		
	#Note, will need to remove duplicate times from the final file, we will end up with 9:30 twice using this list
	# print('\n')
	# for file in slice_list:
		# print(file)
		
		
	#add a header to all of the files
	# for file in files:
	# 	add_header(file)
	
	

	
	# print('rows in csv file: ', count_rows(file_name))
	# df2=import_data(file_name)
	# print(df2.head())
	
main()
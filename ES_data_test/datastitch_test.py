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
		date = list_csv[1][0]
		time = list_csv[1][1]
	return date,time
	
def remove_rows(file):
	data=''
	with open(file,'r') as f:
		for i, line in enumerate(f):
			if i % 2 == 0:
				data=data+line
	
	with open(file,'w') as outfile:
		outfile.write(data)
		
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
	
	
	#remove a bunch of rows from each file
	# for file in files:
		# print('first num: ',count_rows(file))
		# remove_rows(file)
		# remove_rows(file)
		# remove_rows(file)
		# remove_rows(file)
		# print('new_num: ',count_rows(file))

	
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
		
	# Next we want to iterate backwards through the list of files and pull the section in each range given
	# and attach that to the end of a new dataframe we are creating.
	
	# full_data = pd.DataFrame([])
	
	# for i in arange(len(slice_list)):
		# df=pd.read_csv(slice_list[i][0],header=0)
		# top_idx=df.loc[['Date','Time'],[slice_list[i][3],slice_list[i][4]]]
		# low_idx=df.loc[['Date','Time'],[slice_list[i][1],slice_list[i][2]]]
		# full_data = full_data.append(df[])
		
	print(slice_list[0])
	df=pd.read_csv(slice_list[0][0],header=0)
	top_idx=df.loc[['Date','Time'],[slice_list[i][3],slice_list[i][4]]]
	low_idx=df.loc[['Date','Time'],[slice_list[i][1],slice_list[i][2]]]
	print(df[top_idx])
	print(df[low_idx])
	
	#add a header to all of the files
	# for file in files:
		# add_header(file)
	
	

	
	# print('rows in csv file: ', count_rows(file_name))
	# df2=import_data(file_name)
	# print(df2.head())
	
main()
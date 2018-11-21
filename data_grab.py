'''
Use this script to generate desired price data from the csv file.


'''

import pandas as pd
import os
import numpy as np
# import csv


#open csv file, return the data in a pandas dataframe
def import_data(file_name):
	#open the file using pandas, use the first row as the header
	data = pd.read_csv(file_name,header=0)
	
	return data
	
def get_time(file_name,date,time):
	#go into the file, for the given date, pull out the first time
	#that is later than the given time
	
	df=pd.read_csv(file_name,header=0)
	time_idx_df=df.loc[df['Date']==date]
	# print(time_idx_df[['Date','Time']])
	time_idx=time_idx_df.index[time_idx_df['Time'] > time].tolist()
	# print(time_idx)
	out_time_idx=time_idx[-1]
	out_time=df.loc[[out_time_idx],['Time']].values.tolist()
	# print(out_time[0][0])
	return out_time[0][0]
	
	
def save_to_csv(dataframe,filename):
	#save the dataframe to a csv file
	dataframe.to_csv(filename, sep=',', index=False)
	
def daily_stats(dataframe):
	#output the open, high, low, close for each day.
	day=[]
	

	
def main():
	#####
	# input the file name and info here
	#####
	
	script_dir = os.path.dirname(__file__)
	rel_path='ES_Data/'
	# file_name='ES_full_dec_2007_to_nov_2018.csv'
	file_name='ESZ18_06_13_to_11_13.csv'
	file_full= os.path.join(script_dir,rel_path,file_name)
	
	df_1=import_data(file_full)
	print('num rows in df = '+str(df_1.shape[0]))
	
	# Generate a list of days in the file
	days=df_1['Date'].unique().tolist()
	check_nan=np.where(pd.isnull(df_1))
	df=df_1.drop(df_1.index[[check_nan[0][0]]])
	print('num rows in df = '+str(df.shape[0]))
	# print(check_nan[0][0])
	# print(df.loc[check_nan[0][0]])
	
	# print(type(days))
	# print(days)
	
	
	

	
main()
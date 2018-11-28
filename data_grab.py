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
	
	
	
def daily_stats(df,open_time,close_time):
	#output the open, high, low, close for each day.
	
	# ~ a_list=df.loc[[16769]].values.tolist()
	# ~ print(a_list[0])
	
	
	#get the days open
	open_row_idx_list = df.index[df['Time'] == open_time].tolist()
	open_row_idx = max(open_row_idx_list)
	open_row = df.loc[[open_row_idx]].values.tolist()
	day_open = open_row[0][4]
	#get the days close
	close_row_idx_list = df.index[df['Time'] == close_time].tolist()
	close_row_idx = min(close_row_idx_list)
	close_row = df.loc[[close_row_idx]].values.tolist()
	day_close = close_row[0][7]
	# ~ print(open_row_idx,close_row_idx,day_open,day_close)
	# ~ return
	#trim the current_day_df to include only values between open time and close time
	# ~ print(open_row_idx,close_row_idx)
	# ~ print('Total rows in df: '+str(current_day_df.shape[0]))
	df = df.loc[close_row_idx:open_row_idx]
	# ~ print('Total rows in df: '+str(current_day_df.shape[0]))
	# ~ print(current_day_df)
	
	#get the days high
	high_row_list = df.loc[df['High'].idxmax()].tolist()
	day_high = high_row_list[5]
	high_time = high_row_list[1]
	#get the days low
	low_row_list = df.loc[df['Low'].idxmin()].tolist()
	day_low = low_row_list[6]
	low_time = low_row_list[1]
	
	
	return day_open,day_high,day_low,day_close,high_time,low_time
	

	
def main():
	#####
	# input the file name and info here
	#####
	
	# Data location for mac:
	path = '/Users/Marlowe/Marlowe/Securities_Trading/Trading_Ideas/Data/ES_Data/'
	# ~ file_name='ES_full_dec_2007_to_nov_2018.csv'
	file_name='ESZ18_06_13_to_11_13.csv'
	file_full= os.path.join(path,file_name)
	
	# ~ df=import_data(file_full)
	# ~ print(df.head())
	# ~ return
	
	# Data location for windows:
	# ~ script_dir = os.path.dirname(__file__)
	# ~ rel_path='ES_Data/'
	# file_name='ES_full_dec_2007_to_nov_2018.csv'
	# ~ file_name='ESZ18_06_13_to_11_13.csv'
	# ~ file_full= os.path.join(script_dir,rel_path,file_name)
	
	
	df_1=import_data(file_full)
	# ~ print('num rows in df = '+str(df_1.shape[0]))
	
	
	# remove NAN rows
	check_nan=np.where(pd.isnull(df_1))
	df=df_1.drop(df_1.index[[check_nan[0][0]]])
	
	
	# Generate a list of days in the file
	# days=df_1['Date'].unique().tolist()
	# check_nan=np.where(pd.isnull(df_1))
	# df=df_1.drop(df_1.index[[check_nan[0][0]]])
	# print('num rows in df = '+str(df.shape[0]))
	# print(check_nan[0][0])
	# print(df.loc[check_nan[0][0]])
	
	# print(type(days))
	# print(days)
	
	
	
	#####
	# return data for a single date here
	#####
	'''
	# Full day starts at 18:01:00 of previous day and ends at 17:00:00 of current day
	open_time='18:01:00'
	close_time='17:00:00'
	today = '2018-10-24'
	yesterday = '2018-10-23'
	
	
	# cash session starts at 09:30:00 ends at 16:00:00
	# ~ open_time='09:30:00'
	# ~ close_time='16:00:00'
	# ~ today = '2018-10-24'
	
	if open_time == '18:01:00':
		current_day_df = df.loc[df['Date'] == today]
		yesterday_df = df.loc[df['Date'] == yesterday]
		current_day_df = pd.concat([current_day_df,yesterday_df])
	elif open_time == '09:30:00':
		current_day_df = df.loc[df['Date'] == today]
		
	
	# search through the day, get the open, high, low, close
	# ~ daily_stats(current_day_df,open_time,close_time)
	# ~ return
	day_open,day_high,day_low,day_close,high_time,low_time = daily_stats(current_day_df,open_time,close_time)
	
	print('\n')
	print('Todays date: '+today+', Open Time: '+open_time+', Close Time: '+close_time)
	print('Todays open: '+str(day_open)+', Todays Close: '+str(day_close))
	print('Todays High: '+str(day_high)+', Time of high: '+high_time)
	print('Todays Low: '+str(day_low)+', Time of Low: '+low_time)
	print('\n')
	'''
	
	#####
	# return data for multiple days here
	#####
	
	# Full day starts at 18:01:00 of previous day and ends at 17:00:00 of current day
	# ~ open_time='18:01:00'
	# ~ close_time='17:00:00'
	
	# cash session starts at 09:30:00 ends at 16:00:00
	open_time='09:30:00'
	close_time='16:00:00'
	
	# search through each day, get the open, close, high, low
	
	# cycle through days
	
	# Generate a list of days in the file
	days=df['Date'].unique().tolist()
	# ~ print(days)
	# ~ return
	# create a list of dates in this format:
	# [['date',open,high,low,close,high_time,low_time]]
	stat_list=[]
	
	# 11-24-18
	#####
	# the problem I am running into is the days where the overall session is not full date, like sunday and friday
	#####
	
	for i in range(1,len(days)):
		today = days[i]
		print(today)
		# ~ yesterday = days[i-1]
		# ~ if open_time == '18:01:00':
			# ~ current_day_df = df.loc[df['Date'] == today]
			# ~ yesterday_df = df.loc[df['Date'] == yesterday]
			# ~ current_day_df = pd.concat([current_day_df,yesterday_df])
		# ~ elif open_time == '09:30:00':
			# ~ current_day_df = df.loc[df['Date'] == today]
		
		current_day_df = df.loc[df['Date'] == today]
		print(len(current_day_df))
		print(current_day_df.head())
		print(current_day_df.tail())
		if i > 3:
			return
		# ~ day_open,day_high,day_low,day_close,high_time,low_time = daily_stats(current_day_df,open_time,close_time)
		# ~ stat_list.append([today,day_open,day_high,day_low,day_close,high_time,low_time])
	
	for item in stat_list:
		print(item)
	
	# ~ print('num rows in df = '+str(df.shape[0]))
	
	# ~ print(type(days[0]))
	# ~ print(len(days))
	# ~ for day in days:
		# ~ print(day)
	

	
main()

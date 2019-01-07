'''
This script determines statistics for various types of moves.

At the beginning of each statistic, choose a minimum and maximum ATR to consider.
This is important because the statistics will be different depending on the market type
and the market type has to be taken into consideration.



# Include the following columns in the dataframe
# 1:Date, 2:Todays Open, 3:Open High, 4: Time of High, 5: Open Low, 6: Time of Low,
# 7:Value at 10am, 8:Total Volume, 9:Open Type, 10:Open Type Secondary, 11:Day Type
# 12:Day Type Secondary, 13:Open in Yesterdays Range, 14:Open in Yesterdays Value
# 15:Gap Up/Down, 16:Number of times crossing open, 18:Previous Open, 19:Previous Close,
# 20:Previous High, 21:Previous Low, 22:days ATR, 23:10 day ATR, 25:Number of Trades,
# 26:Profit/Loss Points, 27:Profit/Loss Dollars


#Open the excel file data
doc = pd.read_excel(io=xlsx_file, sheet_name=sheet, index_col=0, header=4, usecols=cols)

python statistic tools:
statistics.mean(sample_list)
statistics.stdev(sample_list)

'''

import pandas as pd
import statistics as stat
from openpyxl import load_workbook
import datetime


# define excel file names
path = '/Users/Marlowe/Marlowe/Securities_Trading/_Ideas/TradeOpen/'
file_name = 'TradingTheOpen.xlsx'
sheet = 'SPHistoricalData'

xlsx_file = path + file_name


def time_avg(datetimeList):
	#input list is datetime.datetime
	
	# ~ print(datetimeList)
	# ~ return
	
	total = sum(dt.hour*3600 + dt.minute*60 + dt.second for dt in datetimeList)
	avg = total / len(datetimeList)
	minutes, seconds = divmod(int(avg), 60)
	hours, minutes = divmod(minutes, 60)
	mean = datetime.datetime(1900, 1, 1,hours, minutes, seconds)
	
	#to get the std dev, create a list of dt objects of the
	#difference between each object and the mean and square the result
	#(results listed in seconds)
	diff_list=[]
	for dt in datetimeList:
		conv_seconds = dt.hour*3600 + dt.minute*60 + dt.second
		diff = conv_seconds-avg
		diff_sq = diff*diff
		diff_list.append(diff_sq)
	#next get the mean of those squared differences
	#(still in seconds)
	mean_differences = sum(obj for obj in diff_list)/len(datetimeList)
	
	#take the square root of that average
	#(in seconds)
	std_dev_sec = round(mean_differences**(1/2),0)
	
	#lastly convert std dev to datetime obj
	minutes1, seconds1 = divmod(int(std_dev_sec), 60)
	hours1, minutes1 = divmod(minutes1, 60)
	std_dev = datetime.datetime(1900, 1, 1,hours1, minutes1, seconds1)
	
	return mean,std_dev
	

def time_std_dev(datetimeList):
	#input list is datetime.datetime
	return


def open_test_drive():
	
	# On open-test-drive days, how soon is the test completed, mean and std dev
	cols=[1,2,3,4,5,6,9]
	doc = pd.read_excel(io=xlsx_file, sheet_name=sheet, index_col=0, header=4, usecols=cols)
	# ~ print(doc.head())
	# ~ columns = list(doc.columns.values)
	# ~ for item in columns:
		# ~ print(item)
	# ~ return
	
	#First find the minimum time of the high or low.
	time_of_test=[]
	#Also find the value of the test compared to the open
	#value_of_test=[[value of open,value of test]]
	value_of_test=[]
	for index, row in doc.iterrows():
		if row['Open Type'] == 'Open-Test-Drive':
			print(row['Time of High'],row['Time of Low'])
			# ~ print (min(row['Time of High'],row['Time of Low']))
			# ~ time_of_test.append(min(row['Time of High'],row['Time of Low']))
			
			#left off here, need to find the value at the test if it is a high or low
			# ~ value_of_test.append([row['Todays Open'],row['']])
	
	print(sum(time_of_test))
	
	
def open_reject_reverse_followthrough():
	
	# On open-reject-reverse days, how often does the day end in the rejection of the reverse?
	# how often does the next few days follow through?
	
	# How far from the open does the reversal go?
	# How long does it take for the reversal to reach the peak?
	# How long does it take for the reversal to go back through the open?
	
	# 12/26/18
	#How often does the daily action surpass the rejection point? How often does it breach that rejection point?
	
	###
	#set ATR for these calculations
	#This is important because the statistics will be different depending on the market type
	#and the market type has to be taken into consideration.
	###
	min_atr=40.
	max_atr=100.
	
	#create df with desired columns
	cols=[1,2,4,6,7,9,18,19,20,21,22,23]
	doc_init = pd.read_excel(io=xlsx_file, sheet_name=sheet, index_col=0, header=4, usecols=cols)
	
	#only use rows within desired ATR
	doc = pd.DataFrame()
	for index, row in doc_init.iterrows():
		ten_atr=round(row['10 day ATR'],2)
		if ten_atr >= min_atr and ten_atr <= max_atr:
			doc = doc.append(row)
			
	
	
	# ~ print(doc.head())
	# ~ columns = list(doc.columns.values)
	# ~ for item in columns:
		# ~ print(item)
	# ~ return
	
	# ~ print(doc['2018-12-12'])
	
	# get the index of the open-reject-reverse days
	idxs=[]
	for index, row in doc.iterrows():
		if row['Open Type'] == 'Open-Reject-Reverse':
			idx=str(index)
			head, sep, tail = idx.partition(' ')
			idxs.append(head)
	
	
	# create a dictionary with the key[date]:[days_open,days_close,reversal_direction,reversal_peak_time,days_direction,1day_atr,10day_atr]
	# the reversal direction is if the index headed positive or negative after the reversal
	# this covers all days that are open-reject-reverse
	test_dict={k:[] for k in idxs}
	for item in idxs:
		###
		#get todays open, the open listed for the date of the given index
		###
		open_hold=doc[item]['Todays Open'].tolist()
		today_open=open_hold[0]
		
		###
		#get todays close, the previous close listed in the date after todays index
		###
		index_num=doc.index.get_loc(item)
		close_hold=doc.iloc[index_num-1]['Previous Close'].tolist()
		today_close=close_hold[0]
		
		#Days open: item 0
		test_dict[item].append(today_open)
		#Days close: item 1
		test_dict[item].append(today_close)
		
		###
		#determine the reversal direction
		###
		
		#the following determines the reversal direction if the value at 10am
		#relative to the open is higher or lower
		#2018-12-15: not a great way to determine. Want to test if the opens high is before
		#the opens low or vice versa to determine reversal direction.
		# ~ opens_close_hold=doc[item]['Val at 10'].tolist()
		# ~ today_opens_close=opens_close_hold[0]
		# ~ diff=today_open-today_opens_close
		# ~ if diff > 0:
			# ~ direction='negative'
		# ~ else:
			# ~ direction='positive'
		# ~ test_dict[item].append(direction)
		# ~ #print('date: ',item)
		# ~ #print(direction)
		
		
		#the following determines the reversal direction by finding if the high or low
		#is earlier. If the high is earlier than the low, the reversal went to the negative
		#direction. If the low is earlier than the reversal went positive
		high_time_hold=doc[item]['Time of High'].tolist()
		high_time=high_time_hold[0]
		ht_hold=datetime.datetime.strptime(str(high_time),"%H:%M:%S")
		
		#convert datetime.time to timedelta object
		# ~ high_time_delta=high_time - datetime.datetime(0,0,0)
		
		low_time_hold=doc[item]['Time of Low'].tolist()
		low_time=low_time_hold[0]
		lt_hold=datetime.datetime.strptime(str(low_time),"%H:%M:%S")
		
		if low_time < high_time:
			reversal_direction = 'positive'
		else:
			reversal_direction = 'negative'
		
		#Reversal Direction: item 2
		test_dict[item].append(reversal_direction)
		
		#time of peak for reversal: item 3
		test_dict[item].append(min(ht_hold,lt_hold))
		
		# ~ print('date: ',item)
		# ~ print('low time: '+str(low_time)+' high time: '+str(high_time)+' direction: '+direction)
		if today_close < today_open:
			days_direction = 'negative'
		else:
			days_direction = 'positive'
		
		#adding days direction to dictionary: item 4
		test_dict[item].append(days_direction)
		#adding days 1 day atr to dictionary: item 5
		day_atr=doc[item]['TR'].tolist()
		test_dict[item].append(day_atr[0])
		#adding days 10 day atr to dictionary: item 6
		atr_hold=doc[item]['10 day ATR'].tolist()
		test_dict[item].append(atr_hold[0])
		
		
		
	###
	#generate stats
	#dict_structure: key[date]:[days_open,days_close,reversal_direction,reversal_peak_time,days_direction,1day_atr,10day_atr]
	###
	#total number of open-reject-reverse days
	samp_size=len(test_dict)
	print('\n')
	print('Total sample size of open-reject-reverse days = '+str(samp_size))
	
	
	direction_match=0
	days_move_all=[]
	days_move_direction_match=[]
	ten_day_atr_overall=[]
	reversal_time=[]
	for key in test_dict:
		# create list of the 10day atrs for all open-reject-reverse days
		ten_day_atr_overall.append(test_dict[key][6])
		days_move=abs(test_dict[key][0]-test_dict[key][1])
		days_move_all.append(days_move)
		reversal_time.append(test_dict[key][3])
		#days that closed in direction of reversal
		if test_dict[key][2]==test_dict[key][4]:
			#number of days that closed in direction of reversal
			direction_match=direction_match+1
			days_move_direction_match.append(days_move)
			
	
	direction_match_pct=round(100*direction_match/samp_size,1)
	# ~ print(reversal_time)
	mean_reversal_time,std_dev_reversal_time=time_avg(reversal_time)
	
	print('Total sample size mean 10 day ATR: '+str(round(stat.mean(ten_day_atr_overall),2)))
	print('Total sample size 10 day ATR std dev: '+str(round(stat.stdev(ten_day_atr_overall),2)))
	print('Total sample size mean reversal time: '+mean_reversal_time.strftime("%H:%M"))
	print('Total sample size reversal time std dev: '+std_dev_reversal_time.strftime("%H:%M"))
	return
	print('\n')
	print('On open-reject-reverse days, the day closes in the same direction as the reversal '+str(direction_match_pct)+'% of the time')
	print('Total sample size of open-reject-reverse days where the day closes in the same direction as the reversal '+str(direction_match))
	print('The days move mean is '+str(round(stat.mean(days_move_direction_match),2)))
	print('The days move std dev is '+str(round(stat.stdev(days_move_direction_match),2)))
	print('The max days move is '+str(max(days_move_direction_match)))
	print('The min days move is '+str(min(days_move_direction_match)))
	print('\n')
	



def main():
	
	
	
	#####
	# Generate statistics
	#####
	
	# ~ open_test_drive()
	open_reject_reverse_followthrough()
	
	

main()

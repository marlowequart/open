'''
This script is designed to update my spreadsheet of moat companies.

Note: some earnings data has been shown to be wrong. it may be necessary to double
check the data.



# Include the following columns in the dataframe
# 1:Date, 2:Todays Open, 3:Open High, 4: Time of High, 5: Open Low, 6: Time of Low,
# 7:Value at 10am, 8:Total Volume, 9:Open Type, 10:Open Type Secondary, 11:Day Type
# 12:Day Type Secondary, 13:Open in Yesterdays Range, 14:Open in Yesterdays Value
# 15:Gap Up/Down, 16:Number of times crossing open, 18:Previous Open, 19:Previous Close,
# 20:Previous High, 21:Previous Low, 23:Number of Trades, 24:Profit/Loss Points, 25:Profit/Loss Dollars


#Open the excel file data
doc = pd.read_excel(io=xlsx_file, sheet_name=sheet, index_col=0, header=4, usecols=cols)

'''

import pandas as pd

from openpyxl import load_workbook


# define excel file names
path = '/Users/Marlowe/Marlowe/Securities_Trading/Trading_Ideas/TradeOpen/'
file_name = 'TradingTheOpen.xlsx'
sheet = 'SPHistoricalData'

xlsx_file = path + file_name


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
	
	#create df with desired columns
	cols=[1,2,7,9,18,19,20,21]
	doc = pd.read_excel(io=xlsx_file, sheet_name=sheet, index_col=0, header=4, usecols=cols)
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
	
	
	# create a dictionary with the key[date]:[days open,days close,reversal direction]
	# the reversal direction is if the index headed positive or negative after the reversal
	test_dict={k:[] for k in idxs}
	for item in idxs:
		#get todays open, the open listed for the date of the given index
		open_hold=doc[item]['Todays Open'].tolist()
		today_open=open_hold[0]
		
		#get todays close, the previous close listed in the date after todays index
		index_num=doc.index.get_loc(item)
		close_hold=doc.iloc[index_num-1]['Previous Close'].tolist()
		today_close=close_hold[0]
		
		test_dict[item].append(today_open)
		test_dict[item].append(today_close)
		
		#determine the reversal direction
		#the following determines the reversal direction if the value at 10am
		#relative to the open
		#2018-12-15: not a great way to determine. Want to test if the opens high is before
		#the opens low or vice versa to determine reversal direction.
		opens_close_hold=doc[item]['Val at 10'].tolist()
		today_opens_close=opens_close_hold[0]
		diff=today_open-today_opens_close
		if diff > 0:
			direction='negative'
		else:
			direction='positive'
		test_dict[item].append(direction)
			
		# ~ print('date: ',item)
		# ~ print(direction)
	
	print(test_dict)


def main():
	
	
	
	#####
	# Generate statistics
	#####
	
	# ~ open_test_drive()
	open_reject_reverse_followthrough()
	
	

main()

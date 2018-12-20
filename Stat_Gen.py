'''
This script is designed to update my spreadsheet of moat companies.

Note: some earnings data has been shown to be wrong. it may be necessary to double
check the data.



# Include the following columns in the dataframe
# 1:Date, 2:Todays Open, 3:Open High, 4: Time of High, 5: Open Low, 6: Time of Low,
# 7:Total Volume, 8:Open Type, 9:Day Type, 10:Open in Yesterdays Range, 11:Open in Yesterdays Value
# 12:Gap Up/Down, 13:Number of times crossing open, 15:Previous Open, 16:Previous Close,
# 17:Previous High, 18:Previous Low, 20:Number of Trades, 21:Profit/Loss Points, 22:Profit/Loss Dollars
cols=[1,4,6,8]
#Open the excel file data
doc = pd.read_excel(io=xlsx_file, sheet_name=sheet, index_col=0, header=4, usecols=cols)

'''

import pandas as pd

from openpyxl import load_workbook


# define excel file names
#mac path
#path = '/Users/Marlowe/Marlowe/Securities_Trading/Trading_Ideas/TradeOpen/'
#pc path
path = 'C:\\Python\\open\\'

file_name = 'TradingTheOpen.xlsx'
sheet = 'SPHistoricalData'




xlsx_file = path + file_name


def open_test_drive():
	
	# On open-test-drive days, how soon is the test completed, mean and std dev
	cols=[1,2,3,4,5,6,8]
	doc = pd.read_excel(io=xlsx_file, sheet_name=sheet, index_col=0, header=4, usecols=cols)
	print(doc.head())
	return
	#First find the minimum time of the high or low.
	time_of_test=[]
	#Also find the value of the test compared to the open
	#value_of_test=[[value of open,value of test]]
	value_of_test=[]
	for index, row in doc.iterrows():
		if row['Open Type'] == 'Open-Test-Drive':
			# ~ print (min(row['Time of High'],row['Time of Low']))
			time_of_test.append(min(row['Time of High'],row['Time of Low']))
			
			#left off here, need to find the value at the test if it is a high or low
			value_of_test.append([row['Todays Open'],row['']])
	
	print(sum(time_of_test))

def main():
	
	
	
	#####
	# Generate statistics
	#####
	
	open_test_drive()
	
	

main()

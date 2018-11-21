'''
Use this script to create candle plots of data.



'''

import pandas as pd
import numpy as np
import os

import matplotlib.pyplot as plt
from matplotlib.finance import candlestick2_ochl
from matplotlib.finance import volume_overlay2
import matplotlib.ticker as ticker
from matplotlib import gridspec



#open csv file, return the data in a pandas dataframe
def import_data(file_name):
	#open the file using pandas, use the first row as the header
	data = pd.read_csv(file_name,header=0)
	
	#remove Adj Close column
	# data=data.drop('Adj Close', axis=1)
	
	return data

def gen_plot_1(dataframe,startidx,endidx):
	#####
	# plot just price
	#####
	endidx=endidx+1
	#dataframe is a pandas dataframe with open, high, low, close and volume for each time interval
	
	open=dataframe['Open'][startidx:endidx].tolist()
	high=dataframe['High'][startidx:endidx].tolist()
	low=dataframe['Low'][startidx:endidx].tolist()
	close=dataframe['Close'][startidx:endidx].tolist()
	volume=dataframe['Adj Vol'][startidx:endidx].tolist()
	time=dataframe['Time'][startidx:endidx].tolist()
	# date=dataframe['Date'][startidx:endidx].tolist()
	open.reverse()
	high.reverse()
	low.reverse()
	close.reverse()
	volume.reverse()
	time.reverse()
	# date.reverse()
	num_ticks=6


	def mydate(x,pos):
		try:
			return time[int(x)]
		except IndexError:
			return ''
	
	#####
	# plot just price
	#####
	fig = plt.figure()
	ax = plt.subplot()
	candlestick2_ochl(ax,open,low,high,close,width=0.5,colorup='b',colordown='r',alpha=0.75)
	ax.xaxis.set_major_locator(ticker.MaxNLocator(num_ticks))
	ax.xaxis.set_major_formatter(ticker.FuncFormatter(mydate))
	fig.autofmt_xdate()
	fig.tight_layout()
	ax.set_ylabel('Price')
	ax.set_xlabel('Date/Time')
	ax.set_xlim(-1.0,len(open)-1.0)
	ax.xaxis.set_major_locator(ticker.MaxNLocator(num_ticks))
	ax.xaxis.set_major_formatter(ticker.FuncFormatter(mydate))
	ax.grid()
	plt.show()
	
	
	
def gen_plot_2(dataframe,startidx,endidx):
	#####
	# plot price with volume by price
	#####
	endidx=endidx+1
	#dataframe is a pandas dataframe with open, high, low, close and volume for each time interval
	
	open=dataframe['Open'][startidx:endidx].tolist()
	high=dataframe['High'][startidx:endidx].tolist()
	low=dataframe['Low'][startidx:endidx].tolist()
	close=dataframe['Close'][startidx:endidx].tolist()
	volume=dataframe['Adj Vol'][startidx:endidx].tolist()
	time=dataframe['Time'][startidx:endidx].tolist()
	# date=dataframe['Date'][startidx:endidx].tolist()
	open.reverse()
	high.reverse()
	low.reverse()
	close.reverse()
	volume.reverse()
	time.reverse()
	# date.reverse()
	num_ticks=6

	def mydate(x,pos):
		try:
			return time[int(x)]
		except IndexError:
			return ''
	
	
	#####
	# plot price with volume by price
	#####
	fig = plt.figure()
	
	ax4 = plt.subplot()
	candlestick2_ochl(ax4,open,low,high,close,width=0.5,colorup='b',colordown='r',alpha=0.75)
	ax4.xaxis.set_major_locator(ticker.MaxNLocator(num_ticks))
	ax4.xaxis.set_major_formatter(ticker.FuncFormatter(mydate))
	fig.autofmt_xdate()
	fig.tight_layout()
	ax4.set_ylabel('Price')
	ax4.set_xlabel('Date')
	ax4.set_xlim(-1.0,len(open)-1.0)
	ax4.grid()
	# plt.show()
	
	#plot horizontal bar chart with volume
	#generate volume by price, using value at close
	min_price=min(close)
	max_price=max(close)
	
	
	###############
	###############
	#set the nbins for qty of volume bars
	nbins=75
	barheight=.5
	num_ticks_vol=5
	###############
	###############
	
	
	dy=(max_price-min_price)/nbins
	ys = np.arange(min_price,max_price+dy,dy).round(decimals=2)
	pairs=[]
	bins=[0 for x in range(len(ys))]
	for i in range(len(close)):
		for z in range(len(ys)-1):
			if ys[z] <= close[i] < ys[z+1]:
				bins[z]=bins[z]+volume[i]
				
				
	def setbins(x,pos):
		try:
			return ys[int(x)]
		except IndexError:
			return ''
	
	ax3 = ax4.twinx()
	ax3 = ax4.twiny()
	# ax3.yaxis.set_major_formatter(ticker.FuncFormatter(setbins))
	ax3.barh(ys,bins,align='center',height=barheight,color='gray',alpha=0.5)
	# ax3.set_yticks(ys)
	# ax3.yaxis.set_major_locator(ticker.MaxNLocator(num_ticks_vol))
	ax3.yaxis.set_visible(False)
	ax3.xaxis.set_visible(False)
	# ax3.set_yticklabels(ys)
	# ax3.grid()
	plt.show()
	
	
	
def gen_plot_3(dataframe,startidx,endidx):
	#####
	# plot price with volume in second view below
	#####
	endidx=endidx+1
	#dataframe is a pandas dataframe with open, high, low, close and volume for each time interval
	
	open=dataframe['Open'][startidx:endidx].tolist()
	high=dataframe['High'][startidx:endidx].tolist()
	low=dataframe['Low'][startidx:endidx].tolist()
	close=dataframe['Close'][startidx:endidx].tolist()
	volume=dataframe['Adj Vol'][startidx:endidx].tolist()
	time=dataframe['Time'][startidx:endidx].tolist()
	# date=dataframe['Date'][startidx:endidx].tolist()
	open.reverse()
	high.reverse()
	low.reverse()
	close.reverse()
	volume.reverse()
	time.reverse()
	# date.reverse()
	
	num_ticks=6

	def mydate(x,pos):
		try:
			return time[int(x)]
		except IndexError:
			return ''
	
	#####
	# plot price with volume in second view below
	#####
	fig = plt.figure()
	gs = gridspec.GridSpec(2,1, height_ratios=[3,1])
	ax1 = plt.subplot(gs[0])
	ax2 = plt.subplot(gs[1])
	candlestick2_ochl(ax1,open,low,high,close,width=0.5,colorup='b',colordown='r',alpha=0.75)
	volume_overlay2(ax2,close,volume,width=0.5,colorup='b',colordown='r')
	ax1.xaxis.set_major_locator(ticker.MaxNLocator(num_ticks))
	ax1.xaxis.set_major_formatter(ticker.FuncFormatter(mydate))
	fig.autofmt_xdate()
	fig.tight_layout()
	ax1.set_ylabel('Price')
	ax2.set_ylabel('Volume')
	ax2.set_xlabel('Date')
	ax1.set_xlim(-1.0,len(open)-1.0)
	ax2.set_xlim(-1.0,len(open)-1.0)
	ax2.xaxis.set_major_locator(ticker.MaxNLocator(num_ticks))
	ax2.xaxis.set_major_formatter(ticker.FuncFormatter(mydate))
	ax1.grid()
	ax2.grid()
	plt.show()
	
	
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
	
	
def main():
	#####
	# Change the file name here
	#####
	script_dir = os.path.dirname(__file__)
	rel_path='ES_Data/'
	# file_name='ES_full_dec_2007_to_nov_2018.csv'
	file_name='ESZ18_06_13_to_11_13.csv'
	file_full= os.path.join(script_dir,rel_path,file_name)
	
	df=import_data(file_full)
	
	# print(df.head())
	
	#####
	# modify the dataframe and plot it
	#####
	#set the date
	# Full day starts at 18:01:00 of previous day and ends at 17:00:00 of current day
	# cash session starts at 09:30:00 ends at 16:00:00
	start_date='2018-10-26'
	start_time='09:30:00'
	end_date='2018-10-26'
	end_time='16:00:00'
	start_day_df=df.loc[df['Date'] == start_date]
	end_day_df=df.loc[df['Date'] == end_date]
	# print(start_day_df.head())
	
	start_time_idx_df=start_day_df.index[start_day_df['Time'] == start_time].tolist()
	start_time_idx=start_time_idx_df[0]
	end_time_idx_df=end_day_df.index[end_day_df['Time'] == end_time].tolist()
	end_time_idx=end_time_idx_df[0]

	# print('start_idx date check: idx: '+str(start_time_idx)+', date: '+str(df['Date'][start_time_idx])+', time: '+str(df['Time'][start_time_idx])+', Open: '+str(df['Open'][start_time_idx]))
	# print('end_idx date check: idx: '+str(end_time_idx)+', date: '+str(df['Date'][end_time_idx])+', time: '+str(df['Time'][end_time_idx])+', Open: '+str(df['Open'][end_time_idx]))
	# print('Number of datapoints: '+str(start_time_idx-end_time_idx))
	
	#plot it
	# print(df.head())
	# print(start_time_idx)
	# print(end_time_idx)
	# gen_plot_1(df,end_time_idx,start_time_idx)
	gen_plot_2(df,end_time_idx,start_time_idx)
	# gen_plot_3(df,end_time_idx,start_time_idx)
	
main()

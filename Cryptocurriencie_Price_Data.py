# -*- coding: utf-8 -*-
"""
Created on Mon Nov 13 16:54:54 2017

@author: Alex
"""
#import os

#os.chdir("/Users/AlexD/Desktop/Python Project")
#path_direct = os.getcwd()

'''
packages plotly and quandl might need to be installed first
'''

import quandl
import pandas as pd
#import pickle
import plotly.offline as py
import plotly.graph_objs as go


  

#Define a function to pull the data from one exchange:
def crypto_data(chart_exchange):
    #Download and cache Quandl dataseries
    path = '{}.csv'.format(chart_exchange).replace('/','-')
    df = quandl.get(chart_exchange, returns='pandas')
    df.to_csv(path)
    return df  

df_kraken = crypto_data('BCHARTS/KRAKENUSD')


df_kraken.head() #Shows the first five columns of our dataframe

#First chart of Bitcoin timeseries from Bitstamp:
btc = go.Scatter(x=df_kraken.index, y=df_kraken['Weighted Price'])
py.plot([btc],filename='btc_USD_Kraken.html')


# Pull pricing data for more BTC exchanges and safe them in a dictionary
exchanges = ['COINBASE','BITSTAMP','ITBIT']

exchange_data = {}

exchange_data['KRAKEN'] = df_kraken

for exchange in exchanges:
    exchange_code = 'BCHARTS/{}USD'.format(exchange)
    btc_df = crypto_data(exchange_code)
    exchange_data[exchange] = btc_df
    
#Merch into one single dataframe   
    def combine_dataframes(dataframes, labels, col):
        btc_dict={}
        for index in range(len(dataframes)):
            btc_dict[labels[index]] = dataframes[index][col]
            
        return pd.DataFrame(btc_dict)

btc_usd_datasets = combine_dataframes(list(exchange_data.values()), list(exchange_data.keys()), 'Weighted Price')

#Similar to .head() but looking at the last values in our df
btc_usd_datasets.tail()

#Plotting the results:
#To be continued...
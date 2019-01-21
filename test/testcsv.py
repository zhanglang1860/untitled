#coding:utf-8
import datetime
import pandas as pd
import numpy as np
import pickle

#用pandas将时间转为标准格式
dateparse = lambda dates: pd.datetime.strptime(dates,'%d/%m/%Y %H:%M')
#将时间栏合并,并转为标准时间格式
rawdata = pd.read_csv('RealMarketPriceDataPT.csv',parse_dates={'timeline':['date','(UTC)']},date_parser=dateparse)

#定义一个将时间转为数字的函数,s为字符串
def datestr2num(s):
    #toordinal()将时间格式字符串转为数字
    return datetime.datetime.strptime(s,'%Y-%m-%d %H:%M:%S').toordinal()

x = []
y = []
new_date = []

for i in range(rawdata.shape[0]):
    x_convert = int(datestr2num(str(rawdata.ix[i,0])))
    new_date.append(x_convert)
    y_convert = rawdata.ix[i,1].astype(np.float32)
    x.append(x_convert)
    y.append(y_convert)

x = np.array(x).astype(np.float32)

"""
with open('price.pickle','wb') as f:
    pickle.dump((x,y),f)
"""
print(datetime.datetime.fromordinal(new_date[0]),'------>>>>>>',new_date[0])
print(datetime.datetime.fromordinal(new_date[10]),'------>>>>>>',new_date[10])
print(datetime.datetime.fromordinal(new_date[20]),'------>>>>>>',new_date[20])
print(datetime.datetime.fromordinal(new_date[30]),'------>>>>>>',new_date[30])
print(datetime.datetime.fromordinal(new_date[40]),'------>>>>>>',new_date[40])
print(datetime.datetime.fromordinal(new_date[50]),'------>>>>>>',new_date[50])

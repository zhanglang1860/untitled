#coding:utf-8
import datetime
import pandas as pd
import numpy as np
import re
import pickle
longdate_np = []
hsplit_np=[]
#用pandas将时间转为标准格式
dateparse = lambda dates: pd.datetime.strptime(dates,'%d/%m/%Y %H:%M')
#将时间栏合并,并转为标准时间格式
# rawdata = pd.read_csv('53787 气站数据.csv',parse_dates={'timeline':['date','(UTC)']},date_parser=dateparse)
rawdata = pd.read_csv(r'C:\Users\Administrator\PycharmProjects\untitled\files\53787.csv',
                      header=None,names=['区站号','纬度','经度','观测场海拔高度',
                                         '年','月','日','平均风速','最大风速',
                                         '最大风速的风向','极大风速','极大风速的风向',
                                         'other1','other2','other3','other4','other5'])

split_rawdata=np.hsplit(rawdata, (4,12))
Data=split_rawdata[1]
print(Data.shape)
aa=np.array(Data)
print(aa[1])
# Date_array=hsplit_np[1]
# wind_avg_array=hsplit_np[2]/10
# wind_max_array=hsplit_np[3]/10
# wind_maxdeg_array=hsplit_np[4]
# wind_extrame_array=hsplit_np[5]/10
# wind_extramedeg_array=hsplit_np[6]

# for i in range(Data.shape[0]):
#     print(Data[i][0])
    # dates = pd.to_datetime(sstr, format='%Y %m %d', errors='ignore') #将数据类型转换为日期类型
    # print(sstr)
# # df = Dates.set_index('date') # 将date设置为index
# # print(df.head(2))
# # print(df.tail(2))
# # print(df.shape)
# new_Dates=np.array(Dates)
# print(new_Dates.shape)
# for i in range(rawdata.shape[0]):
#     dates = re.sub('[\[\]]', '', np.array_str(Date_array[i]))
#     date_num = datetime.datetime.strptime(dates, '%Y %m %d').timestamp()
#     Dates.append(dateparse)
# print(Dates)
# modify_rawdata=np.hstack((new_Dates,wind_avg_array,wind_max_array,wind_maxdeg_array,wind_extrame_array,wind_extramedeg_array))



# date_number = datetime.datetime.strptime(str(hsplit_np[1][0]&'-'&hsplit_np[2][0]&'-'&hsplit_np[3][0])
#                                          ,'%Y-%m-%d').timestamp()
#
# print(datetime.datetime.utcfromtimestamp(date_number),'------>>>>>>',date_number)



# #定义一个将时间转为数字的函数,s为字符串
# def datestr2num(s):
#     #toordinal()将时间格式字符串转为数字
#     return datetime.datetime.strptime(s,'%Y-%m-%d %H:%M:%S').toordinal()
#
# x = []
# y = []
# new_date = []
#
# for i in range(rawdata.shape[0]):
#     x_convert = int(datestr2num(str(rawdata.ix[i,0])))
#     new_date.append(x_convert)
#     y_convert = rawdata.ix[i,1].astype(np.float32)
#     x.append(x_convert)
#     y.append(y_convert)
#
# x = np.array(x).astype(np.float32)
#
# """
# with open('price.pickle','wb') as f:
#     pickle.dump((x,y),f)
# """
# print(datetime.datetime.fromordinal(new_date[0]),'------>>>>>>',new_date[0])
# print(datetime.datetime.fromordinal(new_date[10]),'------>>>>>>',new_date[10])
# print(datetime.datetime.fromordinal(new_date[20]),'------>>>>>>',new_date[20])
# print(datetime.datetime.fromordinal(new_date[30]),'------>>>>>>',new_date[30])
# print(datetime.datetime.fromordinal(new_date[40]),'------>>>>>>',new_date[40])
# print(datetime.datetime.fromordinal(new_date[50]),'------>>>>>>',new_date[50])

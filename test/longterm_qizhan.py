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
df = pd.read_csv(r'C:\Users\Administrator\PycharmProjects\untitled\files\53787.csv',
                      header=None)

df.columns = ['区站号','纬度','经度','观测场海拔高度',
                                         'year','月','日','平均风速','最大风速',
                                         '最大风速的风向','极大风速','极大风速的风向',
                                         'other1','other2','other3','other4','other5']

index=df.index
df = df.set_index('year') # 将date设置为index
s = pd.Series(df['平均风速'], index=df.index)
s.head(2)
print('---------获取2013年的数据-----------')
print(df[df["year"]>2000]) # 获取2013年的数据



npdtype = [('year', int), ('month', int),('day', int),('wind_speed', float), ('wind_speed_max', float),
           ('wind_speed_max_deg', float),('wind_speed_extrame', float), ('wind_speed_extrame_deg', float)]

hsplit_np=np.hsplit(df,(4,12))
Data_np=np.dtype(npdtype)
Data_np=np.array(hsplit_np[1])
# print(Data_np.shape,rawdata['平均风速'])
# npdtype = [('year', int), ('month', int),('day', int),('wind_speed', float), ('wind_speed_max', float),
#            ('wind_speed_max_deg', float),('wind_speed_extrame', float), ('wind_speed_extrame_deg', float)]
# Data_array = np.array(Data_np[0], dtype=npdtype)
# print(Data_array.size,Data_array)


# Data_array = Data_array.set_index('year')
#
# print(Data_array.head(2))
# print(Data_array.tail(2))


# Merge_dt64=[]
# Data_Date_np=[]
#
# npdtype = [('date', 'datetime64[ns]'), ('wind_speed', float), ('wind_speed_max', float),('wind_speed_max_deg', float),
#                             ('wind_speed_extrame', float), ('wind_speed_extrame_deg', float)]
#
# for i in range(date_np.shape[0]):
# #     # date_str=""
# #     # date_str=str(date_np[i][0])+"/"+str(date_np[i][1])+"/"+str(date_np[i][2])
#     dt = datetime.datetime(date_np[i][0], date_np[i][1], date_np[i][2])
#     dt64 = np.datetime64(dt)
#     # wind_speed=hsplit_np[2]/10
#     # wind_speed_max=hsplit_np[3]/10
#     # wind_speed_max_deg=hsplit_np[4]
#     # wind_speed_extrame = hsplit_np[5]/10
#     # wind_speed_extrame_deg = hsplit_np[6]
#     # date=str(pd.to_datetime(date_str))
# #     # times=datetime.datetime.strptime(date_str, '%Y/%m/%d').timestamp()
#
#     # Merge_dt64.append([dt64],wind_speed,wind_speed_max,wind_speed_max_deg,wind_speed_extrame,wind_speed_extrame_deg)
#     Merge_dt64.append([dt64])
# Data_Date_np=np.array(Merge_dt64)
#
#
# # Data_np=np.hstack((Data_Date_np,hsplit_np[2]))
# # print(Data_np.shape,Data_np)
#
#
# npdtype = [('year', int), ('month', int),('day', int),('wind_speed', float), ('wind_speed_max', float),
#            ('wind_speed_max_deg', float),('wind_speed_extrame', float), ('wind_speed_extrame_deg', float)]
# np_array = np.empty((0,6), dtype=npdtype)
# #
# for i in range(date_np.shape[0]):
#     data=Data_Date_np[i]+" "+hsplit_np[2,i]
#     Data=data.append(data)
# tmp = np.array(Data, dtype=npdtype)
# # np_array=np.append(np_array, tmp)
# # print(np_array.shape,np_array)
# #






# print(hsplit_np[2].shape,hsplit_np[2])

# Modify_data=np.hstack((hsplit_np[2],hsplit_np[3]))
# print(Modify_data.shape,Modify_data)

# test=re.sub('[\[\]]', '', np.array_str(hsplit_np[1][0]))
#
# print(test)

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

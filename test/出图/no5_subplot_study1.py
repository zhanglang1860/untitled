#-*- coding:utf-8 -*-  

# ��������utf-8���ͻ�����ʶ��
# No��2:����Է�������ʾ�����������,��ϤһԪ�ع�������صļ��㼰ͼʾ��ʾ��
# �о������������֮��,ͬһ�������֮��10m,30m,50m,70m��ͬ����10minƽ������֮�������ԡ�
# �о��������챸߶ȴ����70m�߶�10min����������վ10minƽ������֮�������ԡ�
# ��Ϥ���ݿ��ʱ���ʽ���ú���  to_datatime()����
# ��Ϥ���ݿ���趨�����ĺ��� set_index()����
# ��ϤPandas��ȡĳһ��ʱ�����������ε����ݵķ�����data1 = data['2011/3/13 00:00':'2012/3/14 00:00']
# �о��趨 һԪ���Իع�.��ϤһԪ���Իع��X����ת������data[:,np.newaxis]
import matplotlib as mpl
import matplotlib.pyplot as plt
import pandas as pd  #����pandas��
import pylab as pl
import numpy as np 
import datetime
from datetime import datetime

mpl.rcParams["font.sans-serif"]=["SimHei"] # �����������ʶ�ַ����е����ı�ʶ������Ϊ����
mpl.rcParams['axes.unicode_minus'] = False # ��ʹ��Ĭ�ϵ�unicode minusģʽ���������������ߵĿ̶ȱ�ǩΪ�����������

import math
import scipy 
from sklearn import datasets, linear_model
from sklearn.linear_model import LinearRegression 

#���������ݵ������ļ�speedData1.csv.
data = pd.read_csv("speedData1.csv") #pandas ������EXCEL���ָ�����CSV��ʽ�ķ���

data['Date']= pd.to_datetime(data['Date'],format='%Y/%m/%d %H:%M') 
#�趨���ݿ��е�Dateʱ���б������Ϊʱ�����ݸ�ʽ(���� Y m d H M S)��
data = data.set_index('Date') # �趨���ݵ�ʱ����������'Date'
data1 = data['2011/3/13 00:00':'2012/3/14 00:00']
#����ʱ�����е�������ʽ����ȡ��2011/3/13 00:00������2012/3/14 00:00��ʱ�����һ������ݣ����һ���µ����ݿ�data1.
#1
data1_1_direction = data1[(data1['CH7Avg'] > 0) & (data1['CH7Avg'] < 90)]
speed_1_x = data1_1_direction['CH3Avg']
speed_1_y = data1_1_direction['CH13Avg']
X_speed_1_x = speed_1_x[:,newaxis]
#2
data1_2_direction = data1[(data1['CH7Avg'] > 90) & (data1['CH7Avg'] < 180)]
speed_2_x = data1_2_direction['CH3Avg']
speed_2_y = data1_2_direction['CH13Avg']
X_speed_2_x = speed_2_x[:,newaxis]
#3
data1_3_direction = data1[(data1['CH7Avg'] > 180) & (data1['CH7Avg'] < 270)]
speed_3_x = data1_3_direction['CH3Avg']
speed_3_y = data1_3_direction['CH13Avg']
X_speed_3_x = speed_3_x[:,newaxis]

#4
data1_3_direction = data1[(data1['CH7Avg'] > 270) & (data1['CH7Avg'] < 360)]
speed_3_x = data1_3_direction['CH3Avg']
speed_3_y = data1_3_direction['CH13Avg']
X_speed_3_x = speed_3_x[:,newaxis]





print(data1_n_direction.head())

fig1=plt.figure(figsize=(10,10))
fig1,ax = plt.subplots(2,2)#��4������Ϊ������һ����4����ͼ��ͼ��
#subplot(221),2��ʾ2��,2��ʾ2��,1��ʶ�������ĵ�һ��ͼ.
	
ax1 = plt.subplot(221)
#�������������Զ��庯��,����������ȡ�վݼ�,���ӱ任�о���,����X,y




	
#subplot(222),2��ʾ2��,2��ʾ2��,2��ʾ�������ĵ�2��ͼ,����2����ͼ.
ax2 = plt.subplot(222)





	
ax3 = plt.subplot(223)





	
ax4 = plt.subplot(224)






# -*- coding: utf-8 -*-
"""
Created on Wed Apr  1 17:09:16 2020

@author: ТОМА
"""

import pandas as pd
import math 
import numpy as np
df=pd.read_excel('sample1.xlsx',sheet_name='Лист1')
step=math.sqrt((abs(df.ion_sum[0]-df.ion_sum[1])+abs(df.ion_sum[2]-df.ion_sum[1]))/2)
def get_step(col):
    step=math.sqrt((abs(col[0]-col[1])+abs(col[2]-col[1]))/2)
    return step
for col in df.columns[1:]:
    df[col][4]=get_step(df[col])
df_history=pd.DataFrame(columns=['user_id','location_id','indicator_id','value','date'])
df_indicators=pd.read_excel('sample1.xlsx',sheet_name='indicators_info')
def getIndicatorId(indicator_name):
    indicator_id=df_indicators[df_indicators.indicator_name==indicator_name].indicator_id.iloc[0]
    return indicator_id
for i in range(10):
    
    df_list=[]
    for col in df.columns[1:]:
        df_part=pd.DataFrame(columns=['user_id','location_id','indicator_id','value','date'])
        print(col)
        rand_array=df[col][4]*np.random.noncentral_chisquare(10,2,366)
        df_part.date=pd.date_range(start='1/1/2019',end='1/1/2020')
        df_part.indicator_id=getIndicatorId(col)
        df_part['value']=rand_array
        df_list.append(df_part)
    print(i+1)
    df_part=pd.concat(df_list)
    df_part.location_id=i+1
    print(df_part.indicator_id.unique())
    df_history=df_history.append(df_part)
df_history['user_id']=1
df_history['action_id']=1
df_history.to_csv('inserts/one_day_data.csv',header=None,index=False, encoding='cp1251')
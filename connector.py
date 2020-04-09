# -*- coding: utf-8 -*-
"""
Created on Tue Mar 24 12:31:55 2020

@author: ТОМА
"""

import psycopg2
import pandas as pd

archive_table_names=[
'indicators_categories',
'locations_groups',
'locations',
'indicators_info'
        ]
org_table_names=[
'organisation_names',
'organisation_locations',
'organisation_values'
        ]
log_table_names=[
'laboratory_analyzers',
'laboratory_log_actions',
'laboratory_users'
        ]
def read_query(query,bd_name):
    conn = psycopg2.connect(host="localhost",database=bd_name, user="postgres", password="WeWeWe11")
    result=pd.read_sql(query,conn)
    return result
def connection(bd_name):
    conn = psycopg2.connect(host="localhost",database=bd_name, user="postgres", password="WeWeWe11")
    return conn
#def update_table(list_name,bd_name):
#    df=pd.read_excel('sample1.xlsx',sheet_name=list_name)
#    print(df.head())
#    df.to_csv('inserts/{}.csv'.format(list_name),header=None,index=False, encoding='cp1251')
#    conn = psycopg2.connect(host="localhost",database=bd_name, user="postgres", password="WeWeWe11")
#    cur=conn.cursor()
#    #cur.execute("""truncate table public.{}""".format(list_name))
#    filepath=r"'D:\Nygma\river_monitoring\inserts\{}.csv'".format(list_name)
#    print("copy public.{} ({}) from {} csv delimiter ',' encoding 'WIN1251'".format(list_name,", ".join(df.columns),filepath,list_name) )
#    result=cur.execute("copy public.{} ({}) from {} csv delimiter ',' encoding 'WIN1251'".format(list_name,", ".join(df.columns),filepath,list_name) )
#    cur.close()
#    
#for tb in archive_table_names:
#    update_table(tb,'archive')
#for tb in org_table_names:
#    update_table(tb,'organisations')
#for tb in log_table_names:
#    update_table(tb,'laboratory_logs')
#    

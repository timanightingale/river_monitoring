# -*- coding: utf-8 -*-
"""
Created on Thu Apr  9 14:20:49 2020

@author: ТОМА
"""

from connector import connection
import pandas as pd

def AddUser(first_name,second_name,email):
    conn=connection('laboratory_logs')
    cur=conn.cursor()
    cur.execute("select public.adduser(%(first)s,%(second)s,%(mail)s)",
                {'first':first_name,'second':second_name,'mail':email})
    conn.commit()
    cur.close()
    
def DeleteUser(first_name,second_name,email):
    conn=connection('laboratory_logs')
    cur=conn.cursor()
    cur.execute("select public.deleteuser(%(first)s,%(second)s,%(mail)s)",
                {'first':first_name,'second':second_name,'mail':email})
    conn.commit()
    cur.close()
# -*- coding: utf-8 -*-
"""
Created on Thu Apr  9 14:20:49 2020

@author: ТОМА
"""

from connector import connection
import pandas as pd
from datetime import date

def AddUser(first_name,second_name,email,password,login):
    conn=connection('laboratory_logs')
    cur=conn.cursor()
    cur.execute("select public.adduser(%(first)s,%(second)s,%(mail)s,%(pass)s,%(log)s)",
                {'first':first_name,'second':second_name,'mail':email,'pass':password,'log':login})
    conn.commit()
    cur.close()
    
def DeleteUser(first_name,second_name,email):
    conn=connection('laboratory_logs')
    cur=conn.cursor()
    cur.execute("select public.deleteuser(%(first)s,%(second)s,%(mail)s)",
                {'first':first_name,'second':second_name,'mail':email})
    conn.commit()
    cur.close()
    
def Validate(login,password):
    conn=connection('laboratory_logs')
    cur=conn.cursor()
    cur.execute("select public.validate(%(pass)s)",
                {'pass':password})
    res=cur.fetchall()
    res=res[0][0]
    cur.close()
    if res is not None:
        if login==res[:-1]:
            return 1
        else:
            return 2
    else:
        return 0

def GetUserId(login):
    conn=connection('laboratory_logs')
    cur=conn.cursor()
    cur.execute("select max(user_id) from public.laboratory_users where user_login=%(login)s",
                {'login':login+"\n"})
    res=cur.fetchall()
    res=res[0][0]
    cur.close()
    return res

def CheckIndicator(location_id,day,indicator_id):
    conn=connection('archive')
    cur=conn.cursor()
    cur.execute("""select count(*) from public.one_day_data
                where location_id=%(location)s and indicator_id=%(indicator)s and date=%(day)s""",
                {'location':location_id,'indicator':indicator_id,'day':day})
    res=cur.fetchall()
    cur.close()
    return res[0][0]==0

def AddRow(indicator_id,location_id,user_id,value,day):
    conn=connection('archive')
    cur=conn.cursor()
    cur.execute("""insert into public.one_day_data values(%(user)s,%(location)s,%(indicator)s,%(value)s,%(day)s)""",
                {'location':location_id,'indicator':indicator_id,'day':day,'value':value,'user':user_id})
    conn.commit()
    cur.close()
    return 1


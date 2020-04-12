# -*- coding: utf-8 -*-
"""
Created on Thu Apr  9 17:45:08 2020

@author: ТОМА
"""

import re
def validate(text,field):
    if field in ["Електронна пошта"]:
        return validate_email(text)
    elif field in ["Довгота","Широта","Value"]:
        return validate_float(text)
    else:
        return True
def validate_email(text):
    try:
       match=re.findall(r'.+@\w+\.+\w+',text)[0]
       return(text==match)
    except:
       return False
def validate_integer(num):
    try:
        test=int(num)
        return True
    except:
        return 'Будь ласка, введіть цілочисельне значення' 
    
def validate_float(doublep):
    try:
        test=float(doublep)
        return True
    except:
        return 'Будь ласка, введіть значення з плаваючою комою' 
# -*- coding: utf-8 -*-
"""
Created on Thu Apr  9 17:45:08 2020

@author: ТОМА
"""

import re

def validate_email(text):
    try:
       match=re.findall(r'.+@\w+\.+\w+',text)[0]
       return(text==match)
    except:
       return False

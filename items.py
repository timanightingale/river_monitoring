# -*- coding: utf-8 -*-
"""
Created on Wed Apr  8 15:42:28 2020

@author: ТОМА
"""
from connector import read_query
import pandas as pd

locations=read_query("select distinct location_id,location_name from public.locations" ,"archive")
locations={loc:lid for lid,loc in zip(locations.location_id,locations.location_name)}

indicators=read_query("select distinct indicator_id,indicator_name from public.indicators_info" ,"archive")
indicators={nam:iid for iid,nam in zip(indicators.indicator_id,indicators.indicator_name)}



fields=[
        'Користувачі',
         'Місця',
        'Сума іонів',
        'Питома електропровідність',
        'Сульфати', 
        'Хлориди',
        'Розчинений кисень',
        '% насичення',
        '% насичення у гіполімніоні (для водойм)',
        'Завислі речовини', 
        'Прозорість',
        'pH',
        'Нафтопродукти'
        ]
col_names={
    'Сума іонів':'ion_sum', 
    'Питома електропровідність':'condc_spec',
    'Сульфати':'sulfates',
    'Хлориди':'chlorides',
    'Розчинений кисень':'oxygen_diss',
    '% насичення':'oxygen_sat',
    '% насичення у гіполімніоні (для водойм)':'oxygen_sat_hyp',
    'Завислі речовини':'patricles_suspended',
    'Прозорість':'transparency',
    'pH':'ph',
    'Нафтопродукти':'petroleum_products'
        }

rivers=['Дон', 'Дніпро']
subgroups={'Дніпро': 1,
 'Дунай': 2,
 'Закарпаття': 3,
 'Західний Лісостеп': 4,
 'Західний Степ': 5,
 'Карпати': 6,
 'Крим': 7,
 'Південне Полісся': 8,
 'Південний Лісостеп': 9,
 'Південний Степ': 10,
 'Північне Полісся ': 11,
 'Північний Лісостеп': 12,
 'Північний Степ': 13,
 "Приазов'я": 15,
 "Причорномор'я": 15,
 'Східне Полісся': 16,
 'Східний Лісостеп': 18,
 'Східний Степ': 18}
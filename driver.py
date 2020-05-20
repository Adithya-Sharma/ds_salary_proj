# -*- coding: utf-8 -*-
"""
Created on Wed May 20 18:38:28 2020

@author: Dell
"""

import glassdoor_scriper as gs
import pandas as pd
path="C:/Users/Dell/Documents/ds_salary_proj/chromedriver"

df=gs.get_jobs('Data Scientist, Machine Learning,Deep Learning',100,False,path,15)
df.to_csv('glassdoor_jobs.csv',index=False)
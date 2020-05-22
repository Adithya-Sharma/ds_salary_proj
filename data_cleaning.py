# -*- coding: utf-8 -*-
"""
Created on Thu May 21 00:43:36 2020

@author: Dell
"""
import pandas as pd
df=pd.read_csv('glassdoor_jobs.csv')


#Company name text only
df['company text']=df.apply(lambda x: x['Company Name'] if x['Rating'] <0 else x['Company Name'][:-3],axis=1)
#headquarters and location
df['same_place'] = df.apply(lambda x: 1 if x.Location == x.Headquarters.split(',')[0] else 0, axis=1)
#age of the company
df['age']=df.Founded.apply(lambda x: x if x<1 else 2020-x)
#parsing of job desciption
#python
df['python_yn']=df['Job Description'].apply(lambda x: 1 if 'python'in x.lower() else 0)
#R Studio
#df['R_yn']=df['Job Description'].apply(lambda x: 1 if ''in x.lower() else 0)
#spark
df['Spark']=df['Job Description'].apply(lambda x: 1 if 'spark'in x.lower() else 0)
df.Spark.value_counts()
#df['Django']=df['Job Description'].apply(lambda x: 1 if 'django'in x.lower() else 0)
#aws
df['aws']=df['Job Description'].apply(lambda x: 1 if 'aws'in x.lower() else 0)
df.aws.value_counts()
#excel
df['excel']=df['Job Description'].apply(lambda x: 1 if 'excel'in x.lower() else 0)

df.columns
df_out=df


df_out.to_csv('salary_data_cleaned.csv',index=False)

pd.read_csv('salary_data_cleaned.csv')
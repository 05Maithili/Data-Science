# -*- coding: utf-8 -*-
"""
Created on Tue Apr  8 22:07:12 2025

@author: maith
"""

'''Python for Datascience'''
#PANDAS
import pandas as pd
technologies=[["spark",2000,"30days"],["pandas",3000,"40days"]]
df=pd.DataFrame(technologies)
print(df)
#TO ADD NAMES TO ROWS AND COLUMN
column_name=["courses","fees","Duration"]
row_label=["a","b"]
df=pd.DataFrame(technologies,columns=column_name,index=row_label)
print(df)

df.dtypes
types={"courses":str,"fees":float,"Duration":str}
df.dtypes

########################################
'''CREATING DATAFRAME FROM DICTIONARY'''

technologies={"courses":["spark","pyspark","hadoop"],"fees":[2000,8000,5000],"Duration":["30days","90days","45days"],"Discount":[1000,2000,1000]}
df=pd.DataFrame(technologies)
df

#########################################
#convert dataframe to csv
df.to_csv('data_file.csv')

#########################################
#create Dataframe from csv file
df_new=pd.read_csv('data_file.csv')

##########################################
'''PANDAS DATAFRAME-BASIC OPERATIONS'''
import pandas as pd
import numpy as np
technologies=({"Courses":["spark","pyspark","Handoop","python","pandas",None,"spark","python"],
               "Fees":[1000,2000,1200,3000,4000,3200,np.nan,10000],
               "Duration":["30days","40days","50days","60days","90days"," ","50days","45days"],
               "Discount":[300,200,1000,450,1000,300,200,500]})
row_label=["r0","r1","r2","r3","r4","r5","r6","r7"]
df=pd.DataFrame(technologies,index=row_label)
df
df.shape
df.size
df.columns
df.columns.values
df.index
df.dtype

###########################################
#Accessing one column containts
df['Fees']
#Accessing two column containts
df[["Fees","Duration"]]

#select certain rows and assign it to another dataframe
df2=df[6:]
df2
df3=df[:5 ]
df3
#Accesing specific cell from a column duration
df['Duration'][3]

#Substracting specific value  from a column
df['Fees']=df['Fees']-500
df['Fees']
df.describe()#only work on numerical column not on catagorical column
#above function is also called as 5 number summery

#Re-naming column
df=pd.DataFrame(technologies,index=row_lable)
df.columns=['A','B','C','D']
df
#colums=axis=1,row=axis=0
df2=df.rename({'A':'C1','B':'C2'},axis=1)#column re-name
df2
df2=df.rename({'C':'C1','D':'D2'},axis='columns')#column re-name
df2
df2=df.rename(columns={"A":"A1","B":"B1"})
df2 
#################################################

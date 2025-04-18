# -*- coding: utf-8 -*-
"""
Created on Tue Apr  8 16:26:36 2025

@author: om
"""

import pandas as pd
df = pd.read_csv("C:/3-python_for_DS/melb_data.csv")
df.size
#the size of data set is 404712
df.index
#Out[4]: RangeIndex(start=0, stop=18396, step=1)
df.shape
#(18396, 22)
#there are 18396 rows and 22 columns
df.columns
"""
columns are:
Out[6]: 
Index(['Unnamed: 0', 'Suburb', 'Address', 'Rooms', 'Type', 'Price', 'Method',
       'SellerG', 'Date', 'Distance', 'Postcode', 'Bedroom2', 'Bathroom',
       'Car', 'Landsize', 'BuildingArea', 'YearBuilt', 'CouncilArea',
       'Lattitude', 'Longtitude', 'Regionname', 'Propertycount'],
      dtype='object')  
    
"""
print(len(df.columns))
#their are 22 column
df.describe()
"""
it give 5 no. summary
Out[9]: 
         Unnamed: 0         Rooms  ...    Longtitude  Propertycount
count  18396.000000  18396.000000  ...  15064.000000   18395.000000
mean   11826.787073      2.935040  ...    144.996338    7517.975265
std     6800.710448      0.958202  ...      0.106375    4488.416599
min        1.000000      1.000000  ...    144.431810     249.000000
25%     5936.750000      2.000000  ...    144.931193    4294.000000
50%    11820.500000      3.000000  ...    145.000920    6567.000000
75%    17734.250000      3.000000  ...    145.060000   10331.000000
max    23546.000000     12.000000  ...    145.526350   21650.000000

[8 rows x 14 columns]

"""
##################################
#acess 1 columns
df['Unnamed: 0']
#here we acess Unnamed: 0 column
#acess 2 columns
df[['Suburb','Propertycount']]
#column slicing
df[10:20]
#here we access columns from 10 to 20
#selct columns from starting 3 to end
df[15:]
#selct from staring column to 3
df[:2]
#here we get columns from 0 to 2
df[:]
#here we get all access  of columns
df[::2]
#here we get alternately columns
#access certain cell from column
df['Suburb'][3]
#rename column name
#rename Unnamed: 0  by xyz
df2 = df.rename({'Unnamed: 0 ':'xyz'},axis=1)
df2
df.rename({'Rooms':'qwrt'}, axis=1)
df.head()
df.columns

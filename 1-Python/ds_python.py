# -*- coding: utf-8 -*-
"""
Created on Thu Apr 10 08:19:57 2025

@author: maith
"""

#########################################################
# Drop Rows that has NaN/None/Null Values
# Delete rows with Nan, None
#np.nan, None and ''
import pandas as pd
import numpy as np
technologies={
    'Categories':["Spark","Pyspark","Hadoop","Python"],
    'Fee':[20000,25000,27000,22000],
    'Duration':['','40days',np.nan,None],
    'Discount':[1000,1500,1200,1700] 
    }
indexes=['r1','r2','r3','r4']
df=pd.DataFrame(technologies,index=indexes)
print(df)
df=pd.DataFrame(technologies,index=indexes)
df2=df.dropna() ##dropping np.nan and None
print(df2)


#drop nan and None containing rows
df_clean=df.dropna(subset=['Duration'])

#removing empty strings containing rows as well
df_clean=df_clean[df_clean['Duration']!='']


#############################################
#Converting all the columns into same data type using astype

df=df.astype(str)
df.dtypes

#now converting some specific columni into integer and some to float
df=df.astype({"Fee":int,"Discount":float})
print(df.dtypes)

#doing the same conversionn using a list
cols=["Fee","Discount"]
df=pd.DataFrame(technologies)
df[cols]=df[cols].astype('float') #u are giving the data type with ''
df.dtypes

"""But Python (specifically, pandas) is designed to interpret that
 string as the name of a data type.
 'float' is a string → pandas internally
 looks it up in a type mapping dictionary.
It knows 'float' → maps to Python's float class (float).
So pandas reads it as: "Convert this column to type float."
"""
#by using for loop
for col in ['Fee','Discount']:
    df[col]=df[col].astype('float')
    
    
#Raising or ignoring error while conversion of column is failed
df=df.astype({"Categories":int},errors='ignore')
df.dtypes

df=df.astype({"Categories":int},errors='raise')

####################################################
#using DataFrame.to_numeric() to convert data to numeric
df["Fee"]=pd.to_numeric(df["Fee"])
df.dtypes
##
#converting multiple to numeric type using apply method
df=pd.DataFrame(technologies)
df.dtypes
df[['Fee','Discount']]=df[['Fee','Discount']].apply(pd.to_numeric)
df.dtypes

#quic example to get number of rows in Data frame
rows_count=len(df.index)
row_count=len()

#Using DataFrame.apply to apply somwthing to column
import pandas as pd
import numpy as np
data=[(3,5,7),(2,4,6),(5,8,9)]
df=pd.DataFrame(data,columns=['A','B','C'])


#adding 3 into all cells using apply()
def add_3(x):
    return x+3
df2=df.apply(add_3)

#using apply() modify only single column
import pandas as pd
df=pd.DataFrame(data,columns=['A','B','C'])
def add_4(x):
    return x+4
df['B']=df['B'].apply(add_4)

#for multiple columns
#using lambda function

df["A"]=df["A"].apply(lambda x:x-2)
df

#using panads.dataframe.transform
df
def add_2(x):
    return x+2 
df=df.transform(add_2)

#using map function
df['A']=df['A'].map(lambda A:A/2)
print(df)

'''
why does it become int32?
pandas internally choose the most efficeint
platform-dependent Numpy dtype that corresponds
to Python's int. This depends on your operating system
and Python/Numpy version:
On 32 -bit system, int usually maps to int32
On 64-bit systems, int often maps to int64
However, sometimes due to memory optimization
or system constraints, pandas might still pick int32
even on a 64-bit system

'''
import pandas as pd
import numpy as np

# Creating the dictionary
technologies = {
    'Categories': ["Spark", "Pyspark", "Hadoop", "Python"],
    'Fee': [20000, 25000, 27000, 22000],
    'Duration': ['', '40days', np.nan, None],
    'Discount': [1000, 1500, 1200, 1700]
}

# Converting the dictionary to a DataFrame
df = pd.DataFrame(technologies)

# Explicitly controlling the dtype
df = df.astype({"Fee": "int64", "Discount": "float64"})
df.dtypes
#####################################################
import pandas as pd
import numpy as np

data = [(3,5,7),(2,4,6),(5,8,9)]
df = pd.DataFrame(data, columns = ['A','B','C'])
print(df)

#Using Numpy.square() Method
#Using numpy.square() and [] operator
df['A'] = np.square(df['A'])
print(df)

##################
# Pandas groupby() With Examples
import pandas as pd
technologies = {
    'Courses': ["Spark", "PySpark", "Hadoop", "Python","Pandas", "Hadoop", "Spark", "Python" ,"NA"],
    'Fee': [22000, 25000, 23000, 24000,26000,25000, 25000, 22000, 1500],
    'Duration': ['30days', '50days', '55days', '40days', '60days','35days','30days', '50days','40days'],
    'Discount': [1000, 2300, 1000, 1200, 2500, None,1400,1600,0]
}

df = pd.DataFrame(technologies)
print(df)

'''
OUTPUT:
  Courses    Fee Duration  Discount
0    Spark  22000   30days    1000.0
1  PySpark  25000   50days    2300.0
2   Hadoop  23000   55days    1000.0
3   Python  24000   40days    1200.0
4   Pandas  26000   60days    2500.0
5   Hadoop  25000   35days       NaN
6    Spark  25000   30days    1400.0
7   Python  22000   50days    1600.0
8       NA   1500   40days       0.0
'''

#Use groupby() to continue the sum
df2 = df.groupby(['Courses']).sum()
print(df2)
'''
OUTPUT:
           Fee      Duration  Discount
Courses                               
Hadoop   48000  55days35days    1000.0
NA        1500        40days       0.0
Pandas   26000        60days    2500.0
PySpark  25000        50days    2300.0
Python   46000  40days50days    2800.0
Spark    47000  30days30days    2400.0
'''
######################################
# Add Index of grouped Data
# Add Row Index to the group by result
df2 = df.groupby(['Courses','Duration']).sum().reset_index()
print(df2)

'''
Output:
    Courses  Duration Fee     Discount
0   Hadoop   35days  25000       0.0
1   Hadoop   55days  23000    1000.0
2       NA   40days   1500       0.0
3   Pandas   60days  26000    2500.0
4  PySpark   50days  25000    2300.0
5   Python   40days  24000    1200.0
6   Python   50days  22000    1600.0
7    Spark   30days  47000    2400.0

'''

# Get the lists of all column names from headers
column_headers = list(df.columns.values)
print("The Column Headers:",column_headers)
'''
The Column Headers: ['Courses', 'Fee', 'Duration', 'Discount']
'''
#########################################
# Using list(df) to get the column headers as a list
column_headers = list(df.columns)
column_headers
'''
Out[74]:['Courses', 'Fee', 'Duration', 'Discount']
'''

# Using list(df) to get the list of all Column Names
column_headers = list(df)
column_headers
'''
Out[75]: ['Courses', 'Fee', 'Duration', 'Discount']
'''
##########################################################
# Pandas Shuffle DataFrame 
import pandas as pd
technologies = {
    'Courses': ["Spark", "PySpark", "Hadoop", "Python","Pandas", "Oracle", "Java" ],
    'Fee': [22000, 25000, 23000, 24000,26000,25000, 25000 ],
    'Duration': ['30days', '50days', '55days', '40days', '60days','35days','30days' ],
    'Discount': [1000, 2300, 1000, 1200, 2500 ,1400,1600]
}

df = pd.DataFrame(technologies)
print(df)
'''
Output:
     Courses Fee    Duration    Discount
0    Spark  22000   30days      1000
1  PySpark  25000   50days      2300
2   Hadoop  23000   55days      1000
3   Python  24000   40days      1200
4   Pandas  26000   60days      2500
5   Oracle  25000   35days      1400
6     Java  25000   30days      1600
'''
# Pandas Shuffle Dataframe Rows
# Shuffle the dataframe rows and return all rows
df1 = df.sample( frac = 1)
print(df1)
'''
Output:
    Courses Fee     Duration    Discount
3   Python  24000   40days      1200
4   Pandas  26000   60days      2500
0    Spark  22000   30days      1000
5   Oracle  25000   35days      1400
6     Java  25000   30days      1600
1  PySpark  25000   50days      2300
2   Hadoop  23000   55days      1000
'''
###############################
# Create a new Index starting from 0
df1 = df.sample(frac = 1).reset_index()
print(df1)
'''
index      Courses Fee     Duration    Discount
0      2   Hadoop  23000   55days      1000
1      4   Pandas  26000   60days      2500
2      1  PySpark  25000   50days      2300
3      6     Java  25000   30days      1600
4      3   Python  24000   40days      1200
5      0    Spark  22000   30days      1000
6      5   Oracle  25000   35days      1400
'''

#############################
# Drop shuffle Index
df1 = df.sample(frac = 1).reset_index(drop=True)
print(df1)

'''
Output:
    Courses Fee     Duration    Discount
0   Oracle  25000   35days      1400
1   Python  24000   40days      1200
2  PySpark  25000   50days      2300
3   Pandas  26000   60days      2500
4    Spark  22000   30days      1000
5   Hadoop  23000   55days      1000
6     Java  25000   30days      1600

'''
###########################################
import pandas as pd
technologies = {
    'Courses': ["Spark", "PySpark", "Python","Pandas" ],
    'Fee': [20000, 25000, 22000, 30000 ],
    'Duration': ['30days', '40days', '35days', '50days'] 
}

index_labels = ['r1', 'r2', 'r3', 'r4']
df1 = pd.DataFrame(technologies,index = index_labels)

technologies2 = {
    'Courses':["Spark", "Java", "Python","Go" ],
    'Discount' : [2000, 2300, 1200, 2000]
    }
index_labels2 = ['r1','r6', 'r3' ,'r5']
df2 = pd.DataFrame(technologies2, index = index_labels2)

# pandas jpoins
df3 = df1.join(df2, lsuffix="_left", rsuffix="_right")
print(df3)

'''
Courses_left    Fee Duration Courses_right  Discount
r1        Spark  20000   30days         Spark    2000.0
r2      PySpark  25000   40days           NaN       NaN
r3       Python  22000   35days        Python    1200.0
r4       Pandas  30000   50days           NaN       NaN
'''

##############################
# pandas inner join DataFrame
df3 = df1.join(df2, lsuffix="_left", rsuffix="_right",how ='inner')
print(df3)
'''
     Courses_left Fee    Duration Courses_right  Discount
r1        Spark  20000   30days         Spark      2000
r3       Python  22000   35days        Python      1200
'''
#############################
# Right join DataFrame
df3 = df1.join(df2, lsuffix="_left", rsuffix="_right",how ='right')
print(df3)
'''
Output:
     Courses_left  Fee    Duration Courses_right  Discount
r1        Spark  20000.0   30days         Spark      2000
r6          NaN      NaN      NaN          Java      2300
r3       Python  22000.0   35days        Python      1200
r5          NaN      NaN      NaN            Go      2000

'''
################################
# left join DataFrame
df3 = df1.join(df2, lsuffix="_left", rsuffix="_right",how ='left')
print(df3)

'''
Output:
      Courses_left    Fee Duration Courses_right  Discount
   r1        Spark  20000   30days         Spark    2000.0
   r2      PySpark  25000   40days           NaN       NaN
   r3       Python  22000   35days        Python    1200.0
   r4       Pandas  30000   50days           NaN       NaN
'''
################################
# Pandas Merge 
import pandas as pd
technologies = {
    'Courses': ["Spark", "PySpark", "Python","Pandas" ],
    'Fee': [20000, 25000, 22000, 30000 ],
    'Duration': ['30days', '40days', '35days', '50days'] 
}

index_labels = ['r1', 'r2', 'r3', 'r4']
df1 = pd.DataFrame(technologies,index = index_labels)

technologies2 = {
    'Courses':["Spark", "Java", "Python","Go" ],
    'Discount' : [2000, 2300, 1200, 2000]
    }
index_labels2 = ['r1','r6', 'r3' ,'r5']
df2 = pd.DataFrame(technologies2, index = index_labels2)

# Using pandas.merge()
df3 = pd.merge(df1,df2)
print(df3)
df3 = df1.merge(df2)
print(df3)
'''
  Courses    Fee Duration  Discount
0   Spark  20000   30days      2000
1  Python  22000   35days      1200
'''
####################################
# Use pandas.concate 
df1 = pd.DataFrame({'Courses':["Spark","PySpark","Python","Pandas"],
                    'Fees':[20000, 25000, 22000,24000]})
df2 = pd.DataFrame({'Courses':["Pandas","Hadoop","Hyperion","java"],
                    'Fees':[25000, 25200, 24500,24900]})

# Using pandas.concat() to concat two DataFrame
data = [df1,df2]
df2 = pd.concat(data)
df2
'''
Output:
    Courses   Fees
0     Spark  20000
1   PySpark  25000
2    Python  22000
3    Pandas  24000
0    Pandas  25000
1    Hadoop  25200
2  Hyperion  24500
3      java  24900
'''
###########################################
df = pd.DataFrame({'Courses':["Spark","PySpark","Python","Pandas"],
                   'Fees':[20000,25000,22000,24000]})
df1 = pd.DataFrame({'Courses':["Unix","Hadoop","Hyperion","Java"],
                    'Fees':[25000,25200,24500,24900]})
df2 = pd.DataFrame( {'Duration':['30days','40days','35days','60days','55days'],
                     'Discount':[1000,2300,2500,2000,3000]})

df3 = pd.concat([df, df1,df2])
print(df3)

'''
Output:
    Courses     Fees Duration  Discount
0     Spark  20000.0      NaN       NaN
1   PySpark  25000.0      NaN       NaN
2    Python  22000.0      NaN       NaN
3    Pandas  24000.0      NaN       NaN
0      Unix  25000.0      NaN       NaN
1    Hadoop  25200.0      NaN       NaN
2  Hyperion  24500.0      NaN       NaN
3      Java  24900.0      NaN       NaN
0       NaN      NaN   30days    1000.0
1       NaN      NaN   40days    2300.0
2       NaN      NaN   35days    2500.0
3       NaN      NaN   60days    2000.0
4       NaN      NaN   55days    3000.0

'''

# Read CSV file into DataFrame
df = pd.read_csv('Courses.csv')
print(df)
###############################
# Write DataFrame to Excel file
df.to_excel('E:/1-Python/Courses.xlsx')
################################
import pandas as pd
# Read Excel file
df = pd.read_excel('E:/1-Python/Courses.xlsx')
print(df)

#########################################################

##############
'''NumPy'''
##############
# all()
import numpy as np
x = np.array([1,2,3])
x
np.all(x) #True
x = np.array([1,2,3,0])
np.all(x)

# any()
x = np.array([1,2,3,0])
np.any(x) #True

# isfinite()
x = np.array([1,2,np.nan,np.inf])
x
np.isfinite(x) #array([ True,  True, False, False])

# isnan()
np.isnan(x) #array([False, False,  True, False])


x = np.array([3,5])
y = np.array([2,5])
np.greater(x,y) #Output:array([ True, False])
np.greater_equal(x,y) #Output:array([ True, True])

array_2D = np.identity(3)
array_2D
'''
array([[1., 0., 0.],
       [0., 1., 0.],
       [0., 0., 1.]])
'''

rand_No = np.random.normal(0,1,2)
rand_No
'''
Out[46]: array([1.31853518, 0.30054412])
'''
a = np.arange(10,22)
a
'''
Out[47]: array([10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21])
'''

#####################
import numpy as np
lst = [1,2,3]
arr = np.array(lst)
arr
arr.ndim  #Out[52]: 1
arr.shape #Out[53]: (3,)
type(arr) #Out[54]: numpy.ndarray
arr_two = np.array([[1,2,3],
                   [3,4,5],
                   [6,7,8]])

arr_two.ndim   #Out[56]: 2
arr_two.shape  #Out[57]: (3, 3)

mat = np.matrix([[1,2,3],
                 [4,5,6],
                 [6,7,8]])
mat.ndim   #Out[59]: 2
mat.shape  #Out[60]: (3, 3)

#################################
arr = np.random.randint(1,100,9)
arr #Store random 9 number from 1 to 100 ,Out[62]: array([85, 78, 32, 44, 87, 63, 78, 76, 21])
arr.ndim #Out[63]: 1

new_arr = arr.reshape(3,3)
new_arr.ndim    #Out[65]: 2
new_arr.ravel() # Convert multi dimentinal arrray into single direction array([85, 78, 32, 44, 87, 63, 78, 76, 21])
arr[2]

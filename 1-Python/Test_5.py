# -*- coding: utf-8 -*-
"""
Created on Wed Apr 16 08:16:18 2025

@author: maith
"""

'''
1.Write a NumPy program to create an element-wise  comparison (greater, greater_equal, less and less_equal) of two given arrays.
'''
import numpy as np
arr1 = np.array([1,2,3,4])
arr2 = np.array([3,1,3,2])

print("Element of arr1 is greater than the element of arr2:",np.greater(arr1,arr2))
print("Element of arr1 is greater or equal to the element of arr2:",np.greater_equal(arr1, arr2))
print("Element of arr1 is less than to the element of arr2:",np.less(arr1,arr2))
print("Element of arr1 is less or equal to the element of arr2:",np.less_equal(arr1,arr2))
#########################################################################

'''
2.	You are given the following data about employees in a company:
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
    'Age': [25, 30, 35, 45, 28],
    'Department': ['HR', 'IT', 'Finance', 'IT', 'HR'],
    'Joining_Year': [2018, 2016, 2015, 2019, 2020]
            }
  Create a DataFrame from the above dictionary and Display the following:
o	The first 2 rows
o	The column names
o	Data types of each column
o	Summary statistics for numeric columns.
'''
import pandas as pd

data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
    'Age': [25, 30, 35, 45, 28],
    'Department': ['HR', 'IT', 'Finance', 'IT', 'HR'],
    'Joining_Year': [2018, 2016, 2015, 2019, 2020]
            }

df=pd.DataFrame(data)

print("First Two rows data\n:",df.head(2))
print("Name of Columns:",df.columns.tolist())
print("Data Type:\n",df.dtypes)
print("Summary statistics:\n",df.describe())
########################################################
'''
3.	Extend the DataFrame from Question 2:
•	Add a new column called Salary with values: [50000, 60000, 70000, 65000, 48000].
•	Calculate a new column Experience as 2025 - Joining_Year.
•	Create a new column Seniority:
o	'Junior' if experience < 5 years
o	'Mid' if 5 <= experience < 8 years
o	'Senior' if experience >= 8 years
'''
df['Salary']=[50000, 60000, 70000, 65000, 48000]
df['Experience']= 2025-df['Joining_Year']
print("\nExtended DataFrame:\n", df)
df['Seniority']=
################################################################
'''
4.	Write a NumPy program to compute the multiplication of two given matrixes.
 p = [[1, 0], [0, 1]]
 q = [[4, 2], [1, 3]]
'''
import numpy as np

p=np.array([[1,0],[0,1]])
q=np.array([[4,2],[1,3]])

print(np.dot(p,q))
##############################################################
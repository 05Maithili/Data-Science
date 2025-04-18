# -*- coding: utf-8 -*-
"""
Created on Wed Apr 16 16:44:15 2025

@author: maith
"""

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
df=pd.read_csv(r"E:\2-Python\Salary_Data.csv")
df.columns = ['Age','Gender','Education', 'Job', 'Exp','Salary']

# Histograms
plt.hist(df.Age, bins=10, edgecolor='black', alpha=0.7)
plt.title('Age distribution')
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.show()

# Scatter
plt.scatter(df.Age,df.Salary,color='lightblue', alpha=0.7)
plt.title('Age vs Salary')
plt.xlabel('Age')
plt.ylabel('Salary')
plt.show()

# Correlation
corr = df.corr(numeric_only=True)
plt.imshow(corr, cmap='coolwarm', interpolation='none')
plt.colorbar()
plt.xticks(range(len(corr)),corr.columns, rotation=45)

# Boxplot
plt.boxplot(df.Age)
plt.title('Age Distribution')
plt.show()

# Bar
df.Age.value_counts().plot(kind='bar',color='orange')
plt.title('Age Distribution')
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.show()

# Pie


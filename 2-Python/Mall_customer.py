# -*- coding: utf-8 -*-
"""
Created on Wed Apr 16 15:11:54 2025

@author: maith
"""

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
df=pd.read_csv(r"E:\2-Python\Mall_Customers.csv")
df.columns = ['customer_id','Gender','Age','Annual_income','Spending_score']
sns.displot(df.Age,kde=True)
sns.displot(df.Annual_income,kde=True)
sns.displot(df.Spending_score, kde=True)
sns.displot(df.Gender, kde=True)
df.dtypes
sns.jointplot(x=df.Age, y=df.Spending_score)
#maximum spending occurs during 20-30, even at 50 too
sns.jointplot(x=df.Age,y=df.Spending_score, kind='reg')
#Spending reduces as age increases
sns.jointplot(x=df.Age, y=df.Spending_score, kind='hex')
sns.pairplot(df,hue='Gender')
sns.pairplot(df,hue='Age')
sns.pairplot(df,hue="Spending_score",kind='reg')

# Histograms
plt.hist(df.Age, bins=10, edgecolor='black', alpha=0.7)
plt.title('Age distribution')
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.show()
#for annual income
plt.hist(df.Annual_income, bins=20, edgecolor='black', alpha=0.6)
plt.title("Annual oincome distribution")
plt.xlabel("Annual income")
plt.ylabel("Frequency")
plt.show()
#for spending score
plt.hist(df.Spending_score, bins=10, edgecolor='purple', alpha=0.6)
plt.title('Spending score Distribution')
plt.xlabel('Spending score')
plt.ylabel('Frequency')
plt.show()


# Scatter
plt.scatter(df.Age,df.Annual_income,color='lightblue', alpha=0.7)
plt.title('Age vs Annual_income')
plt.xlabel('Age')
plt.ylabel('Annual Income')
plt.show()
# for age and spending score
plt.scatter(df.Age, df.Spending_score, color='Lightgreen',alpha=0.7)
plt.title("Age VS Spending Score")
plt.xlabel('Age')
plt.ylabel("Spending Score")
plt.show()
corr = df.corr(numeric_only=True)
'''As value of correlation coeffient of age and spending score is negative so it is negatively correlate and as the value is small so it is slightly negatively correlated'''
# Correlation
corr = df.corr(numeric_only=True)
plt.imshow(corr, cmap='coolwarm', interpolation='none')
plt.colorbar()
plt.xticks(range(len(corr)),corr.columns, rotation=45)

# Boxplot
plt.boxplot(df.Age)
plt.title('Age Distribution')
plt.show()
# it is right skewed graph 
plt.boxplot(df.Spending_score)
plt.title('Spending score Distribution')
plt.show()

# Bar
df.Age.value_counts().plot(kind='bar',color='orange')
plt.title('Age Distribution')
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.show()

#Pie
df.Gender.value_counts().plot(kind='pie', autopct='%1.1f%%')
plt.title('Gender Distribution')
plt.ylabel('')
plt.show()

# Scatter plot with regression line
from numpy.polynomial.polynomial import polyfit
x = df.Age
y = df.Spending_score
b,m = polyfit(x, y, 1) #1 is degree of the polynomial to fit
plt.scatter(x, y, alpha=0.5)
plt.plot(x, m*x+b, color='purple') #m*x+b is an line equation
plt.title('Age vs Spending Score with Trend line')
plt.xlabel('Age')
plt.ylabel('Spending Score')
plt.show()

# Pairwise scatter matrix(subset of features)
pd.plotting.scatter_matrix(df[['Age','Annual_income','Spending_score']], figsize=(8,8))
plt.suptitle('Pairwise Scatter Matrix')
plt.show()

# Gender distribution
gender_counts = df.Gender.value_counts()

# Pie chart
gender_counts.plot(kind='pie', autopct='%1.1f%%', startangle=90)
plt.ylabel('')
plt.title('Gender Distribution')
plt.show()

# Bar chart
gender_counts.plot(kind='bar', color=['skyblue','salmon'],edgecolor='black')
plt.title('Gender Distribution')
plt.ylabel('Count')
plt.show()

# Correlation heatmap
import numpy as np
import seaborn  as sns # minimal use here just for heatmap

corr = df[['Age','Annual_income','Spending_score']].corr()
plt.imshow(corr, cmap='coolwarm', interpolation='none')
plt.colorbar()
plt.xticks(range(len(corr)), corr.columns, rotation=45)
plt.yticks(range(len(corr)), corr.columns)
plt.title('Correlation Heatmap')
plt.show()
# spending score and annual income slightly correlated
# spending score and age negatively slightly correlated
# age score and annual income slightly correlated
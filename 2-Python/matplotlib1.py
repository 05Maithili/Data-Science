# -*- coding: utf-8 -*-
"""
Created on Wed Apr 16 15:13:12 2025

@author: maith
"""

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# load dataset
tips = sns.load_dataset('tips')

# 1. Histogram of total_bill
plt.hist(tips['total_bill'],bins=20, color='red', edgecolor='black')
plt.title('Total Bill Distribution')
plt.xlabel('Total Bill')
plt.ylabel('Count')
plt.show

# 2. Histogram of tip
plt.hist(tips['tip'], bins=20, color='lightgreen', edgecolor='black')
plt.title('Tip Distribution')
plt.xlabel('Tips')
plt.ylabel('Count')
plt.show()
#it is right skewed 

# 3.Scatter plot of tip vs total_bill
plt.scatter(tips['tip'], tips['total_bill'], color='purple',alpha=0.6)
plt.title('Tip vs Total Bill')
plt.xlabel('Tip')
plt.ylabel('Total Bill')
plt.show();
# tip and total bill are linearly correlated
# linearly correlated:
    
# 4. Simple correlation heatmap
corr = tips.corr(numeric_only=True) # Find numeric correlation coeffient
plt.imshow(corr, cmap='coolwarm', interpolation='none')
plt.colorbar()
plt.xticks(range(len(corr)), corr.columns, rotation=45)

'''
plt.xticks(...)
This function controls the labels on the x-axis:
Where the ticks are placed
What labels are shown.
How the labels are rotated or styled.

range(len(corr))
This generates the positions for the ticks:
    corr is a square matrix (like 3x3 if there are 3 numeric columns)
    len(corr) gives how many columns (and rows) there are, say:3.
    range(len(corr))-> [0,1,2] -> places ticks at position 0,
    corr.columns
    These are the labels for those ticks positions:
         ['total_bill', 'tip', 'size']
         so now you're labeling tick 0 as 'total bill' ,tick 1 as "tip"
'''

plt.yticks(range(len(corr)),corr.columns)
plt.title("Correlation Matrix")
plt.show()

# 5. Boxplots
plt.boxplot(tips['total_bill'])
plt.title('Boxplot-Total Bill')
plt.show()

plt.boxplot(tips['tip'])
plt.title('Boxplot-Tip')
plt.show()

# 6. Count of days
tips['day'].value_counts().plot(kind='bar', color='orange')
plt.title('Count by Day')
plt.xlabel('Day')
plt.ylabel('Count')
plt.show()
# in this 

# 7. Count of gender
tips['sex'].value_counts().plot(kind='bar',color='lightblue')
plt.title('Count by Gender')
plt.xlabel('Gender')
plt.ylabel('Count')
plt.show()
# in that restaurant male custmor are more as compare to female

# 8. Gender pie chart
tips['sex'].value_counts().plot(kind='pie', autopct='%1.1f%%')
 
'''
The autopct = '%1.1f%%' parameter is used in
Matplotlib's pie() function to display the 
percentage value on each slice of a pie chart.

Breakdown of '%1.1f%%':
    % starts a formatting string.
    
    1.1f means:
        1 = minimum width of the number(not strictly needed here).
        .1f = format the number as a float with 1 decimal place.
        The final %% is to display a literal percent sign %
        (because % has special meanning in formatting string,
         so we escape it with another %)
'''
plt.title('Gender Distribution')
plt.ylabel('')
#even though pie charts doent have y axis
#matplotlib still has that axis object in the
#background . so setting ylabel('') just makes
#sure nothing is displayed there
plt.show()
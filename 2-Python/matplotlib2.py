# -*- coding: utf-8 -*-
"""
Created on Thu Apr 17 15:07:48 2025

@author: maith
"""

#############################################################
# Write python program to draw a line with
# suitable label in the x axis, y axis and a title
import matplotlib.pyplot as plt
X = range(1,50)
Y = [value * 3 for value in X]
print("Values of X:")
print(*range(1,50))
print("Values of Y (thrice of X):")
print(Y)

#Plot lines and/or markers to the Axes.
plt.plot(X,Y)
# Set the x axis label of the current axis
plt.xlabel('x-axis')
# Set the y axis label of the current axis.
plt.ylabel('y-axis')
# Set title
plt.title('Draw a line')
# Show/Display the figure
plt.show()

###########################################################
# Write a Python program to draw a line
# using given axis values with suitable label
# in the x axis , y axis and a title.
import matplotlib.pyplot as plt
x=[1,2,3]
y=[2,4,1]
#Plot lines and/or markers to the Axes.
plt.plot(x,y)
# Set the x axis label of the current axis
plt.xlabel('x-axis')
# Set the y axis label of the current axis.
plt.ylabel('y-axis')
# Set title
plt.title('Sample Graph')
# Show/Display the figure
plt.show()

###########################################################
# Write a python program to draw line charts of
# the finacial data of Alphabatic 
# between October 3, 2016 to October 7, 2016

import matplotlib.pyplot as plt
import pandas as pd
df = pd.read_csv(r"E:\2-Python\fdata.csv")
df.plot()
plt.show()

#############################################################
# Write a python program to plot two or
# more lines with legends, different widths and colors

import matplotlib.pyplot as plt
# line 1 plot
x1 = [10,20,30]
y1 = [20,40,10]

# line 2 plot
x2 = [10,20,30]
y2 = [40,10,30]

# Set the x axis and y axis label of the current axis
plt.xlabel('x-axis')
plt.ylabel('y-axis')
#Set the title
plt.title('Two or more lines with difference width and colors')
#Display 
plt.plot(x1,y1, color='blue' , linewidth = 3, label = 'line1-width-3')
plt.plot(x2,y2, color='red' , linewidth = 5, label = 'line2-width-5')
plt.legend()
plt.show()

####################################################
# Write a python program to plot  two or more
# lines with different styles

import matplotlib.pyplot as plt

x1=[10,20,30]
y1=[20,40,10]
x2=[10,20,30]
y2=[40,10,30]
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.title('Two or more lines with different style and colors')
plt.plot(x1,y1, color='purple', linewidth=3, label='line1-dotted', linestyle='dotted')
plt.plot(x2,y2, color='lightgreen', linewidth=5, label='line1-dotted', linestyle='dotted')
plt.legend()
plt.show()

##################################################################
# write a python program to plot two or more
# lines and set the line markers
import matplotlib.pyplot as plt
# y and x axis values
x=[1,4,5,6,7]
y=[2,6,3,6,3]
# plotting the points
plt.plot(x,y,color='red',linestyle='dashdot', linewidth=3, marker='o' , markerfacecolor='green',markersize=12)
# Set the y-limits of the current axes
plt.ylim(1,8)
# Set the x-limits of the current axes
plt.xlim(1,8)
# naming the x and y axis
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.title('Display marker')
plt.show()
##########################################################################################
# Write a python program to plot several lines
# With different format styles in one command
# using array
import numpy as np
import matplotlib.pyplot as plt

# Sample time at 200ms intervals
t = np.arange(0.,5.,0.2)

# green dashes, blue squares and red triangles
plt.plot(t,t,'g--',t,t**2,'bs',t,t**3,'r^')
'''
x=t, y=t
'g--' = green (g) dashed line(--)
plots a diagonal dashed green line (y = x)

t, t**2, 'bs'
x = t, y= t**2 (squares)
'bs' = blue(b) squares (s) as ,markers
Plots t^2 as blue squares

t, t**3, 'r^'
x = t, y = t**3 (cubes)
'r^' = red (r) triangle-up markers (^)
Plots t³ as red triangles

'''
plt.show()
########################################################
# Use of plt.xticks
import matplotlib.pyplot as plt
x_pos = [0,1,2,3]
x = ['Apple', 'Banana', 'Mango','Orange']

plt.bar(x_pos, [10,15,7,12])
plt.xticks(x_pos, x)
plt.ylabel('Quantity')
plt.title('Fruit Stock')
plt.show()
##########################################################

#Write a python program to display bar chart of the popularity of the programming language
import matplotlib.pyplot as plt
x=['Java', 'Python', 'PHP', 'Javascript', 'C#', 'C++']
popularity = [22.2 , 17.6, 8.8, 8, 7.7, 6.7]
x_pos = [i for i , _ in enumerate(x)]
'''
x_pos = [i for i, _ in enumerate(x)]
This creates a list of index positions for each language

enumerate(x) gives (index, language) pairs:
    (0,'Java'),(1,'Python'),......,(5,'C++')

[i for i , _ in enumerate(x)] extracts just the indices:
x_pos = [0,1,2,3,4,5]    
'''
plt.bar(x_pos, popularity, color='blue')
plt.xlabel("Languages")
plt.ylabel("Popularity")
plt.title("Popularity of Programming languagr\n"+"Worldwide, oct 2017 compared to a year ago")
plt.xticks(x_pos,x)
plt.show()

##################################################################################
#Write 
import matplotlib.pyplot as plt
x=['Java', 'Python', 'PHP', 'Javascript', 'C#', 'C++']
popularity = [22.2 , 17.6, 8.8, 8, 7.7, 6.7]
x_pos = [i for i , _ in enumerate(x)]
plt.barh(x_pos, popularity, color='green')
plt.xlabel("Languages")
plt.ylabel("Popularity")
plt.title("Popularity of Programming languagr\n"+"Worldwide, oct 2017 compared to a year ago")
plt.yticks(x_pos,x)
plt.show()
##########################################################
#Write a python program to create bar plot 
#of scores by group and gender
#Use multiple X values on the same chart
#for men and women
import numpy as np
import matplotlib.pyplot as plt
# data to plot 
n_groups = 5
men_means = (22,30,33,30,26)
women_means = (25,32,30, 35,29)
# create plot
fig, ax = plt.subplots()
index = np.arange(n_groups)
bar_width = 0.35
opacity = 0.8
rects1 = plt.bar(index, men_means, bar_width, alpha = opacity, color='g', label='Men')
rects2 = plt.bar(index, women_means, bar_width, alpha=opacity, color='r', label='Women')
plt.xlabel('Person')
plt.ylabel('Scores')
plt.title('Scores by  person')
plt.xticks(index + bar_width, ('G1','G2','G3','G4','G5'))
plt.legend()
plt.tight_layout()
plt.show()
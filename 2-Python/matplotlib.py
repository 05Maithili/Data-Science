# -*- coding: utf-8 -*-
"""
Created on Tue Apr 15 08:24:34 2025

@author: maith
"""
##################################################################
#matplotlib ,seaborn#
import matplotlib.pyplot as plt
import seaborn as sns
tips = sns.load_dataset('tips')
tips.head()
sns.displot(tips.total_bill, kde = True)
sns.displot(tips.tip,kde = True)
 
#The distribution is right- skewed
#(positively skewed)-meaning most
#total bills are on the lower side (left),
#but there are a few large bills that stretch
#the distribution to the right
#this is typical in restaurant or service data,
#where most meals fall within an average range,
#but a few parties may spend much more.
#sns.displot(tips.size,kde = True)
sns.jointplot(x = tips.tip, y= tips.total_bill ,kind='reg')

'''
scattere plot(center):
    Each point represents one observation 
    (a customer's bill and the coresponding tip).
     There's a positive correlation: as the total bill
     increases, the tip tends to increases as well.
     However, the increase is not perfectly
     linear-some variation exists,
     especially for higher bills.
     Histogram on the X - axis (Top):
         Shows the distribution of tip amounts.
         Most tip fall batween $2 and $4,
         with fewer tips at the higher end.
     Histogram on Y-axis(Right):
         Shows the distribution of total_bill.
         The majority of billare in the $10-$20 range 
'''
sns.jointplot(x=tips.tip, y=tips.total_bill,kind ='hex')
sns.pairplot(tips,kind='reg')

'''
total_bill vs tip
Positive correlation: As the total bill increases,
the tip amount generally increases.
The points are fairly spread,
but there's a visible upward trend.

total_bill vs size
Weak positive correlation : larger group sizes tend 
to have higher total bills.

Still, there's a lot of overlap-small
groups can also have high bills.

tips vs size
Weak correlation:Bigger groups don't always
give higher tips.
Most tips, even in larger groups,
still over around $2-$5.
'''

tips.time.value_counts()
sns.pairplot(tips, hue='time')
'''
This is an advanced pair plot with hue- based 
grouping, showing comparisons between 
lunch vs dinner based on:
total_bill
tip
size(party size)

total_bill Distribution:
    Dinner (orange) bills tend to be higher than lunch
    (blue ) bills.
    Dinner shows a wider spread, peaking higher around the $15-$20
Lunch bills are more tightly clustered under $20.
tip Distribution:
Tips during dinner are also generally higher
tha those of lunch.
The distribution for dinner is broader
and more positively skewed.
size (Party size) Distribution:
Dinner has larger party sizes overall.    
'''
sns.pairplot(tips,hue='day')
'''
total_bill Distribution:
    Saturday shows the highest frequency of large bills.
    Sunday follows closely with a broad range bills.
    Friday has a narrower spread indicating fewer total bills, mostly lower.
Tip follow a similar trend to total bill 
'''
################################################
import matplotlib.pyplot as plt
import seaborn as sns
tips=sns.load_dataset("tips")
tips.head()
sns.displot(tips.total_bill,kde=True)  #here the kde is used to show the line of ditribution 
sns.jointplot(x=tips.tip,kde=True)
'''distribution is right skewed most of the cutomers have given the tips on the left side between 1 to 4 dollar '''
sns.displot(tips.size,kde=True)
sns.jointplot(x=tips.tip,y=tips.total_bill,kind='hex') #hex is used to represent in the form of hexagoan
'''kind='reg'#reg is to add density line '''

'''catter plot(centre):
    each point represent oberservation of each customer (a customers bills coresponds to the tip)
    there is a positive correalation as  total bill increases the tips is also increase however the increased is not perfectly liner-some varition also exist especially for the higher bills histogram on the top is for the x axis 
    shows the sistribution of the tip amount ,most tips falls between 2 and 5
    with fewer falls at the higher end 
    and historgram in the right side is for the y axis 
    show the distribution of total bills 
    the mahority of bills are in the 10 to 20 dollrs range '''
    
sns.pairplot(tips,kind='reg')

sns.displot(tips.sex,kde=True)
sns.jointplot(x=tips.sex,y=tips.tip,kind='hex')


tips.time.value_counts()
sns.pairplot(tips,hue="time")
'''there are more no of cutomers are present int the dinner time as compared to the lunch time '''
sns.pairplot(tips,hue="sex",kind='reg')
'''mens have given more noo of tips as compared to the femals '''
sns.pairplot(tips,hue="smoker",kind='reg')
'''there are less smokers are present as compared to smoker '''
sns.pairplot(tips,hue="day",kind='reg')
'''the no of cutomers are high in saturday  and most tips are given in  saturday also the total bills are also maximum in saturday'''

'''sunday follows closely with a broad range of bills 
friday has a narrower spread 
indicating fewer total bills,mostly lower
thurday (blue) is more consistent but less frequent than weekends.tips follows the same trend like total bills '''

sns.heatmap(tips.corr(numeric_only=True),annot=True)
'''
Understanding Correlation Coefficients
Ranges from -1 to +1.
+1->perfect positive correlation(both increases together)
0->no coorelation
-1->perfect negative correlation(one increases, the)
total_bill & tip  0.68   strong positive correlation
total_bill & size  0.50  moderate positive correlation
tip & size 0.49 Moderate correaltion- bigger group
'''
tips.dtypes
sns.boxplot(tips.total_bill)#their are outliers in total bill
sns.boxplot(tips.tip)
sns.countplot(x = 'day' , data = tips)#highest number of customer are on saturday
sns.countplot(y = 'sex' , data = tips)#male customer are more than female
tips.sex.value_counts().plot(kind='pie')
tips.sex.value_counts().plot(kind='bar')

sns.countplot(data = tips[tips.time == 'Dinner'], x = 'day')
sns.countplot(data = tips[tips.time == 'Lunch'],x='day')

fg = sns.FacetGrid(tips,row = 'smoker',col = 'time')
fg.map(sns.histplot, 'total_bill')

'''
this is a facet grid of histograms
showing the distribution of total bills
across different smoking statuses and time of day
(Lunch vs Dinner)
Top-left : Smokers during lunch
Top-right : Smokers during Dinner
Bottom- left : Non Smokers during lunch
Bottom right : Non smokers during Dinner
Smokers vs Non Smokers
Dinner(top-right vs Bottom-right):
Both Smokers and non-smokers show similar bill
Smokers have a slightly more spread-out
distribution , indicatng more variability

Lunch (Top-Left vs Bottom left):
Non smokers (bottom left) make up the majority
of lunch patrons.
Smokers(top-left) are much fewer at lunch,
with total bills mostly under $20
Lunch vs Dinner
Dinner is clearly more popular regardless
of smoking status
Total bills are generally higher and
more varied at dinner , especially for smokers

'''
##########################################################
 

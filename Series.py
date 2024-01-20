# -*- coding: utf-8 -*-
"""
Created on Tue May  9 17:15:37 2023

@author: Vaibhav Bhrkade

Series 
"""
# A series is used to model one dimenstion data
# Similar to list in python
# the series object have more few more bits
# including an index and a name

import pandas as pd
song2=pd.Series([145,343,64,3],name='counts')
song2

song2.index


"""
Created on Wed May 10 08:16:09 2023

@author:  Vaibhav Bhorkade

"""
import pandas as pd

song2=pd.Series([232,54,675,2],name="Counts")
song2


song2=pd.Series(['A','B','C','D'],name="Counts")
song2

song2.index

# index as string
song3=pd.Series([34,45,54,33],
index=['VAibhav','Sachin','Gaurav','Ketan'])
song3
song3.index

# NaN value
# This is stands for Not a number

# NaN change by mean
import numpy as np

song3.mean()

# duplicate index

george=pd.Series([23,43,5,3],name="Counts",index=[1934,1968,1968,1934])
print(george)

# Read pandas series

george[1968]

# We can iterate over data
for item in george:
    print(item)

# Update 
george['1968']=655
george

#Delete
george=pd.Series([23,43,5,3],name="Counts",index=[1934,1968,1968,1934])
print(george)

del george['1968']

print(george)

###########################################
#Convert datatype
# int uses .astype(int)
# note its is fail for NaN 
# datetime use pd.to_datetime

songs_66=pd.Series([3,None,11,9],name="Counts",
                   index=["george",'Ringo','John','Paul'])
pd.to_nuearic(songs_66.apply(str))
# There is erroer
pd.to_numeric(songs_66.apply(str),errors="coerce")

# DEaling with None
# filina 
songs_66.fillna(-1)

# Drop
songs_66.dropna()

# Append ,combining

songs_69=pd.Series([7,16,21,39],name="Counts",
                   index=["RAm",'Shyam','Ghanshyam','krishana']) 
songs=songs_66.append(songs_69)
songs

# Plotting of sseries into a graup
import matplotlib.pyplot as plt

fig=plt.figure()
songs_69.plot()
plt.legend()

#######################################
# Bar Graph
fig=plt.figure()
songs_69.plot(kind='bar')
songs_69.plot(kind='bar',color='k',alpha=.5)
plt.legend()

fig=plt.figure()
songs_69.plot(kind='bar')
songs_69.plot(kind='bar',color='b',alpha=.5)
plt.legend()

fig=plt.figure()
songs_69.plot(kind='bar')
songs_69.plot(kind='bar',color='red',alpha=.5)
plt.legend()

###########################################
# HIstogram
data=pd.Series(np.random.randn(500),name="500 random ")
fig=plt.figure()
ax=fig.add_subplot(111)
data.hist()
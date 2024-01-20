# -*- coding: utf-8 -*-

"""
Created on Wed May 31 08:25:07 2023

@author: Vaibhav Bhorkade

Numpy Assignment
"""
"Write a numpy program to get numpy version "

import numpy as np
np.__version__

np.show_config()

# Add function

np.info(np.add)

# transpose
# np.transpose

# test whether none of the element are zero giving True
x=np.array([1,2,3,4])

np.all(x)

# IF zero present giving False 
x=np.array([0,2,3,4])

np.all(x)

# Test any of element is non zero
x=np.array([0,0,23,0])
x
np.any(x)

# test for finite set
a=np.array([1,0,np.nan,np.inf])

np.isfinite(a)

# Check for complex number
a=np.array([1+2j,1+0j])
print(a)
print("Is number is complex : ")
np.iscomplex(a)
np.isreal(a)

np.isscalar(3.1)
np.isscalar([3.1])

a=[[11,12,12],[23,34,45],[23,34,54]]

# Show the dimenstion

A=np.array(a)
A

A.ndim

# Show shape
A.shape

# Row*Col
A.size

# Accesss rows and se
A[1,2]

A[1,2]

A[1,1]

A[0,0]

' OR '

A[0][0]

# 1st row and 1st and 2nd col

A[0][0:2]

A[:1,2]

# Basic operations 

x=np.array([[2,1],[2,4]])

y=np.array([[2,1],[2,4]])

# Add
Z=x+y
Z

# Sub
Z=x-y
Z

# Mul
Z=x*y
Z

"or "

Z=np.dot(x,y)
Z

# Calculate the sine of Z

np.sin(Z)

# Calucate transpose of matrix

c=np.array([[1,1],[2,2],[3,3]])
c

c.T

"""
Created on Thu Jun  1 08:14:33 2023

@author: Vaibhav Bhorkade

"""
# Multiplication of vector
# Dot product
import numpy as np

p=[[1,0],[0,1]]
q=[[1,2],[3,4]]
p
q
result=np.dot(p,q)
print(result)

# Outer  product
p=[[1,0],[0,1]]
q=[[1,2],[3,4]]
p
q
result=np.outer(p,q)
print(result)

# Cross product
p=[[1,0],[0,1]]
q=[[1,2],[3,4]]
p
q
result1=np.cross(p,q)
result1
result2=np.cross(q,p)
result2

# Determinant

import numpy as np

from numpy import linalg as LA

a=np.array([[1,0],[1,2]])
print(a)

print(np.linalg.det(a))

# Eigin Value and Eigin vector

import numpy as np
m=np.mat("3 -2;1 0")
print("Original Matrix: ",m)
w,v=np.linalg.eig(m)
print("Eigenvector of the said matrix",w)

print("Eigenvalue of the said matrix",v)

# Inverse of matrix

import numpy as np
m=np.array([[1,2],[3,4]])
m
result=np.linalg.inv(m)
print("Inverse of matrix",result)

# Normal Distrubustion
# Generate 5 numbers

x=np.random.normal(size=5)
print(x)

# Genetrate 6 random no bet

x=np.random.randint(low=10,high=30,size=6)
print(x)

# Random 3*3*3 array values

x=np.random.random((3,3,3))
x

# 5 * 5 array with max and min value

x=np.random.random((5,5))
x
xmin,xmax=x.min(),x.max()
print(xmin,xmax)
 
"""
Created on Fri Jun  2 08:18:38 2023

@author: Vaibhav Bhorkade

"""

# Get min and max value
import numpy as np
x=np.arange(4).reshape((2,2))
x
print("MAx value along second axis ")
print(np.amax(x,1))
print("Min value along second axis ")
print(np.amin(x,1))

# Write python program to draw line

import matplotlib.pyplot as plt
x=range(1,50)
y=[value * 3 for value in x]
print('Values of X')
print(*range(1,50))
y
plt.plot(x,y)

plt.title("Draw Line")
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.show()

# Write python program to draw a line 

import matplotlib.pyplot as plt

x=[1,2,3]
y=[2,4,1]

plt.plot(x,y)
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.title('Sample Graph')
plt.show()

# Write  a python program to draw line charts of finacial data
import matplotlib.pyplot as plt
import pandas as pd

df=pd.read_csv('C:/1-python/fdata.csv')
df.plot()
plt.show() 

# Write  a python program to draw line charts of Attendance data
import matplotlib.pyplot as plt
import pandas as pd

df=pd.read_csv('C:/1-python/Data_Science_Attendance_Sheet2.csv')
df
df.columns.plot(kind='bar')
df['Vaibhav Bhorkade'].plot(kind='bar')
plt.show() 


df=pd.read_csv('C:/1-python/Data_Science_Attendance_Sheet2.csv')
df

df2=df.drop('year',axis=1)
df2=df.drop('month',axis=1)
df2=df.drop('weekday',axis=1)
df2=df.drop('datum',axis=1)

df2=df2[:-1]
df2.plot()
plt.show()

# Write a python program to plot 2 or more line 
x1=[10,20,30]
y1=[20,40,10]
# line 2 points
x2=[10,20,30]
y2=[40,10,30]

plt.xlabel('x-axis')
plt.ylabel('y-axis')

plt.plot(x1)

"""
Created on Sat Jun  3 07:59:36 2023

@author: Vaibhav Bhorkade

"""

# Write python program to plot two or more lines with legends
import matplotlib.pyplot as plt
x1=[10,20,30]
y1=[20,40,10]
# line 2 points
x2=[10,20,30]
y2=[40,10,30]
# labeling to x and y axis
plt.xlabel('x-axis')
plt.ylabel('y-axis')

plt.title('Two or more lines with diffrence widths and color')
# Display
plt.plot(x1,y1, color='blue',linewidth=3,label='line-width3')
plt.plot(x2,y2, color='red',linewidth=5,label='line-width5')

plt.legend()

# Write Python program to plot in diffrent styles

import matplotlib.pyplot as plt
x1=[10,20,30]
y1=[20,40,10]
# line 2 points
x2=[10,20,30]
y2=[40,10,30]
# labeling to x and y axis
plt.xlabel('x-axis')
plt.ylabel('y-axis')

plt.title('Two or more lines with diffrence widths and color')
# Display
plt.plot(x1,y1, color='blue',linewidth=3,label='line1-dotted',linestyle='dotted')
plt.plot(x2,y2, color='red',linewidth=5,label='line2-dashed',linestyle='dashed')

plt.legend()

plt.show()

# Write python program to add line markers
# Line markers
import matplotlib.pyplot as plt
x=[1,4,5,6,7]
y=[2,6,3,6,3]

plt.plot(x,y, color='red',linestyle='dashdot',linewidth=3,marker='o',markerfacecolor='blue',markersize=12)

# set y limit of current axis
plt.ylim(1,8)
# set x limit of current axis
plt.xlim(1,8)

plt.xlabel('x-axis')

plt.ylabel('y-axis')

plt.title('Display marker')
plt.show()

# Write a Python program o plot seversl lines with diffrent format styles
import numpy as np
import matplotlib.pyplot as plt

# Sampled time at 200ms intervels
t=np.arange(0.,5.,0.2)

# green dashes , blue squeres and red triangles
plt.plot(t,t,'g--',t,t**2,'bs',t,t**3,'r^')

plt.show()


# Write python program to display a bar chart of the popularity of langauage

import matplotlib.pyplot as plt
x=['Java','Python','PHP','JavaScript','C#','C++']
popularity=[22.2,17.6,8.8,8,7.7,6.7]
x_pos= [i for i,_ in enumerate(x)]      
#_ is variable means it take one by one letter from the x with its corresponding index
plt.bar(x_pos,popularity,color='blue')
plt.xlabel("langauge")
plt.ylabel("popularity")
plt.title("Populartiy of the proramming langaure\n"+"worldwide ,oct 2017 compared to a year")
plt.xticks(x_pos,x)  

plt.show()

# Graph in horizontal and vertical you can use the yticks

# Write python program to display a bar chart of the popularity of langauage

import matplotlib.pyplot as plt
x=['Java','Python','PHP','JavaScript','C#','C++']
popularity=[22.2,17.6,8.8,8,7.7,6.7]
x_pos= [i for i,_ in enumerate(x)]      
plt.bar(x_pos,popularity,color='blue')
plt.xlabel("langauge")
plt.ylabel("popularity")
plt.title("Populartiy of the proramming langaure\n"+"worldwide ,oct 2017 compared to a year")
plt.yticks(x_pos,x)  
plt.show()

import matplotlib.pyplot as plt
x=['Java','Python','PHP','JavaScript','C#','C++']
popularity=[22.2,17.6,8.8,8,7.7,6.7]
x_pos= [i for i,_ in enumerate(x)]      #_ is variable means it take one by one letter from the x with its corresponding index
#enumerate is used to check or access the keys and values from the given list  
plt.barh(x_pos,popularity,color='green')
plt.xlabel("popularity")      #x label
plt.ylabel("language")    #y label
plt.title("Populartiy of the proramming langaure\n"+"worldwide ,oct 2017 compared to a year")
plt.yticks(x_pos,x)     #graph in horizontal and vertical yoou can use the yticks
plt.show()

# Write a python program to craete bar plot of scores by groups and gender
import numpy as np
import matplotlib.pyplot as plt

# data to plot
n_groups=5
men_means=(22,30,33,30,26)
women_means=(25,32,30,35,29)

# create plot
# ax for multiple subplots
fig, ax=plt.subplots()
index=np.arange(n_groups)
bar_width=0.35
opacity=0.8

rects1=plt.bar(index,men_means,bar_width,alpha=opacity,
                  color='g',label='Men')

rects2=plt.bar(index + bar_width ,women_means,bar_width,alpha=opacity,
                  color='r',label='Women')
plt.xlabel('Person')
plt.ylabel('Scores')
plt.title('Scores by Persons')
plt.xticks(index + bar_width,('G1','G2','G3','G4','G5'))
plt.legend()
plt.tight_layout()
plt.show()
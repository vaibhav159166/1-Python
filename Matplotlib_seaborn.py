# matplotlib ---- visualization of data (bar,histgraph,graphs)

import matplotlib.pyplot as plt

plt.plot([1,2,6,3])

plt.show()

# multiline plots
import matplotlib.pyplot as plt
x=range(1,5)
plt.plot(x,[xi*1.5 for xi in x])

plt.plot(x,[xi*3 for xi in x])

plt.plot(x,[xi/3.0 for xi in x])

# grid
import matplotlib.pyplot as plt
import numpy as np
x=np.arange(1,5 )
plt.plot(x, x*1.5,x,x*3.0,x,x/3)
plt.grid(True)
plt.show()

# Handling axes
import matplotlib.pyplot as plt
import numpy as np
x=np.arange(1,5)
plt.plot(x, x*1.5,x,x*3.0,x,x/3)

plt.axis()

plt.axis([0,5,-1,13])

plt.show()

# Add labels
# like x-axis , y-axis

import matplotlib.pyplot as plt
plt.plot([1,2,3,4])
plt.xlabel("THis is the x axis")
plt.ylabel("THis is the y axis")

plt.show()

# Adding title
import matplotlib.pyplot as plt
plt.plot([1,3,2,4])
plt.title("Simple plot ")
plt.show()

# Adding legend to graph
import matplotlib.pyplot as plt
import numpy as np
x=np.arange(1,5)
plt.plot(x, x*1.5,label="Normal")
plt.plot(x, x*3.5,label="Fast") # select all rows reg. 
plt.plot(x, x*2,label="slow")

plt.legend()

plt.show()

# Control colors
import matplotlib.pyplot as plt
import numpy as np
y=np.arange(1,3)
plt.plot(y,"y");
plt.plot(y+1,"m");

plt.plot(y+2,"c");

plt.show()

# Specifying style in multilines plot

plt.plot(y,'y',y+1,'m',y+2,'c');
plt.show()

# change the style

plt.plot(y,'--',y+1,'.:',y+2,':');
plt.show()

# markers
import matplotlib.pyplot as plt
import numpy as np
y=np.arange(1,3,0.2)
plt.plot(y,'x',y+1,'o',y+2,'D');
plt.show()

# Histogram charts
import matplotlib.pyplot as plt
import numpy as np
y=np.random.randn(100)
plt.hist(y);
plt.show()

# bar graph
plt.bar([1,2,3],[3,2,5]);
plt.show()

# first list -> coordinates of bar graph 
# second list -> height of bar graph

# bar graph
plt.bar([2,3,4],[3,4,5])
plt.show()


# Scatarplot
import matplotlib.pyplot as plt
import numpy as np

x=np.random.randn(1000)
y=np.random.randn(1000)
plt.scatter(x, y)
plt.show()

# colors 
size=50*np.random.randn(1000)
colors=np.random.rand(1000)
plt.scatter(x, y, s=size,c=colors)
plt.show()

# Adding text
# global minima / glabal maxima

X=np.linspace(-4, 4,1024)
Y=.25*(X+4)*(X+1)*(X-2)
plt.text(-0.5,-0.25,"Background minimum")
plt.plot(X,Y,c='k')
plt.show()

#______________________________________________________________
#############################################################
# pip install seaborn
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

sns.get_dataset_names()
df=sns.load_dataset('titanic')
df.head()

df=sns.load_dataset('mpg')


"""
Created on Sat May 13 08:20:55 2023

@author: Vaibhav Bhorkade

"""

import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

sns.get_dataset_names()
# dataset
df=sns.load_dataset('titanic')
df.head()

# data- dataframe 
sns.countplot(x="sex",data=df)

# color change using Set1,Set2,Set3
sns.countplot(x="sex",hue="survived",data=df,
palette='Set1')

sns.countplot(x="sex",hue="survived",data=df,
palette='Set2')

sns.countplot(x="sex",hue="survived",data=df,
palette='Set3')

# survived is use for split column
# use for countious data
sns.kdeplot(x='age',data=df,color='Red')

# Distribusion plot
sns.displot(x='age',kde=True,bins=5,data=df)
            
# Distribusion plot

sns.displot(x='age',kde=True,bins=5,data=df,color='Red')

# False - only bar comes 
# Distribusion plot
sns.displot(x='age',kde=False,bins=5,data=df)

# hue
sns.displot(x='age',kde=True,bins=5,hue=df['survived'],palette='Set1',data=df)

# Scatter plot
# iris dataset - flower
# flower dataset 
# sepal size

df=sns.load_dataset('iris')
df.head()

sns.scatterplot(x='sepal_length',y='petal_length',data=df,hue='species')

# Inference of the graph
# In above plot we can observe that an iris flower with a sepal length < 6 cm and
# len > 2cm is most likely setasa. 

# versicolor- 3<=sepal_len <6 and petal len <5

# Joint plot
sns.jointplot(x='sepal_length',y='petal_length',data=df,kind='reg')

sns.jointplot(x='sepal_length',y='petal_length',data=df,kind='hist')

sns.jointplot(x='sepal_length',y='petal_length',data=df,kind='kde')

# pairplot shows all df

sns.pairplot(df)

# corr- corelation
# heatmap
corr=df.corr()
sns.heatmap(corr)

# # #  # #  # #  # ## # # # # # # ## # # # ## # ## # # ## # ## ## # #

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
cars=pd.read_csv("C:/1-python/cars.csv")
cars.columns
cars.describe()

plt.hist(cars.speed)
# Almost are car traveling speed 40
sns.displot(x='speed',kde=True,data=cars)
# kde - kurnal density e
sns.displot(x='speed',kde=True,bins=6,data=cars)
# the dis covred 20 to 40 km are 17
sns.displot(x='dist',kde=True,data=cars)

# Box plotsns.boxplo
# Box plot indirectly taking about histogram

sns.boxplot(cars.speed)

sns.boxplot(cars.speed,color='red')

# distance
# There is one outlayer 
plt.hist(cars.dist)
sns.boxplot(cars.dist)
sns.boxplot(x='speed',data=df)
# kkeweness of speed

from scipy.stats import skew
from scipy.stats import kurtosis

# convert into list
speed=cars['speed'].tolist()
speed
print("Skewness of speed ",skew(speed))

sp_list=cars['speed'].tolist()
speed
print("Skewness of speed",skew(sp_list))

dist=cars['dist'].tolist

####################################################
# Assignment 

import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# Gives the name of dataset 
sns.get_dataset_names()

df=sns.load_dataset('iris')
df.head()

sns.countplot(x='sepal_length',data=df)

sns.countplot(x='sepal_length',data=df)

# bar
sns.countplot(x='sepal_length',data=df,color='black')

# kde
sns.kdeplot(x='sepal_length',data=df,color='red')

# statterplot
sns.scatterplot(x='sepal_length',y='petal_length',data=df,hue='species')

# In the plot above we can observe that an iris flower with a
# sepal length < 6cm 

# Joint plot 

sns.jointplot(x='sepal_length',y='petal_length',data=df,kind='reg')

# pair plot
# all colums data will shown

sns.pairplot(df)

# co-relation 
corr=df.corr()
sns.heatmap(corr)

# inferencev ---- 

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df=sns.load_dataset('iris')

 #df.head()
df.columns
df.describe()

plt.hist(df.sepal_length)
# Almost are car traveling speed 40
sns.displot(x='sepal_length',kde=True,data=df)
# kde - kurnal density e
sns.displot(x='sepal_length',kde=True,bins=6,data=cars)
# the dis covred 20 to 40 km are 17
sns.displot(x='sepal_width',kde=True,data=df)

# Box plot
# Box plot indirectly taking about histogram

sns.boxplot(df.sepal_length)

sns.boxplot(df.sepal_length,color='red')

# distance
# There is one outlayer 
plt.hist(df.sepal_width)
sns.boxplot(df.sepal_length)



# Joint plot 

sns.jointplot(x='sepal_length',y='petal_length',data=df,kind='reg')

# pair plot
# all colums data will shown

sns.pairplot(df)

# co-relation 
corr=df.corr()
sns.heatmap(corr)

sns.scatterplot(x='sepal_length',y='petal_length',data=df,hue='species')

df



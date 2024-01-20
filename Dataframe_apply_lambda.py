
#########------ Apply method on column 
import pandas as pd

data={
      "A":[1,2,3],
      "B":[4,5,6],
      "C":[7,8,9]
      }
df=pd.DataFrame(data)
print(df)

def add_3(x):
    return x+3
df2=df.apply(add_3)
df2

##########---------apply on single column 
import pandas as pd

data={
      "A":[1,2,3],
      "B":[4,5,6],
      "C":[7,8,9]
      }
df=pd.DataFrame(data)
print(df)

def add_5(x):
    return x+5
df['B']=df['B'].apply(add_5)
df['B']

# For two columns 0r multiple columns
def add_5(x):
    return x+5
df[['A','B']]=df[['A','B']].apply(add_5)
df

##############---------Apply lambda fun to each column 
df2=df.apply(lambda x:x+10)
df2

#######################################
# Apply lambda function to single column;'
df["A"]=df["A"].apply(lambda x:x-1)
df

# Instead apply one more fun transform
def add_2(x):
    return x+2
df2=df.transform(add_2)
df2

# map function
df["A"]=df["A"].map(lambda x:x/2)
df

#Using numpy function on single column

import numpy as np
df["A"]=df["A"].apply(np.square)
df

# Using square() method
df['B']=np.square(df['B'])
print(df)

#pandas groupby() with example
import pandas as pd 
techn=({
    "A":['a','b','c','a','b','c','d'],
    "B":[12,32,32,43,545,323,65],
    "C":['1','2','3','4','2','3','3'],
    "D":[12,32,32,43,545,323,65]})
df=pd.DataFrame(techn)
df
# use groupby
df3=df.groupby(['A']).sum()
df2
# multiple column
df2=df.groupby(['A','C']).sum()
df2

# Add index to the group data
df2=df.groupby(['A','C']).sum().reset_index()
df2

##########################################
technologies={
    'Courses':['spark','Pyspark','HAdoop','Python','PAndas'],
    'Fee':[2323,3445,6767,3423,5654],
    'DUration':['30days','50days','30days',None,'np.nan']
    }

###########################################
"""
Evening 
"""
import pandas as pd
technologies={
    'Courses':['spark','Pyspark','HAdoop','Python','PAndas'],
    'Fee':[2323,3445,6767,3423,5654],
    'DUration':['30days','50days','30days',None,'np.nan']
    }

df=pd.DataFrame(technologies)
df
df.columns
#Get the list of all columns names from header
column_header=list(df.columns.values)
print(column_header)

column_header=list(df.columns)
print(column_header)

column_header=list(df)
print(column_header)

####################################
#Suffling of rows 
# Pandas Shuffle DataFrame Rows
import pandas as pd
technologies={
    'Courses':['spark','Pyspark','HAdoop','Python','PAndas'],
    'Fee':[2323,3445,6767,3423,5654],
    'DUration':['30days','50days','30days',None,'np.nan']
    }

df=pd.DataFrame(technologies)

df1=df.sample(frac=1)
df1

# Create new index starting from zero
df1=df.sample(frac=1).reset_index()
df1

# Drop the shuffle index
df1=df.sample(frac=1).reset_index(drop=True)
df1

#######################################
import pandas as pd
technologies={
    'Courses':['spark','Pyspark','HAdoop','Python','PAndas'],
    'Fee':[2323,3445,6767,3423,5654],
    'DUration':['30days','50days','30days',None,'np.nan']
    }
index_label=['r1','r2','r3','r4','r5']
df1=pd.DataFrame(technologies,index=index_label)
df1

"""
Assisgnment
"""
import pandas as pd
df=pd.read_csv("Company_Data.csv")
df
#Quick Example of Get the no. pf rows in DataFrame
rows_count=len(df.index)
rows_count
rows_count=len(df.axes[0])
rows_count

col_count=len(df.axes[1])
col_count

# 
rows_count=df.shape[0]
rows_count

col_count=df.shape[1]
col_count

#########------ Apply method on column 

df=pd.read_csv("Company_Data.csv")
print(df)

import pandas as pd
##########---------apply on single column 


def add_5(x):
    return x+5
df['Sales']=df['Sales'].apply(add_5)
df['Sales']


# For two columns 0r multiple columns
def add_5(x):
    return x+5
df[['Income','Price']]=df[['Income','Price']].apply(add_5)
df

#######################################
# Apply lambda function to single column;'
df["Income"]=df["Income"].apply(lambda x:x-1)
df

# map function
df["Income"]=df["Income"].map(lambda x:x/2)
df

#Using numpy function on single column

import numpy as np
df["Income"]=df["Income"].apply(np.square)
df

# Using square() method
df['Price']=np.square(df['Price'])
print(df)

#pandas groupby() with example
# use groupby
df3=df.groupby(['Sales']).sum()
df2
# multiple column
df2=df.groupby(['Price','Income']).sum()
df2

# Add index to the group data
df2=df.groupby(['CompPrice','Advertising']).sum().reset_index()
df2

df.columns
#Get the list of all columns names from header
column_header=list(df.columns.values)
print(column_header)

column_header=list(df.columns)
print(column_header)

column_header=list(df)
print(column_header)

####################################
#Suffling of rows 
# Pandas Shuffle DataFrame Rows

df1=df.sample(frac=1)
df1

# Create new index starting from zero
df1=df.sample(frac=1).reset_index()
df1

# Drop the shuffle index
df1=df.sample(frac=1).reset_index(drop=True)
df1

"""
Created on Tue May  9 08:07:20 2023

@author: Vaibhav Bhorkade 
"""
# 50 % shuffle rows frac=0.5
df1=df.sample(frac=0.5)
df1
# 
#########################################
#---------- Joining --------------------
# inner join
# left join
# Right join
# Full outer join
 
import pandas as pd
technologies={
    'Courses':['spark','Pyspark','HAdoop','Python','PAndas'],
    'Fee':[2323,3445,6767,3423,5654],
    'DUration':['30days','50days','30days',None,'np.nan']
    }
index_label=['r1','r2','r3','r4','r5']
df1=pd.DataFrame(technologies,index=index_label)
df1

technologies2={
    'Courses':['spark','HAdoop','Python','sql'],
    'Discount':[23,34,67,34]
   
    }
index_label2=['r1','r6','r3','r5']
df2=pd.DataFrame(technologies2,index=index_label2)
df2

# pandas join by default it will join the table left join 
df3=df1.join(df2, lsuffix="_left",rsuffix="_right")
df3

# pandas inner join DataFrame
df3=df1.join(df2,lsuffix="_Left",rsuffix="_Right",how="inner")
df3

# # pandas Left join DataFrame
df3=df1.join(df2,lsuffix="_Left",rsuffix="_Right",how="left")
df3

# pandas Right join DataFrame
df3=df1.join(df2,lsuffix="_Left",rsuffix="_Right",how="right")
df3

# Pandas join on column
df3=df1.set_index('Courses').join(df2.set_index('Courses'),how="inner")
df3

#Pandas .merge() similar inner join
df3=pd.merge(df1, df2)
df3

df3=df1.merge(df2)
df3

#pandas .concat() to concat Two dataFrame # join vertically
import pandas as pd
technologies={
    'Courses':['spark','Pyspark','HAdoop','Python','PAndas'],
    'Fee':[2323,3445,6767,3423,5654],
    'DUration':['30days','50days','30days',None,'np.nan']
    }
index_label=['r1','r2','r3','r4','r5']
df=pd.DataFrame(technologies,index=index_label)
df

technologies2={
    'Courses':['spark','HAdoop','Python','sql'],
    'Discount':[23,34,67,34]
   
    }
df1=pd.DataFrame(technologies2)
df1

technologies3={
    'Courses':['Java','HAdoop','Python','sql'],
    'Discount':[232,343,647,334]
   
    }
df3=pd.DataFrame(technologies3)
df3
data=[df,df1]
df2=pd.concat(data)
df2

d=pd.concat([df,df1,df2])
print(d)

###########################################
# Write DataFrame to csv file with default param:
df3.to_csv("c:/1-python/course.csv")
df3

#Read csv file of DataFrame
df=pd.read_csv('course.csv')
df

#Write DataFrame to excel
df.to_excel("c:/1-python/Course.xlsx")
df
#read excel file
df=pd.read_excel("c:/1-python/Course.xlsx")
df



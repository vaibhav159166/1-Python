# -*- coding: utf-8 -*-
"""
Created on Fri Apr 28 09:16:48 2023

@author: VAIBHAV BHORKADE

Python For Data Science

"""

"""
For install pandas
# pip install pandas
For update
# conda install pandas==1.5.3
"""

# To check the version of pandas
import pandas as pd
pd.__version__

# Create pandas DataFrame from List in List 
# pd.DataFrame D and F shoud Capital
import pandas as pd
techno=[["Spark",200000,"30days"],["pandas",300000,"40 days"],]
df=pd.DataFrame(techno)

#  Give Column name and rows name
column_names=["Courses","Fee","Duration"]
row_label=["a","b"]

df=pd.DataFrame(techno,columns=column_names,index=row_label)
print(df)

######################################
# String data type = object data type both are interchangable

df.dtypes

######################################
# Custom data Type
types={'Courses':str,'Fee':float,'Duration':str}
df.dtypes

types={'Courses':int,'Fee':str,'Duration':str}
df.dtypes
#######################################
# Create DataFrame using Dict

tech={
      'Courses':['Spark','pandas','hadoop'],
      'Fee':[21234,43212,45643],
      'Duration':['30days','40days','50days'],
      'Discount':[1000,2000,3322]
      }
df =pd.DataFrame(tech)
df

################################
# rows label

tech={
      'Courses':['Spark','pandas','hadoop'],
      'Fee':[21234,43212,45643],
      'Duration':['30days','40days','50days'],
      'Discount':[1000,2000,3322]
      }
df =pd.DataFrame(tech)
df
row_label=["a","b","c"]

df=pd.DataFrame(tech,index=row_label)
print(df)
################################
# Convert DataFrame into to csv
df.to_csv('data_file.csv')

d=pd.read_csv("data_file.csv")
print(d)

# a=open('data_file.csv')
# a.read()

"""
Evening session 
02/05/23

"""

######################################
# convert DataFrame to csv
df.to_csv('c:/1-python/data_file.csv')

# create data Frame from csv file
d =pd.read_csv('c:/1-python/data_file.csv')
d

######################################
# Pandas DataFrame - Basic Operations
import pandas as pd
import numpy as np
technologies=({
    'courses':['AI','DS','ML','CS',None],
    'Fee':[200,2323,442,3432,''],
    'Duration':['15days','30days','45days','50days',''],
    'discount':[21,34,45,55,None]
    })
row_lable=['r0','r1','r2','r3','r5']
df=pd.DataFrame(technologies,index=row_lable)
print(df)
# row , column
df.shape

#size 
df.size

#columns names
df.columns

# column values
df.columns.values

# column rows as index
df.index

# data types
df.dtypes

#####################################
# Access single column
df['Fee']

# Accsessing 2 column or multiple column give double bracket
df[['Fee','Duration']]

# df2=df[row:column]
df2=df[6:] # 6 rows all column
df2

df3=df[:4] # all rows and 6 4 column
df3

df4=df[:1]
df4


df5=df[2:] # 2 and its onword means 2,3,4,5 upto
df5

##################################
# accessing cell 
df['Duration'][3]

# substracted from specific column
df['Fee'] = df['Fee'] - 500
df['Fee']

# exepory data analysis
df.describe()

###################################
df=pd.DataFrame(technologies, index=row_lable)

# Rename DataFrame column 
df.columns=['A','B','C','D']
df

df=pd.DataFrame(technologies, index=row_lable)
df

# asix is 1 but rows = 0
df.columns=['A','B','C','D']
df2 = df.rename({'A':"c1",'B':'c2'},axis=1)
df2

df2 = df.rename({'C':"c3",'D':'c4'},axis='columns')
df2

df2 = df.rename(columns={'A':"c1",'B':'c2'})
df2


"""
Created on Wed May  3 08:17:41 2023

@author: Vaibhav Bhorkade
Session : Morning Session   

"""

import pandas as pd
pd.__version__
import numpy as np
np.__version__

# pd is alias name of package

# DataFrame 
import pandas as pd
lang={
      'Courses':['Python','Java','c++','c','HTML','JS'],
      'Fee':[2000,2323,3433,4545,5656,4566],
      'Duration':[1,2,3,4,5,6],
      'Discount':['2','3','4','4','5','6']
      } 

df=pd.DataFrame(lang)
df
# Row labels
import pandas as pd
lang={
      'Courses':['Python','Java','c++','c','HTML','JS','css'],
      'Fee':[2000,2323,3433,4545,5656,4566,4534],
      'Discount':[1,2,3,4,5,6,7],
      'Duration':['2days','3days','4days','4days','5days','6days','7days']
      } 
row_label=['A1','A2','A3','A4','A5','A6','A7']
df=pd.DataFrame(lang, index=row_label)
df
print(df)

# dtypes
df.dtypes

# convert - direct data type convert-----0bj into string
df2=df.convert_dtypes()
print(df2.dtypes)

"""
output ----
print(df2.dtypes)
Courses     string
Fee          Int64
Discount     Int64
Duration    string
dtype: object
"""

# df convert all into object 
df=df.astype(str)
df.dtypes

#df.dtypes --- output
#Out[65]: 
#Courses     object
#Fee         object
#Discount    object
#Duration    object
#dtype: object

# Change one or multiple column Multiple
df2=df2.astype({'Fee':int,'Discount':float})
df2
df2.dtypes

# Convert data type for all columns in a list into float
df=pd.DataFrame(lang)
df.dtypes
cols=['Fee','Discount']
df[cols]=df[cols].astype('float')
df.dtypes

# convert data type for columns in a string
df=pd.DataFrame(lang)
df.dtypes
cols=['Courses','Duration']
df[cols]=df[cols].astype('string')
df.dtypes


"""
Created on Wed May  3 16:38:52 2023

@author: VAibhav Bhorkade
Evening session

"""
# Converting courses is string into a int it ignore error simply print object datatype
df = df.astype({"Courses":int},errors='ignore')
df.dtypes

# Errors Raise 
df = df.astype({"Courses":int},errors='raise')
df.dtypes

# Converts feed column to numaric type
# COnvert object into integer
df=df.astype(str)
df.dtypes
df["Discount"]=pd.to_numeric(df['Discount'])
df.dtypes

df["Fee"]=pd.to_numeric(df['Fee'])
df.dtypes

"""
output
df.dtypes
Out[16]: 
Courses     object
Fee         object
Discount     int64
Duration    object
dtype: object

df["Fee"]=pd.to_numeric(df['Fee'])

df.dtypes
Out[18]: 
Courses     object
Fee          int64
Discount     int64
Duration    object
dtype: object

"""
# Drop or delete rows by the help the label
df
df1=df.drop(['A1','A2'])
print(df1)

# Delete rows by position
df1=df.drop(df.index[[1,3]])  # 2 index 2 [[]] req

df1=df.drop(df.index[3])  # 2 index 2 [[]] req
df1

# Delete Rows by index range
df1=df.drop(df.index[2:])
df1

# When we have default indexes for rows
df=pd.DataFrame(lang)
df1=df.drop(0)
print(df1)

# When we have default indexes for rows
df=pd.DataFrame(lang)
df=df.drop(0)
print(df)

# 
df=pd.DataFrame(lang)
df1=df.drop([0,3]) # It will delete row0 and row3
df1=df.drop(range(0,2)) # It will delete 0 and 1 
df1

import pandas as pd
lang={
      'Courses':['x','y','z','p','q','r'],
      'Fee':[20,23,34,45,56,45],
      'Duration':[1,2,3,4,5,6],
      'Discount':['2days','3days','4days','4days','5days','6days']
      } 
df=pd.DataFrame(lang)
df

# Delete Colunmn 
df2=df.drop(['Fee'],axis=1)
df2

"""
Created on Wed May  3 19:42:53 2023

@author: Vaibhav 
Assignment
"""

import pandas as pd

df=pd.read_csv('C:/1-python/AutoInsurance.csv')

#shape
df.shape
#size
df.size
#column
df.columns 
#column values      
df.columns.values 
#index  
df.index 
#Data Types        
df.dtypes 

# 7 values that describe DataFrame
df.describe()

#Delete Rows by index range
df1=df.drop(df.index[5:]) #delete other than first 5 rows
df1

# Drop at particular index
df1=df1.drop(0)
df1

# Delete columns
df2=df1.drop(['Gender','Income','Location Code','Marital Status'],axis=1)
print(df2)

#Assigning Row label
row_label2=['r1','r2','r3','r4']
df=pd.DataFrame(df2, index=row_label2)
print(df)

# Accesing particular row and coloumn
df3=df[2:2]
print(df3)
"""
Created on Thu May  4 08:20:41 2023

@author: VAibhav Bhorkade
Morning
"""
# Explicitly using parameter name 'label'
df2=df.drop(labels=['Fee'],axis=1)
df2
# using column
df2=df.drop(columns=['Fee'],axis=1)
df2
# drop column using index 
print(df.drop(df.columns[1],axis=1))

# using implence
df.drop(df.columns[[1,2]],axis=1,inplace=True)
df

import pandas as pd
lang={
      'Courses':['x','y','z','p','q','r'],
      'Fee':[20,23,34,45,56,45],
      'Duration':[1,2,3,4,5,6],
      'Discount':['2days','3days','4days','4days','5days','6days']
      } 
df=pd.DataFrame(lang)
df
#Drop two or more column
df2=df.drop(["Courses",'Fee'],axis=1)
df2
#Drop 2 0r more by using index
df=pd.DataFrame(lang)

df2=df.drop(df.columns[[0,1]], axis=1)
df2

#########################################
#Drop column from list of list
df=pd.DataFrame(lang)
liscol=['Courses','Fee']
df2=df.drop(liscol,axis=1)
df2

# REmove columns inplace
df.drop(df.columns[0],axis=1,inplace=True)
print(df)

#index=iloc
#label=loc
lang={
      'Courses':['spark','py','hadook','python','pandas',None,'spark','java'],
      'Fee':[20,23,34,45,56,45,34,34],
      'Duration':[1,2,3,4,5,6,7,8],
      'Discount':['2days','3days','4days','1day','2day','4days','5days','6days']
      } 
row_label=['r0','r1','r2','r3','r4','r5','r6','r7']
df=pd.DataFrame(lang,index=row_label)
df

# df.iloc[startrow:endrow,startcol:endcol]
df2=df.iloc[:,0:2]
df2

# This is slicing operator to get DataFrame item by index
# The first silicing [:] for all rows return
# The second slice for column

df2=df.iloc[0:2, :]
print(df2)

# 0 to 1 rows [0:2] first slice
# for all column second slice [:]

df3=df.iloc[1:2,1:3]
print(df3)
# specific column 
df3=df.iloc[:,1:3]
df3

# select rows in index
df2=df.iloc[2]
df2
# multipal rows
df2=df.iloc[[2,3,6]]
df2
df2=df.iloc[1:5]
df2
df2=df.iloc[:1]
df2
df2=df.iloc[:3]

df2=df.iloc[-1:]
df2
df2=df.iloc[-3:]
df2

df2=df.iloc[::2]
df2

# ALTERNATE ROWS 
df2=df.iloc[::2]
df2

# LOC
#select row by index lable loc
df2=df.loc['r2']
df2

df2=df.loc[['r2','r3','r6']]
df2

df2=df.loc['r1':'r5']
df2

"""
Created on Thu May  4 16:39:34 2023

@author: Vaibhav Bhorkade

Evening Session
"""
# Alternatec rows 
df2=df.loc['r1':'r5':2]
df2
#####################################
#select column using Name 
df2=df['Courses']
df2
# Select multiple column
df2=df[["Courses","Fee","Duration"]]
df2
# USing LOC [] to take column slices
df2=df.loc[:,["Courses","Fee","Duration"]]
df2

# Select columns betn two column
df2=df.loc[:,'Fee':'Discount']
df2

# Select columns by range
df2=df.loc[:,'Duration':]
df2

# select column upto 'Duratrion'
df2=df.loc[:,:'Duration']
df2
# Select column upto
df2=df.loc[:,:'Duration']
df2
# Alternative column
df2=df.loc[:,::2]
print(df2)

#Pandas DataFrame .query example
#Query all rows with courses equal to spark
df2=df.query("Courses=='spark'")
df2

# not equal spark
df2=df.query("Courses!='spark'")
df2

df2=df.query("Courses!='spark' and Fee!=34")
df2

#Pandas add column to Dataframe
import numpy as np
import pandas as pd

"""
Assignment
"""
import pandas as pd

#dataframe from csv file
df=pd.read_csv('boston_data.csv')
df

# shape
df.shape
#size
df.size
#columns
df.columns

df.columns.values
#index
df.index
#dtypes
df.dtypes

#Accessing columns
df['crim']
##Accessing two columns
df[['crim','rad']]
#accessing certain cell from column 
df['rad'][3]
df['rad'][4]
#describe
df.describe()

# Drop rows by index
df1 = df.drop([1,2])
df1
# Delete Rows by position
df1=df.drop(df.index[3])
df1
df1=df.drop(df.index[[2,3]])
df1
# Delete Rows by Index Range
df1=df.drop(df.index[4:])
df1
#It will delete 0 ,1,2,3
df1 = df.drop(range(0,4))
df1

#Drop Column by name

df2=df.drop(["indus"], axis = 1)
print(df2)

# Explicitly using parameter name 'labels'
df2=df.drop(labels=["indus"], axis = 1)

#column
df2=df.drop(columns=["rad"], axis = 1)
df2

# Drop column by index.
print(df.drop(df.columns[1], axis = 1))


# using  -------------   inplace=True
df.drop(df.columns[[1]], axis = 1, inplace=True)
print(df)

#Drop Two or More Columns By label
df2=df.drop(["age", "tax"], axis = 1)
print(df2)


#Drop Two or More Columns by Index
df2=df.drop(df.columns[[0,1]], axis = 1)
print(df2)


#Drop Columns from List of Columns

lisCol = ["age","tax"]
df2=df.drop(lisCol, axis = 1)
print(df2)

#Remove columns From DataFrame inplace
df.drop(df.columns[1], axis = 1, inplace=True)
df

######--------df.iloc[startrow:endrow, startcolumn:endcolumn]

df2=df.iloc[:, 0:2]
df2

df2=df.iloc[0:2, :]
df2

#Slicing Rows and Columns 
df3=df.iloc[1:2, 1:3]
df3

#All rows 
df3=df.iloc[:, 1:3]
df3

# Select rows 
df2 = df.iloc[2]     
df2


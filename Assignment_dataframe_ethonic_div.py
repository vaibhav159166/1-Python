"""
Practice Assignment 

"""
# -*- coding: utf-8 -*-
"""
Created on Wed May 31 08:25:07 2023

@author: Vaibhav Bhorkade

"""

import pandas as pd

df=pd.read_csv("C:/1-python/ethnic diversity.csv")
df

df.dtypes

# Convert dtypes 
df=df.convert_dtypes()
df.dtypes

df.columns

df=df.rename(columns={'Employee_Name': 'emp', 'EmpID': 'id'},inplace=True)
df

# Apply as type
df=df.astype(str)

df = df.astype({"EmpID": float})
print(df.dtypes)

df = df.astype(str)
df.dtypes

cols=[ 'Employee_Name','Department']
df[cols] = df[cols].astype('string')
df.dtypes

#Ignores error
df = df.astype({"Department": int},errors='ignore')
df.dtypes

# Generates error
df = df.astype({"Department": int},errors='raise')

#DataFrame properties
df.shape

df.size

df.columns

df.columns.values

df.index

#Accessing one column contents
df['Department']

##Accessing two columns contents
df[['Department','Employee_Name']]

#select certain rows and assign it to another dataframe
df2=df[6:]
df2

# Accessing certain cell from column
df['Employee_Name'][4]



# Describe DataFrame for all numberic columns
df.describe()


#  Rename column 

df2 = df.rename({'Employee_Name': 'EN', 'EmpID': 'Eid'}, axis='columns')
df2
df2 = df.rename(columns={'Employee_Name': 'EN', 'EmpID': 'Eid'})

df=df.rename(columns={'Employee_Name': 'EN', 'EmpID': 'Eid'},inplace=True)
df

df=pd.read_csv("C:/1-python/ethnic diversity.csv")
df

# Drop DataFrame rows
df1=df.drop(df.index[1])

df1=df.drop(df.index[1])
df1

df1=df.drop(df.index[[1,3]])
df1

# Delete Rows by Index Range
df1=df.drop(df.index[23:])
df1

# Drop column by names
df1=df.drop(['Employee_Name'],axis=1)
df1

# Labels
df1=df.drop(labels=['Employee_Name'],axis=1)
df1

# columns
df1=df.drop(columns=['Employee_Name'],axis=1)
df1

# Drop Column by index
df.drop(df.columns[1],axis=1)
df

# Drop from Df 
# inplace used for main ope on df
df.drop(df.columns[[2]],axis=1,inplace=True)
df

# Drop two or more columns

lisCol = ["Employee_Name","EmpID"]
df2=df.drop(lisCol, axis = 1)
print(df2)

# Drop two or columns by index

df2=df.drop(df.columns[[0,1]],axis=1)

# Drop multiple column
lisCol = ["Employee_Name","EmpID"]
df2=df.drop(lisCol, axis = 1)
print(df2)

#Remove columns From DataFrame inplace
df.drop(df.columns[1], axis = 1, inplace=True)
df


df2=df.iloc[:, 0:2]
df2

df2=df.iloc[0:2, :]
df2

#The second slice [:] indicates that all columns are required.

#Slicing Specific Rows and Columns using iloc attribute
df3=df.iloc[1:2, 1:3]
df3
#Another example
df3=df.iloc[:, 1:3]
df3
#The second operator [1:3] yields columns 1 and 3 only.
# Select Rows by Integer Index
df2 = df.iloc[2]
df2


df2 = df.iloc[[2,3,6]]  
df2
df2 = df.iloc[1:5] 
df2
df2 = df.iloc[:1]
df2    
df2 = df.iloc[:3]    

df2 = df.iloc[-3:]
   
df2 = df.iloc[::2]   

# Select Rows by Index Labels
df2 = df.loc[1]   
df2     
df2 = df.loc[[2,3,6]]  
df2  

df2 = df.loc[1:5]    
df2

df2 = df.loc[1:5]
df2 = df.loc[1:5:2]   
df2
##########################################

#Select Rows by Index using Pandas iloc[]
#Select Row by Integer Index

print(df.iloc[2])

# Select Rows by Index List
print(df.iloc[[2,3,6]])


# Select Rows by Integer Index Range
print(df.iloc[1:5])

# Select First Row by Index
print(df.iloc[:1])


# Select First 3 Rows
print(df.iloc[:3])


# Select Last Row by Index
print(df.iloc[-1:])


print(df.iloc[-3:])


df=pd.read_csv("C:/1-python/ethnic diversity.csv")
df


df2=df["Employee_Name"]
df2

## select multiple columns
df2 = df[["Employee_Name","EmpID"]]
df2

# Using loc[] to take column slices
#loc[] syntax to slice columns
#df.loc[:,start:stop:step]
## Selecte multiple columns

df2 = df.loc[:,["Employee_Name","EmpID"]]
df2

# Select Random columns 

df2 = df.loc[:, ["Employee_Name","EmpID"]]
df2

# Select columns between two columns 
df2 = df.loc[:,"Employee_Name","EmpID"]
df2

## Select columns by range
df2 = df.loc[:,"Employee_Name":] 
df2

# Select columns by range 

df2 = df.loc[:,:'Employee_Name']  

## Select every alternate column
df2 = df.loc[:,::2]
df2       
   


############################

# not equals condition
df2=df.query("Employee_Name != 'Brown, Mia'" )
df2

##############################

#Pandas Add Column to DataFrame


#Pandas Add Column to DataFrame
# Add new column to the DataFrame
df2=df.drop(df.index[5:])
df2

Add = ['ABC road', 'BCD Chock', 'Ghansham road', 'Kopargaon', 'Ayodhya']
df2 = df2.assign(Address=Add)
print(df2)


############################

#Append Column to Existing Pandas DataFrame
# Add New column to the existing DataFrame

df2["Address"] = Add
print(df)


#############################

df.columns
print(df.columns)


print(df.columns)

#Quick Examples of Get the Number of Rows in DataFrame
rows_count = len(df.index)
rows_count
rows_count = len(df.axes[0])
rows_count

##################################

row_count = df.shape[0]  # Returns number of rows
col_count = df.shape[1]  # Returns number of columns
print(row_count)

##################################

#pandas Apply Function to a Column
# Below are quick examples
# Using Dataframe.apply() to apply function add column


# Using apply function single column
def add_4(x):
   return x+4
df["EmpID"] = df["EmpID"].apply(add_4)
df["EmpID"]




##############################

#Apply Lambda Function to Single Column
# Using Dataframe.apply() and lambda function


#Using Numpy function on single Column
# Using Dataframe.apply() & [] operator

import numpy as np
df['EmpID'] = df['EmpID'].apply(np.square)
print(df)



##############################
#Pandas Get Column Names from DataFrame
import pandas as pd
import numpy as np


df.columns
# Get the list of all column names from headers

column_headers = list(df.columns.values)
print("The Column Header :", column_headers)

#Using list(df) to get the column headers as a list
column_headers = list(df.columns)
column_headers

#Using list(df) to get the list of all Column Names
column_headers = list(df)
column_headers

############################

#Pandas Shuffle DataFrame Rows 

#Pandas Shuffle DataFrame Rows

# shuffle the DataFrame rows & return all rows

df1 = df.sample(frac = 1)
print(df1)

# Create a new Index starting from zero
df1 = df.sample(frac = 1).reset_index()
print(df1)

# Drop shuffle Index
df1 = df.sample(frac = 1).reset_index(drop=True)
print(df1)

#pandas inner join is mostly used join, 
#It is used to join two DataFrames on indexes. 
#When indexes don’t match the rows get dropped from both DataFrames.
##################################################

# pandas join ,by default it will join the table left join
df3=df1.join(df2, lsuffix="_left", rsuffix="_right")
print(df3)

# pandas Inner join DataFrames
df3=df1.join(df2, lsuffix="_left", rsuffix="_right", how='inner')
print(df3)

 #pandas Left join DataFrames
df3=df1.join(df2, lsuffix="_left", rsuffix="_right", how='left')
print(df3)
 #pandas Right join DataFrames
df3=df1.join(df2, lsuffix="_left", rsuffix="_right", how='right')
print(df3)



# Get by Column Index
col_list = df[df.columns[0]].values.tolist()
print(col_list)



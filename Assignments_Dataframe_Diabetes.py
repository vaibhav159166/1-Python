# -*- coding: utf-8 -*-
"""
Created on Wed May 31 08:25:07 2023

@author: Vaibhav Bhorkade

"""

import pandas as pd

df=pd.read_csv("C:/1-python/Diabetes.csv")
df

df.dtypes

# Convert dtypes 
df=df.convert_dtypes()
df.dtypes

df.columns

df=df.rename(columns={'Number of times pregnant': 'NOP', 'Age (years)': 'Age'},inplace=True)
df

# Apply as type
df=df.astype(str)

df = df.astype({" Number of times pregnant": float})
print(df.dtypes)

df = df.astype(str)
df.dtypes

cols=[ ' Diabetes pedigree function',' 2-Hour serum insulin']
df[cols] = df[cols].astype('string')
df.dtypes

#Ignores error
df = df.astype({" Diabetes pedigree function": int},errors='ignore')
df.dtypes

# Generates error
df = df.astype({" Diabetes pedigree function": int},errors='raise')

#DataFrame properties
df.shape

df.size

df.columns

df.columns.values

df.index

#Accessing one column contents
df[' Diabetes pedigree function']

##Accessing two columns contents
df[[' Diabetes pedigree function',' 2-Hour serum insulin']]

#select certain rows and assign it to another dataframe
df2=df[6:]
df2

# Accessing certain cell from column
df[' 2-Hour serum insulin'][4]



# Describe DataFrame for all numberic columns
df.describe()


#  Rename column 

df2 = df.rename({' Diabetes pedigree function': 'DPF', ' 2-Hour serum insulin': 'si'}, axis='columns')
df2
df2 = df.rename(columns={' Diabetes pedigree function': 'DPF', ' 2-Hour serum insulin': 'si'})

df=df.rename(columns={' Diabetes pedigree function': 'DPF', ' 2-Hour serum insulin': 'si'},inplace=True)
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
df1=df.drop([' Diabetes pedigree function'],axis=1)
df1

# Labels
df1=df.drop(labels=[' Diabetes pedigree function'],axis=1)
df1

# columns
df1=df.drop(columns=[' Diabetes pedigree function'],axis=1)
df1

# Drop Column by index
df.drop(df.columns[1],axis=1)
df

# Drop from Df 
# inplace used for main ope on df
df.drop(df.columns[[2]],axis=1,inplace=True)
df

# Drop two or more columns

lisCol = [" Diabetes pedigree function"," 2-Hour serum insulin"]
df2=df.drop(lisCol, axis = 1)
print(df2)

# Drop two or columns by index

df2=df.drop(df.columns[[0,1]],axis=1)

# Drop multiple column
lisCol = [" Diabetes pedigree function"," 2-Hour serum insulin"]
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


df2=df[" Diabetes pedigree function"]
df2

## select multiple columns
df2 = df[[" Diabetes pedigree function"," 2-Hour serum insulin"] ]
df2

# Using loc[] to take column slices
#loc[] syntax to slice columns
#df.loc[:,start:stop:step]
## Selecte multiple columns

df2 = df.loc[:,[" Diabetes pedigree function"," 2-Hour serum insulin"]]
df2

# Select Random columns 

df2 = df.loc[:, [" Diabetes pedigree function"," 2-Hour serum insulin"]]
df2

# Select columns between two columns 
df2 = df.loc[:," Diabetes pedigree function":" 2-Hour serum insulin"]
df2

## Select columns by range
df2 = df.loc[:," 2-Hour serum insulin":] 
df2

# Select columns by range 

df2 = df.loc[:,:' 2-Hour serum insulin']  

## Select every alternate column
df2 = df.loc[:,::2]
df2       
   


############################

# not equals condition
df2=df.query(" Diabetes pedigree function != '0.627'" )
df2

##############################

#Pandas Add Column to DataFrame


#Pandas Add Column to DataFrame
# Add new column to the DataFrame
df2=df.drop(df.index[5:])
df2

Emp = ['Ram', 'sham', 'Ghansham', 'Ganesh', 'Ramesh']
df2 = df2.assign(Emp=Emp)
print(df2)
############################

# Add multiple columns to the DataFrame
MNCCompanies = ['TATA','HCL','Infosys','Google','Amazon']
df2 = df2.assign(MNCComp = MNCCompanies,Emp=Emp )
df2

############################

#Append Column to Existing Pandas DataFrame
# Add New column to the existing DataFrame

df2["MNCCompanies"] = MNCCompanies
print(df)


#############################

# Add new column at the specific position

df2.insert(0,'Emp',Emp)
print(df)

######################

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
df[" Diabetes pedigree function"] = df[" Diabetes pedigree function"].apply(add_4)
df[" Diabetes pedigree function"]




##############################

#Apply Lambda Function to Single Column
# Using Dataframe.apply() and lambda function


#Using Numpy function on single Column
# Using Dataframe.apply() & [] operator

import numpy as np
df[' Diabetes pedigree function'] = df[' Diabetes pedigree function'].apply(np.square)
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


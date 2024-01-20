# -*- coding: utf-8 -*-
"""

@author: Vaibhav Bhorkade

"""

import pandas as pd

df=pd.read_csv("C:/1-python/emp_data.csv")
df

df.dtypes

# Convert dtypes 
df=df.convert_dtypes()
df.dtypes

df.columns

df=df.rename(columns={'Salary_hike,Churn_out_rate': 'emp'},inplace=True)
print(df)

# Apply as type
df=df.astype(str)

df = df.astype({"Salary_hike,Churn_out_rate": float})
print(df.dtypes)

df = df.astype(str)
df.dtypes

cols=[ 'Salary_hike,Churn_out_rate']
df[cols] = df[cols].astype('string')
df.dtypes

#Ignores error
df = df.astype({"Salary_hike,Churn_out_rate": int},errors='ignore')
df.dtypes

# Generates error
df = df.astype({"Salary_hike,Churn_out_rate": int},errors='raise')

#DataFrame properties
df.shape

df.size

df.columns

df.columns.values

df.index

#Accessing one column contents
df['Salary_hike,Churn_out_rate']

##Accessing two columns contents
df['Salary_hike,Churn_out_rate']

#select certain rows and assign it to another dataframe
df2=df[6:]
df2

# Accessing certain cell from column
df['Salary_hike,Churn_out_rate'][4]



# Describe DataFrame for all numberic columns
df.describe()


#  Rename column 

df2 = df.rename({'Salary_hike,Churn_out_rate': 'EN'}, axis='columns')
df2
df2 = df.rename(columns={'Salary_hike,Churn_out_rate': 'EN'})

df=df.rename(columns={'Salary_hike,Churn_out_rate': 'EN'},inplace=True)
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
df1=df.drop(['Salary_hike,Churn_out_rate'],axis=1)
df1

# Labels
df1=df.drop(labels=['Salary_hike,Churn_out_rate'],axis=1)
df1

# columns
df1=df.drop(columns=['Salary_hike,Churn_out_rate'],axis=1)
df1

# Drop Column by index
df.drop(df.columns[1],axis=1)
df

# Drop from Df 
# inplace used for main ope on df
df.drop(df.columns[[2]],axis=1,inplace=True)
df

# Drop two or more columns

lisCol = ["Salary_hike,Churn_out_rate"]
df2=df.drop(lisCol, axis = 1)
print(df2)

# Drop two or columns by index

df2=df.drop(df.columns[[0,1]],axis=1)

# Drop multiple column
lisCol = ['Salary_hike,Churn_out_rate']
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




df2=df["Salary_hike,Churn_out_rate"]
df2

## select multiple columns
df2 = df[["Salary_hike,Churn_out_rate"]]
df2

df2=df.drop(df.index[5:])
df2
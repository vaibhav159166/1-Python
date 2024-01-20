"""
Assignment
"""
import pandas as pd
import numpy as np
df=pd.read_csv("C:/1-python/bank_data.csv")
df
######################################
df.shape
#####################################
df.size
# Accessing one column contents
col = df['balance']
print(col)

# Accessing two columns contents
two_col = df[['duration', 'balance']]
print(two_col)

# accessing certain cell from column
df['housing'][2]

# Describe DataFrame
df.describe()

# rename() – Renames pandas DataFrame columns
df = df.rename(columns={'balance': 'Balance', 'loan': 'LOAN'})
df

# Rename Column 
df.columns = df.columns.str.replace('balance', 'salary')
df


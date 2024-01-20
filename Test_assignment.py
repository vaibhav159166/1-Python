# -*- coding: utf-8 -*-
"""
Created on Thu May 25 15:33:13 2023

@author: Vaibhav Bhorkade
Branch : Computer Engineering 

"""

import pandas as pd
data=pd.read_csv("C:/1-python/Data_Science_Attendance_Sheet2.csv")
data

data.columns

# 1.Rename the column name 
data.rename(columns={'Vaibhav Bhorkade':'Vaibhav_Bhorkade'},inplace=True)
data.columns
print(data)

data.rename(columns={'Krushna Lad':'Vaibhav_'},inplace=True)
data.columns
print(data)

# 2.Convert column into list
column= list(data['Vaibhav_Bhorkade'])
print(column)

# 3. for 0,1,2,3,4,5,7

column.count(0)

column.count(1)

column.count(2)

column.count(3)

column.count(4)

column.count(5)

column.count(7)

# 4. Bar Graph for attendance
import matplotlib.pyplot as plt
fig=plt.figure()
data['Vaibhav_Bhorkade'].plot(kind='bar')
plt.legend()


# 5.describe()
data['Vaibhav_Bhorkade'].describe()

# 6.Generate box plot using seaborn for your column and write the inference
import seaborn as sns
sns.boxplot(data['Vaibhav_Bhorkade'])

sns.boxplot(data.Vaibhav_Bhorkade,color='red')

# Q.7 Generate joint plot using seaborn for your column and write the inference
import seaborn as sns
sns.jointplot(column)
sns.jointplot()
  
# Q. 8 From complete dataframe, find out how many are regular students, how many are moderate and
#how many are poor in attendance.
data.rename(index={27: 'New_Row'}, inplace=True)

total_at = data.loc['New_Row']
total_at = total_at.drop(['year', 'month', 'weekday', 'datum'])

regular=0

moderate=0

poor=0

for i in total_at:
    if i>=80:
        regular+=1
    elif i<80 and i>=45:
        moderate+=1
    elif i<45:
        poor+=1

print("Total regular students are: ",regular)
print("Total moderate students are: ",moderate)
print("Total poor attendace students are: ",poor)

"""
MArksheet.csv
"""

import pandas as pd
mark=pd.read_csv("C:/1-python/Marksheet.csv")
mark
mark.columns

# 9. Out of functions, list and dictionary ,in which area you are strong and weak?
marks=mark.iloc[39]
marks['Function']
marks['List']
marks['Dictionary']

if marks['List'] > marks['Dictionary']:
    print('Strong in List and poor in dictionary')
elif marks['Function'] > marks['List']:
    print('Strong in Functions and Poor in List')
else:
    print('Strong in Dictionary and Poor in List ')
    
"""

max_values = df.max(axis=0)
max_values
max_column = df.idxmax(axis=1)

print("Columns with maximum values:")
print(max_column)

# Converting into series
import pandas as pd
so=pd.Series(df2,name='counts')
so

print("Column with the maximum value:", max_column)


df12=df2[['Function','List','Dictionary']].max()
df12

df12=df2[['Function','List','Dictionary']].min()
df12

df2.max()
df2
df2.column

print(df.max())
df2.max
"""

#Q.10 How many students have shown very good performance and how many have shown poor performance


good=0
poor=0
for i in mark['Total']:
    if i >= 5:
        good+=1
    elif i < 5:
        poor+=1
print("Students with good performance ",good)
print("Students with poor performance ",poor)


"""
AI_jobs_in_2024.docx
"""
# Read file
file = open("AI_jobs_in_2024.docx", "r")
with open("AI_jobs_in_2024.docx") as fp:





# Q.11 Open the given file in read mode
filepath='c:/1-python/AI_jobs_in_2024.txt'
with open (filepath) as file_object:
    context=file_object.read() 
print(context)

with open ('AI_jobs_in_2024.txt') as file_object:
    context=file_object.read()
print(context)

# Q.12 Remove the numbers from the text
import re

def remove_numbers(text):
    pattern=r'[^a-zA-z.,!?/:;\"\s]'
    return re.sub(pattern, '',text)

remove_numbers(context)


# Q.13 How many companies were surveyed ,extract using text processing


with open(filepath) as file_object:
    data = file_object.read()
    num=re.findall(r'\d+(?:\.\d+)?',data)
    print(num)
    num[0]

# Q.14 How many companies are willing to shift in AI domain,extract using text processing.
with open(filepath) as file_object:
    data = file_object.read()
    num=re.findall(r'\d+(?:\.\d+)?',data)
    print(num)  
    print("Percentage of companies:",num[-8])

# Q.15 How many millions jobs are expected to create in 2024 in field of AI
with open(filepath) as file_object:
    data = file_object.read()
    num=re.findall(r'\d+(?:\.\d+)?',data)
    print(num)
    num[-1]

# .16 Convert numbers into words
import inflect
p=inflect.engine()
def convert_number(text):
    temp_str=text.split()
    new_string=[]
    for word in temp_str:
        if word.isdigit():
            temp=p.number_to_words(word)
            new_string.append(temp)
        else:
            new_string.append(word)
    temp_str=' '.join(new_string)
    return temp_str


convert_number(context)


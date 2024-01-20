
"""
Created on Fri May  5 08:16:34 2023

@author: VAibhav Bhorkade

"""
import pandas as pd
lang={
      'Courses':['spark','py','hadook','python','pandas',None,'spark','java'],
      'Fee':[20,23,34,45,56,45,34,34],
      'Duration':[1,2,3,4,5,6,7,8],
      'Discount':['2days','3days','4days','1day','2day','4days','5days','6days']
      } 
row_label=['r0','r1','r2','r3','r4','r5','r6','r7']
df=pd.DataFrame(lang,index=row_label)
df

# pandas add column to DataFrame
tutors=['VAibhav','sachin','Ram','Shyam','GAurav','Ketan','pratham','Ketan']

df2=df.assign(TutorAssigned=tutors)
df2

df2=df.assign(TAs=tutors)
df2

# Add multiple column
MNCcomp=['TCS','Infosys','Google','Amozon','AMdocs','MIcrosoft','HCL','Cognizent']
df2=df.assign(MNCcomp = MNCcomp,TutorAssigned=tutors)
df2
df2.shape

# Derive new column from Existing column 
df=pd.DataFrame(lang,index=row_label)
df2=df.assign(Discount_per=lambda x:x.Fee * x.Duration / 100)
df2

# Add new column from Existing column 
df=pd.DataFrame(lang)
df["MNCcomp"]=MNCcomp
df

# Insert a column
df.insert(0, "Tutors", tutors) 
df
# df.insert(loc, column, value)

# Rename column 
print(df.columns)
df2=df.rename(columns={'Courses':'Courses_list'})
df2

# Multiple columns Axis
df2=df.rename({'Courses':'Courses_list'},axis=1)
df2

df2=df.rename({'Courses':'Courses_list'},axis='columns')
df2

df2=df.rename({'Courses':'Courses_list','Fee':'Total_Fee'},axis=1)
df2
# Implace
df.rename({'Courses':'Courses_list'},axis='columns',inplace=True)
df


"""
Created on Mon May  8 08:17:32 2023

@author: VAIBHAV BHORKADE
"""

import pandas as pd
lang={
      'Courses':['spark','py','hadook','python','pandas',None,'spark','java'],
      'Fee':[20,23,34,45,56,45,34,34],
      'Duration':[1,2,3,4,5,6,7,8],
      'Discount':['2days','3days','4days','1day','2day','4days','5days','6days']
      } 
row_label=['r0','r1','r2','r3','r4','r5','r6','r7']
df=pd.DataFrame(lang,index=row_label)
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
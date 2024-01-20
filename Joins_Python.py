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
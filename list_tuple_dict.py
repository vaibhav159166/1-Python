# -*- coding: utf-8 -*-
"""
Created 5 april 2023 
@author Vaibhav Bhorkade
List , Tuple , Set and Dictionary
"""

# Creating Tuple
tup=(1,2,3,5,6)
print(f"tup[0]  {tup[0]}")
print(f"tup[1]  {tup[1]}")
print(f"tup[4]  {tup[4]}")
print(f"tup[3]  {tup[3]}")

#tuple can hold different type of value 
tup2=(1,"hi",True)
print(tup2)
print(type(tup2))
# iteration in tuple 
for x in tup2:
    print(x)
tup3=("apple","orange","plum","apple")
for i in range(0,4):
    print(tup3[i])
    
tup4=("apple","orange","apple","apple")
tup4.count("apple")
len(tup4)
print(tup4.index("apple"))
print(tup4.index("orange"))
tup4=("apple","orange","apple","apple")
if 'apple' in tup4:
    print("Present")
if 'banana' in tup4:
    print("Not present")
tup5=(1,2,3,('vaibhav','gaurav'),5)
print(tup5)
print(tup5[3])

#List Operations
lst=['john','paul','george','ringo']
print(lst)
lst[1]
lst[-1]
lst[-2]
lst1=[1,2,3,4]
root_lst=['vaibhav',lst,lst1,3]
print(root_lst)

# append and extend
lst=['john','paul','george','ringo']
print(lst[1:])
print(lst[-3:-1])
lst.append('vaibhav')
print(lst)
lst.extend('gaurav')
print(lst)
lst=['john','paul','george','ringo']
#insert 
lst.insert(0,'shubham')
print(lst)


"""
 6/04/23
 Write a python program to find out is duplicate is present 
 or not
"""
lst=[1,2,3,4,5,6,7,2,9]
def duplicate(lst):
    for i in range(len(lst)-1):  #-1 because start with 0
        for j in range(1,len(lst)): # start 1 j for another travel
           if(lst[i]==lst[j]):
            return True
    return False
print(duplicate(lst))

a=[]
b=int(input("En  "))
a.append(b)
print(a)

st='abcd'
st[::-1]

# palimdrome python progrom
a=input("Enter the data : ")
def palimdrome(a):
    if a==a[::-1]:
        print("It is palimdrome string ")
    else:
        print("It is not palimdrome string ")
palimdrome(a)

# find minimum number in list
lst=[1,3,6,2,9,0]
a=lst[0]
for i in lst:
    if i<a:
        min=i
print(f"The minimum number in list is {min}")

# find maximum number in list

lst=[1,3,6,2,9,0]
a=lst[0]
for i in lst:
    if i>a:
        max=i
print(f"The maximum number in list is {max}")



"""
Created on Fri Apr  7 08:30:59 2023

@author: Vaibhav
"""

# Remove Method
a=['vaibhav','gaurav','ketan','sachin']
print(a)
a.remove('ketan')
a.pop(1)
print(a)    
# insert
a=['vaibhav','gaurav','ketan','sachin']
a.insert(1,'Shubham')
print(a)
#list concantation
l1=[1,2,3,4]
l2=[5,6,7,8]
l3=l1+l2
print(l3)

# creating set
basket={'banana','apple','orange','pear','apple'}
print(basket)

for item in basket:
    print(item)
# insert into set
basket.update(['hello','hi'])
print(basket)

basket.add("mango")
print(basket)
# min and max 
print(len(basket))
basket2={1,5,77,2,3}
print(max(basket2)) 
print(min(basket2)) 

# Remove method
print(basket.remove('apple'))  

print(basket)    

print(basket.discard('hello'))
print(basket)

#Set OPeration
s1={'apple','orange','banana'}
s2={'grape','lime','banana'}
print("union :",s1|s2)
print("Integratio :",s1&s2)
print("diiff :",s1-s2)
print("diiff :",s2-s1)

# dictonories
dic={
      'maharashtra':'Mumbai',
      'Gujrat':'Ahmadabad',
      'Up':'lakhnow'}
print(dic)
print('dict[Maharashtra]:',dic['maharashtra'])
dic.pop('Up')
print(dic)
# adding new element
dic['west']='kol'
print(dic)
# deleting new element
del dic['west']
print(dic)

# interartion
for states in dic:
    print(states,end=', ')

#values
print(dic.values())
print(dic.keys())
print(dic.items())


"""
Created on Mon Apr 10 08:20:02 2023

@author: Vaibhav Bhorkade
"""
 
     
dic={
          'maharashtra':'Mumbai',
          'Gujrat':'Ahmadabad',
          'Up':'lakhnow'
          } 
print(dic)
print('mumbai' in dic )
print('Up' in dic )

print(len(dic))   
# dictionary can have tuple value
seasons={'summer':('feb','march','april','may'),
         'rainy':('june','july','august','sept'),
         'winter':('oct','nov','dec','jan')}
print(seasons['rainy'])
print(seasons['rainy'][1])

seasons={'summer':['feb','march','april','may'],
         'rainy':['june','july','august','sept'],
         'winter':['oct','nov','dec','jan']}
print(seasons['rainy'])
print(seasons['rainy'][1])

dict2={
       'brand':'Maruti',
       'model':'breeza',
       'year':2022,
       'year':2021}
print(dict2)
for x in dict2:
    print(x)
for x in dict2:
    print(dict2[x])
    
#values accessed
for x in dict2.values():
    print(x)
    
for x in dict2.keys():
    print(x)

mydict=dict2.copy()
print(mydict)
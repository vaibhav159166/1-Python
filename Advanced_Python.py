# -*- coding: utf-8 -*-
"""
Created on Fri Apr 21 08:39:31 2023

@author: Vaibhav Bhorkade
Advanced Python
"""

import pandas as pd
f1=pd.read_csv('C:/1-python/buzzers.csv')

##############################
import os
with open('buzzers.csv') as raw_data :
    print(raw_data.read())

##--Reading csv data as lists--##
import csv
with open("buzzers.csv") as raw_data:
    for line in csv.reader(raw_data):
        print(line)

######################################
# in the form of dictionary
import csv
with open("buzzers.csv") as raw_data:
    for line in csv.DictReader(raw_data):
        print(line)
"""
evening 
"""
# key value split by , 
with open("buzzers.csv") as data:
    flights={}
    for line in data:
        k,v=line.split(',')
        flights[k]=v
flights

#####################################
# striping then spliting , your Raw Data 
with open("buzzers.csv") as data:
    ignore=data.readline()
    flights={}
    for line in data:
        k,v=line.strip().split(',')
        flights[k]=v
flights
#####################################
# pre-requisite to decorators
def plus_one(number):
    number1=number + 1
    return number1
plus_one(5)
#####################################
# Defining Function Inside other Function
def plus_one(number):
    
    def add_one(number):
        number1=number+1
        return number1
    
    result= add_one(number)
    return result
plus_one(100)
######################################
#   passing Function as argument
def plus_one(number):
    result1=number + 1
    return result1
def function_call(function):
        result=function(10)
        return result
    
function_call(plus_one)

# function Returing other functions
# manadatory return fun to variable
def hallo_function():
    def say_hi():
        return "Hi"
    return say_hi
hello=hallo_function()
hello()

"""
Created on Fri Apr 28 08:17:00 2023

@author: Vaibhav Bhorkade
"""
def add(a,b,c):
    sum=a+b+c
    return sum
add(1,2,3)
#   lambda Function 
add= lambda a,b,c:a+b+c
add(1,2,3)

# lambda Function
def mul(a,b,c):
    multi=a*b*c
    return multi
mul(2,3,4)

mul= lambda a,b,c:a*b*c
mul(2,3,4)

######## arbitatiry parameter
val=lambda *args:sum(args)
val(1,2,3,4,5,6,7,8,9,10)
val(1,2,3,4,5,6)

##------ *args ----###
def myfun(*args):
    for i in args:
        print(i)
myfun('hi','hello')
# lambda

myfun=lambda *args:args
myfun('hi','hello')

##
def person(name,*data):
    print(name)
    print(data)
    
## keyword argument **data     
def person(name,**data):
    print(name)
    print(data)
person(name='vaibhsv',age=21,place='mumbai')


###########################################
def person(name,**data):
    print(name)
    for i,j in data.items():
        print(i,j)
        
person(name='vaibhsv',age=21,place='mumbai')

###########################################

val= lambda **data:sum(data.values())
val(a=2,b=6,c=5,d=0)

###########################################

pers=lambda **data:[(j)for i,j in data.items()]
pers(name="gaurav",age=26,place='shree Ram')
##############################################

list1=[1,2,3,4]
sq=lambda list1:[i**2 for i in list1]
print(sq(list1))
list1

#############################################





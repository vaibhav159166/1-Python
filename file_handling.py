# -*- coding: utf-8 -*-

"""
File handling 
"""
with open ('handle.txt') as file_object:
    context=file_object.read()
print(context)


with open ('handle.txt') as file_object:
    context=file_object.read()
    #rstrip() remove gap or white space 
print(context.rstrip())

with open ('c:/1-python/handle.txt') as file_object:
    context=file_object.read()
    #rstrip() remove gap or white space 
print(context.rstrip())

filepath='c:/1-python/handle.txt'
with open (filepath) as file_object:
    context=file_object.read()
    #rstrip() remove gap or white space 
print(context.rstrip())

with open (filepath) as file_object:
    for line in file_object:
        print(line)

with open (filepath) as file_object:
    for line in file_object:
        print(line.rstrip())
        
with open (filepath) as file_object:
    lines=file_object.readlines()
for line in lines:
    print(line)

"""
evening session 12/4/23
Write a python code for Lottery random number
"""
from random import randrange
MIN_NUM=1
MAX_NUM=49
NUM_NUMS=6
ticket_nums=[]
for i in range(NUM_NUMS):
    rand=randrange(MIN_NUM,MAX_NUM+1)
    while rand in ticket_nums:
        rand=randrange(MIN_NUM,MAX_NUM+1)
    ticket_nums.append(rand)
ticket_nums.sort()
for n in ticket_nums:
    print(n,end=" ")

"""
remove outliers
#higher element deleted
"""
value=[89,105,7,4,12,23]
retval=sorted(value)
def removeOutliers(data,num_outliers):
    retval=sorted(data)
    for i in range (num_outliers):
        retval.pop(-1)
    return retval
removeOutliers(value, 2)
    
"""
Write python code that determine whether or not password 
good or not . We define good password if it follows following
conditions:
    1.at least 8 character
    2.atleast one upper case
    3.one lower case letter
"""
def checkPassword(password):
    has_upper=False
    has_lower=False
    has_num=False
    
    for i in password:
        if (i>='A' and i<='Z'):
            has_upper=True
        elif (i>='a' and i<='z'):
            has_lower=True
        elif (len(password)>=8):
            has_num=True
    
    if (has_upper==True and has_lower==True and has_num==True):
        print("Good Password")
    else:
        print("Bad Password ")
        
a=(input("Enter a password : "))
checkPassword(a)

"""
Created on Thu Apr 13 08:14:07 2023

@author: Vaibhav Bhorkade

"""
# file handling
# if we use absult path no need to change directory
a=open('handle.txt')
a.readlines()

filename='handle.txt'
with open(filename) as file_object:
    lines=file_object.readlines()
    pi_string=' '
    for line in lines:
        pi_string += " "+line.rstrip()
    print(pi_string)
    print(len(pi_string))
    
    
filename='handle.txt'
with open(filename,'w') as file_object:
    file_object.write("I am a programmer")
    file_object.write("\nHello")
   
    
    
a=open('handle.txt')
a.readlines()
# new line     
filename='han.txt'
with open(filename,'w') as file_object:
    file_object.write("I am a programmer")
    file_object.write("\nHello")

# create write new file
filename='programming.txt'
with open(filename,'w') as file_object:
    file_object.write("I am a programmer")
    file_object.write("\n I love Programming")


filename='programming.txt'
with open(filename,'a') as file_object:
    file_object.write("I am a Vaibhav")
    file_object.write("\n I am computer engineer")
a=open('handle.txt')
a.read()

# appending to a file
filename='programming.txt'
with open(filename,'a') as file_object:
    file_object.write("Hello p")
    file_object.write("\n Sanjivani")


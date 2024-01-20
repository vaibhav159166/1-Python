# -*- coding: utf-8 -*-
"""
List Comprehension

"""
# list
lst=[]
for num in range(0,20):
    lst.append(num)
print(lst)

# list comprehention
lst=[num for num in range (0,20)]
print(lst)

names=['dada','kaka','mama']
lst=[name.capitalize() for name in names]
print(lst)

names=['dada','kaka','mama']
lst=[name.upper() for name in names]
print(lst)
lst=[name.lower() for name in names]
print(lst)

# List comprehension with if statement
def is_even(num):
    return num%2==0
lst=[num for num in range (10) if is_even(num)]
print(lst)



"""
Created on Tue Apr 18 08:18:40 2023

@author: Vaibhav Bhorkade
"""
###########################
lst=[f"{x}{y}"
     for x in range(4)
     for y in range(4)
     ]
print(lst)
########--3 digit--########
lst=[f"{x}{y}{z}"
     for x in range(4)
     for y in range(4)
     for z in range(4)
     ]
print(lst)
print(len(lst))
####--SET Compression --####
set1={
      x
      for x in range(3)
      }
print(set1)
###########################
#Dictionary Comprehension
dict={
      x:x*x
      for x in range(3)
      }

print(dict)
####----Generator----#####
gen=(
    x
    for x in range(3)
    )
print(gen)

for num in gen:
    print(num)
#####---accesss using next---##
gen=(x for x in range(3))
next(gen)
next(gen)
next(gen)

gen=(
    x
    for x in range(3)
    )
next(gen)
#####----Function return multiple value---##
def range_even(end):
    for num in range(0,end,2):
        yield num
for num in range_even(6):
    print(num)
######---insted of  loop we can write---#####
gen=range_even(6)
next(gen)
next(gen)

#Chaining Generators
def lengths(itr):
    for ele in itr:
        yield len(ele)
def hide(itr):
    for ele in itr:
        yield ele*"*"
passwords=["Vaibhav","Hello"]

for password in hide(lengths(passwords)):
    print(password)

####----Printing list with index -----#####
lst=["milk","egg","bread"]
for index in range(len(lst)):
    print(f" {index+1} {lst[index]}")
    
"""
Assignment
password picker
"""
import string
#pick the adjective
adjective=['sleepy','slow','smelly','wet','fat','red','orange','yellow','green','blue','purple','fluffy','white','proud','brave']
#pick the nouns
nouns=['apple','dinisaur','ball','toaster','goat','dragon','hammer','duck','panda']
#pick the words
import random
adjective=random.choice(adjective)
noun=random.choice(nouns)
number=random.randrange(0,100)
#select special char
special_char=random.choice(string.punctuation)
#create the new secure password
password = adjective + noun + str(number) + special_char
print("Your password is : %s"%password)

# while loop to generate more password
print("Welcome to password picker ")
while True:
    adjective=random.choice(adjective)
    noun=random.choice(nouns)
    number=random.randrange(0,100)
    special_char=random.choice(string.punctuation)
    password = adjective + noun + str(number) + special_char
    print("Your password is : %s"%password)
    response=input("Would you like another password (Y or n) ")
    if  response=='n':
        break

"""
ASSIGNMENT 2
"""
print("Append in list : ")
adjective=[]
while True:
    a=input("Enter the adjective : ")
    adjective.append(a)
    print(adjective)
    response=input("Would you like another adjective (Y or n) ")
    if  response=='n':
        break
nouns=[]
while True:
    b=input("Enter the noun : ")
    nouns.append(b)
    print(nouns)
    response=input("Would you like another noun (Y or n) ")
    if  response=='n':
        break
import random
import string

print("Welcome to password picker ")
while True:
    adjective=random.choice(adjective)
    noun=random.choice(nouns)
    number=random.randrange(0,100)
    special_char=random.choice(string.punctuation)
    password = adjective + noun + str(number) + special_char
    print("Your password is : %s"%password)
    #checkPassword(password)
    response=input("Would you like another password (Y or n) ")
    if  response=='n':
        break
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
        
checkPassword(password)




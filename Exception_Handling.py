# -*- coding: utf-8 -*-

"""
Exception Handling
"""
try:
    print(5/0)
except ZeroDivisionError:
    print("You can not divide by zero")

try:
 print("GIve me two numbers , and i will divide them")
 print("Enter 'q' to quite")
 while True:
     first_number=input("Enter the first number : ")
     if first_number=='q':
         break;
     second_number=input("Enter second number : ")
     if second_number=='q':
         break
     answer=int(first_number)/ int(second_number)
     print(answer)
except ZeroDivisionError:
    print("You can not divide by zero")
    
filename='alice.txt'
try:
    with open(filename,encoding='utf-8') as f:
        contents=f.read()
except FileNotFoundError:
    print("Enter corrent file ")
    
     
    
"""
Created on Mon Apr 17 08:12:28 2023

@author: Vaibhav Bhorkade
Advanced Python
"""
# JSON - JavaScript Object NOtation  
import json
numbers=[2,3,4,5,7,11,13]
filename='numbers.json'
with open(filename, 'w') as f:
    json.dump(numbers ,f)

a=open('numbers.json')
a.read()

#Saving data json is useful
username=input("What is your name : ")
filename='username.json'
with open(filename,'w') as f:
    json.dump(username, f)
print(f"We'll remenber you mean when you back {username}")

import json
filename='username.json'
with open(filename) as f:
    username=json.load(f)
print(f"Welcome back , {username} !")

filename='username.json'
try:
    with open(filename) as f:
        username=json.load(f)
except FileNotFoundError:
    username=input("What is your name ?")
    with open(filename,'w') as f:
        json.dump(username,f)
        print(f"We will Remember you when you come back, {username}")
else:
    print(f"Welcome back ,{username}")



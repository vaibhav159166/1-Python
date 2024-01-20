# -*- coding: utf-8 -*-
"""
Created on Tue Apr  4 16:41:03 2023
Basic of Python

@author: Vaibhav Bhorkade
"""

print("Hello World")
x = 1
print(x)

print(type(x))
#converting to int



age1=input("Enter your age : ")
print(type(age1))
age2=input("Enter your age : ")
age=age1+age2
print(age)
age3=int(age)
print(age3)
print(type(age3))

a=int(input("Enter your age "))
a1=int(input("Enter your age "))
a2=a+a1
print(a2)
print(type(a2))

int_v=100
f=float(int_v)
print(f)
a='10'
f=float(a)
print(f)
b=int(a)
print(b)
print(type(b))

""" 
5 april 2023 
@author Vaibhav Bhorkade
Basic of Python
"""
#complex numbers
c1=1
c2=2j
print('c1:',c1,'c2 :',c2)
print(type(c1))
print(type(c2))
print(c1.real)
print(c2.imag)

#Boolean data type
all_ok=True
print(all_ok)
all_ok=False
print(all_ok)
print(type(all_ok))

#convert strings into bool
status=bool(input("Ok it is conform: "))
print(status)
print(type(status))

# Arithmetic Operation
home=10
away=15
print(home+away)
print(type(home+away))
print(10 * 4)
print(type(10*4))
#fractional part ignore
print(100/20)
print(type(100/20))
print(100//20)
print(type(100//20))
# Modulo operation %
print('Modulo operation 2%3 :',2%3)
print('Modulo operation 100%13 :',100%13)

#raise to
a=5
b=3
print(a ** b)
# assignment 
x=0
x+=1
#None Type
win=None
print(win is None)
print(win is not None)
print(type(win))

#indentation

nu=10
if nu < 0:
    print('Its negative')
else:
    print('Its not negative')

saving=float(input('Enter how much saving : '))
if saving == 0:
    print('sorry no saving')
elif saving < 500:
    print("Well done")

# iterating loop - while loop
count=0
print('starting')
while count <= 10:
    print(count)
    count+=1
# Range function
print("Print out values in a array ")
for i in range(10):
    print(i)
    print('done')

num=int(input("Enter a no check for: "))
for i in range(0,15):
    if i==num:
        break
    print(i)
    print('done')
#verticle ....    '_' is used as anonymous either i
for _ in range(0,10):
    print('.',end='')
    print()
 #horizonal .....   
for _ in range(0,10):
    print('.',end='')
    
"""
              ----Test case 1----
Write  python program to calculate BMI of a person using if elif else
5/4/23
"""
height=float(input("Please enter your height in m : "))
weight=float(input("Please enter your weight in kg : "))
BMI=round((weight/(height * height)),2)
if BMI<18.5:
    print(f"You are under weight and your BMI is {BMI}")
elif BMI>18.5 and BMI<25:
    print(f"You are normal weight and your BMI is {BMI}")
elif BMI>30 and BMI<35:
    print(f"You are obese and your BMI is {BMI}")
elif BMI>35:
    print(f"You are clinically obuse and your BMI is {BMI}")
    

"""
          ----Test case 2----
  write python code using logical operators and if elif . so as to allow 
  for roller coster also ask user age and charge ticket accordingly
  5/04/23
"""
print("Welcome to roller coster ")
height=int(input("Enter your height in cm : "))
if height>=120:
    print("You are eligible for roller coster ")
    age=int(input("Enter your age : "))
    bill=0
    if age<12:
        print("Childs ticket is $5")
        bill=5
    elif age>12 and age<18:
        print("Youths ticket is 7$")
        bill=7
    elif age>=18 and age<45:
        print("Youngs ticket is 12 $")
        bill=12
    elif age>=45 and age<55:
        print("Adults ticket is 50 $")
        bill=50
    want_photo=input("Do you want photo y/n : ")
    if want_photo=='Y':
        bill+=3
        print("Total bill is ", bill)
    else:
        print(bill)

"""
created on Thu 6/04/23
@Vaibhav Bhorkade
"""
# break loop statement
print("Only print codeif all iterations complete ")
num=int(input("Enter a number check for : "))
for i in range(0,6):
    if i==num:
        break
    print(i,' ',end='')
print("Done")

print("Only print codeif all iterations complete ")
num=int(input("Enter a number check for : "))
for i in range(0,6):
    if i==num:
        break
    print(i,' ',end='')
    print("Done")
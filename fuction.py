
# function
def prime_num(num):
    for i in range(2,num):
        if(num%i==0):
            return 'It is not prime number'
            break
    return 'It is prime number'
print(prime_num(21))

#display simplay greeting
def greet(username):
    print(f"hello , {username}")
greet('Sanjivani')
# argument and parameter
def describe(animal_type,pet_name):
    print(f"I have a {animal_type}")
    print(f"My {animal_type} name is {pet_name}")
describe('dog','moti')
describe('cat','chiv')
# default value argument
def describe(animal_type,pet_name='moti'):
    print(f"I have a {animal_type}")
    print(f"My {animal_type} name is {pet_name}")
describe(animal_type='cat')

def describe(animal_type='dog',pet_name='moti'):
    print(f"I have a {animal_type}")
    print(f"My {animal_type} name is {pet_name}")
describe()

# anagram program
def are_anagram(str1,str2):
    a=list(str1.replace(""," ").lower())
    b=list(str2.replace(""," ").lower())
    
    if(len(a)!=len(b)):
        return False
    else:
        return(sorted(a)==sorted(b))
    
print(are_anagram("elbow","below"))
print(are_anagram("race","care"))

# sum of list which divisible 5 and 7
lst=[5,7]
lst1=[1,2,5,7,14,55,45,21,49,8,9]

def return_sum(lst):
    sum=0
    for i in range (len(lst)):
        if(lst[i]%5==0 or lst[i]%7==0):
            sum=sum+lst[i]
    return sum
print(return_sum(lst))
print(return_sum(lst1))


#write a function to reverse the sentence
def reverse_word(input):
    if input=="":
        return "You entered wrong input"
    else:
        words=input.split()
        reverse_sen="  ".join(reversed(words))
    return reverse_sen
print(reverse_word("This is india"))
print(reverse_word("I am vaibhav"))


"""
Created on Tue Apr 11 08:15:51 2023

@author: Vaibhav Bhorkade
"""
def get_formated(first_name,last_name):
    full_name=f"{first_name} {last_name}"
    return full_name
cricketer=get_formated('Rohit','sharma')
print(cricketer)

# dictionary function even return
def build_person(first_name,last_name):
    person={'first':first_name,'last':last_name}
    return person
musician=build_person('Ram', 'Sarkar')
print(musician) 

# list to function
def greet_user(names):
    for name in names:
        msg=f"Hello {name}"
        print(msg)
usernames= ['Vaibhav' , 'Saurabh' ,'Surabhi']
greet_user(usernames)

# list to function
def greet_user(names):
    for name in names:
        msg=f"Hello {name.title()}"
        print(msg)
usernames= ['Vaibhav' , 'Saurabh' ,'Surabhi']
greet_user(usernames)

# * for multiple parameter
def make_pizza(*toppings):
    print('making pizza of following toppings')
    for topping in toppings:
        print(f"- {topping}")
    #print(toppings)
make_pizza('pepperoni')
make_pizza('mushrooms','green','cheese')


def make_pizza(size,*toppings):
    print(f'making a {size} pizza of following toppings')
    for topping in toppings:
        print(f"- {topping}")
    #print(toppings)
make_pizza(16,'pepperoni')
make_pizza(12,'mushrooms','green','cheese')


import pizza as p
p.make_pizz(12,'mushrooms','green','cheese')

from pizza import make_pizz
make_pizz(10,'mushrooms','green','cheese')


"""
Assignment
Write a code for leaf year
"""
def leaf_year(year):
    if (((year>0) and (year%4==0)) or ((year%100==0)) and (year%400==0)):
        return True
    return False

print(leaf_year(1601))
print(leaf_year(2016))
print(leaf_year(2000))
# using else condition
def leaf_year(year):
    if ((year>0) and (year%4==0)):
        return True
    elif((year%100==0) and (year%400==0)):
     return True
    else:
        return False
print(leaf_year(2016))
print(leaf_year(2000))
print(leaf_year(1601))

"""
Assignment
Generate and display password containing 7 and 10 chracters
"""
from random import randint
SHORTEST=7
LONGEST=10
MIN_ASCII=33
MAX_ASCII=126
print(SHORTEST)

# constant in capital to declare
# camelNameing randomPassword
def randomPassword():
    randomLength=randint(SHORTEST, LONGEST)
    result=" "
    for i in range(randomLength):
        randomChar=chr(randint(MIN_ASCII,MAX_ASCII))
        #the char fun takes ASCII code as its parameter ,It returns a string containing the
        #character with that ASCII code as its result
        result=result+randomChar
    return result
print("Your random password is :",randomPassword())
print("Your random password is :",randomPassword())

#Write Python code to for fibbonacy series

def fibbonac(n):
    lst=[0,]
    previous=0
    current=1
    lst.append(current)
    for i in range(n-1):
        previous,current=current,previous+current
        lst.append(current)
    return lst
print(fibbonac(10))
  
# import pizza 
from pizza import make_pizz as mp
mp.make_pizz(16,'pepperoni')

"""
Created on Wed Apr 12 08:22:15 2023

@author: Vaibhav Bhorkade
"""

from pizza import make_pizza as mp
mp(16,'pepperoni')

import pizza as p
p.make_pizza(16,'pepperoni')

from pizza import *
make_pizza(12, 'potato')
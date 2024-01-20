"""
Created on Fri Jun  9 21:00:55 2023

@author: Vaibhav Bhorkade

"""

'''Decorator:-is the advanced part of the function
calculator():-we make it once and use at the sevaral time
#pre-requisite to understand the decorator
'''
#pre-requisite
def plus_one(num):
    num1=num+1
    return num1
plus_one(5)
#########################
#defining the function inside other function
def plus_one(num):
    def add_one(num):
        
        num1=num+1
        return num1
    result=add_one(num)
    return result

plus_one(5)
################################
#passing the function as argument to other function
def plus_one(num):
    num1=num+1
    return num1

def function_call(function):
    result=function(5)
    return result

function_call(plus_one)
###################################
#favorite question of the interviweer
#funtion returning the other function
def hello_function():
    def say_hii():
        return 'hii'
    return say_hii
hello_function()
#Out[10]: <function _main_.hello_function.<locals>.say_hii()>


def hello_function():
    def say_hii():
        return 'hii'
    return say_hii
hello=hello_function()
hello()
#always remeber when you call hello_function()
#directly then it will display object not hi
#therefore  you nee to assign it to hello first
#then call hello() function
####################
#python decorator is a function
#that takes in a function and
#returns it by adding the some functionality
def say_hi():
    return 'Hello There'
def uppercase_decorator(function):
    def wrapper():
        func=function()
        make_uppercase=func.upper()
        return make_uppercase
    return wrapper
decorator = uppercase_decorator(say_hi)
decorator()                                 #Out[15]: 'HELLO THERE'
#however ,python provides a much esaier way
#for us to apply decorator
#we simply use the @ symbol before
#the function we'd like the decorator

#########################
#we are the define the function upper 
#and we can easly use the that function inside the 
#other function by easly @ symbol
@uppercase_decorator
def say_hi():
    return 'hello there'
say_hi()

#################################
#applying the multiple decorator
#to the a single function
#we can use the multiple decorators
#to a single function .however
#the decorators will be applied in the order
#that we've called them
def split_string(function):
    def wrapper():
        func = function()
        splitted_string=func.split()
        return splitted_string
    return wrapper
@split_string
@uppercase_decorator
def say_hi():
    return 'hello there'
say_hi()        #Out[22]: ['HELLO', 'THERE']
#it can splite the string first and then make it as the upper case letter
###################################
#case study of the decorator
numbers=[2,6,7,8]
def cal_square(numbers):
    result=[]
    for i in numbers:
        result.append(i*i)
    return result
def cal_cube(numbers):
    result=[]
    for i in numbers:
        result.append(i*i*i)
    return result
print(cal_square(numbers))
print(cal_cube(numbers))

#######################################
#time required for the squareing and calculating the number square and cube
import time
def cal_cube(numbers):
    start=time.time()
    result=[]
    
    for i in numbers:
        result.append(i*i*i)
    
    end=time.time()                     # this end is not in the for loop so it has the differnt meaning
    print((end-start)*1000)
    print('took'+str((end-start)*1000)+'mil sec')
    return result

array=range(1,100000)
out_square=cal_square(array)
out_cube=cal_cube(array)


###################################################3
import time
def time_it(func):
    def wrapper(args,*kwargs):
        start=time.time()
        result=func(args,*kwargs)
        end=time.time()
        print(func._name_+'took'+str((end-start)*1000)+'mil sec')
        return result
    return wrapper
@time_it
def calc_cube(numbers):
    result=[]
    
    for number in numbers:
        result.append(number*number*number)
    
    return result
@time_it
def calc_square(numbers):
    result=[]
    
    for number in numbers:
        result.append(number*number)
    
    return result

array=range(1,100000)
out_square=cal_square(array)
out_cube=cal_cube(array)

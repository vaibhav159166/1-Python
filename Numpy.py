#######----      Numpy   -------###########

import numpy as np

#declaration of array 
arr1=np.array([12,234,34])
arr2=np.array([2,44,56])

arr1
arr1.dtype

# create multi dimensional array

arr =np.array([[10,23,43],[23,34,56]])
arr

# ndmin - multidimension array

arr=np.array([12,23,34,54],ndmin=2)
arr

# ndmin - multidimension array

arr=np.array([12,23,34,54],ndmin=3)
arr

# Change the dattype of arry

arr=np.array([12,323,43],dtype=complex)
arr

# Get the dimension of arry
arr=np.array([[1,2,3,4],[5,5,67,8],[4,5,7,8],[8,9,7,6]])
print(arr)

print(arr.ndim)

#find the size of each item in array
arr=np.array([12,23,34])
print("Each item contain in bytes : ",arr.itemsize)

# Data type array of  each item in array
arr=np.array([12,23,34])
print("Each item contain in bytes : ",arr.dtype)

# Get the shape and size of array
arr=np.array([[1,2,3,4],[5,5,67,8]])
print("Shape of array",arr.shape)

arr=np.array([[1,2,3,4],[5,5,67,8]])
print("Shape of array",arr.size)

# Create array from dtype
arr=np.array([[1,2,3,4],[5,5,67,8]],dtype=float)
arr

# craete squence of integer  using arange()
# in step of 3
arr=np.arange(0,20,3)
print("A sequential array with step /3 ",arr)
arr

# Access the array element
arr=np.arange(11)
print(arr)

print(arr[2])

# -ve indexing
print(arr[-2])

# Multi dimenstional array indexing
arr=np.array([[1,2,3,4],[5,5,67,8]])
arr.shape

arr[1,1]

arr[0,3]

arr[0,0]

arr[0,-1]

# Access elements using silicing
arr=np.array([0,1,2,3,4,5,6,7,8,9]) 
x=arr[1:8:2]
print(x)

arr[-2:3:-1]
b=arr[-2:3:-1]
print(b)

x=arr[-2:10]
print(x)

# indexing in numpy

arr=np.array([[10,20,23,23],[34,45,56,76],[23,34,54,65],[45,65,67,78]]) 

#multi_arr[1,2]- Access row 1 and column 2
#multi_arr[1,:]- Access row 1 and all columns

# all rows , 3 columns ,::2 used for one after one

x=arr[:3,::2] 
print(x)

# Integer arrayb indexing

arr=np.arange(35).reshape(5, 7)
arr

"""
Created on Thu May 11 08:24:42 2023

@author: Vaibhav Bhorkade

"""

import numpy as np

arr=np.arange(12).reshape(3, 4)
arr
# Boolean array indexing
rows=np.array([True,False,True])
rows
wanted_rows=arr[rows,: ]
print(wanted_rows)

# Convert the one dimension array into list

array=np.array([10,23,34,45])
print("Array ",array)

print(type(array))

# Convert the list
list1=array.tolist()
print("List ",list1)
print(type(list1))

# Convert multi dime array to list

array=np.array([[12,23,34,45],[34,45,65,76],[11,22,33,44],[11,22,99,77]])
array

lst=array.tolist()
print("List ",lst)

# Convert List to array 
#--np.array()

lst=[23,34,55,66]

array=np.array(lst)
print("Array " ,array)

# asarray()

lst=[23,34,54,56]
array=np.asarray(lst)
array
print(type(array))

# Numpy array Properties
#           No paraenthesis for properties 

# shape
array=np.array([[12,3,34,45],[12,434,45,56]])
print(array.shape) 

# Resize the arary
array=np.array([[12,3,3],[12,434,45]])
array.shape=(3,2)
print(array)

# reshape() function
array=np.array([[23,34,54],[45,34,22]])
array.shape
new_array= array.reshape(3,2)
new_array.shape

# Usage of ndim
array=np.array([[12,23,34,45],[34,4,3,2],[23,455,65,76]])
array
print(array.ndim)

# Apply Arithmatic opeartion'

arr1=np.arange(16).reshape(4,4)
arr1
arr2=np.array([1,2,3,4])
arr2

# add()
add_arr=np.add(arr1,arr2)
print(f"Afding two arrays :\n {add_arr}")

# Substract

sub_arr=np.subtract(arr1,arr2)
sub_arr

# multiplication 

mul_arry=np.multiply(arr1,arr2)
print(f"Multipling two arrays :\n {mul_arry}")

# Divide

div_arr=np.divide(arr1,arr2)
print(f"Divide two arrays :\n {div_arr}")

# To perform Reciprocal operations

array=np.array([34,54,65,6,7,8])
rep_array=np.reciprocal(array)
rep_array

array=np.array([[23,34,54],[45,34,22]])
rep_array=np.reciprocal(array)
rep_array

# To perform power operations
arr1=np.array([2,3,10])
pow_arr1=np.power(arr1,3)
print(f"Power afrer applaying {pow_arr1}")

# Appling power operation

arr2=np.array([3,2,1])
print("My second arrray : ",arr2)
pow_arr2=np.power(arr1,arr2)
print(f"After applying power fun to arry : {pow_arr2}")

###################################
arr1=np.array([2,3,10])
arr2=np.array([3,2,1])

pow_arr1=np.power(arr1,3)
pow_arr2=np.power(arr1,arr2)

print(f"After applying power fun to arry : {pow_arr2}")

# To perform mod function

import numpy as np

arr1=np.array([2,3,4,5])
arr2=np.array([3,4,5,4]) 
arr1
arr1.dtype
# mod()

mod_arr=np.mod(arr1,arr2)
mod_arr

# # # # # # # # # # # # # # # # # # # # # # # 

# create an empty array

from numpy import array

l=[1.0,2.0,3.0]
a=array(l)

# Crreate numpy array empty
from numpy import empty
a=empty([3,3])
print(a)

# Craete Zero array

from numpy import zeros
a=zeros([3,3])
print(a)

# Craete one arry

from numpy import ones
a=ones([3,3])
print(a)

# Craete Vstack

from numpy import array
from numpy import vstack

# first array'
a1=array([1,2,3])
a2=array([4,5,6])

# vertical array
a3=vstack((a1,a2))
a3
a3.shape

# hstack
from numpy import array
from numpy import hstack

# first array'
a1=array([1,2,3])
a2=array([4,5,6])

# Horizontal array
a3=hstack((a1,a2))
a3
a3.shape

# Two dimensitional array

from numpy import array
data=[[12,12],[23,32],[43,34]]
data
data=array(data)
print(data)

type(data)

# Indexbound array out of bound error '
from numpy import array
data=array([12,12,45,656,6])
data

data[-1]
data[-5]

# 2 D indexing 
from numpy import array
data=array([[12,12],[23,32],[43,34]])
data
print(data[0,])

#  
"""
Created on Fri May 12 08:17:31 2023

@author: VAibhav Bhorkade

"""
from numpy import array

# Split input and output data 
data=array([[11,22,33],
            [44,55,66],
            [77,88,99]])

X,y=data[:,:-1],data[:,-1]
X
y

# broadcast scalar to 1D array

a=array([1,2,3])
print(a)

# define scalar
b=2
b

#braodcast
c=a+b
print(c)

# Vector addition
from numpy import array

a=array([1,2,3])
print(a)

b=array([1,2,3])
print(b)

# add vectors

c=a+b
print(c)

# Vector subsrtaction 
from numpy import array

a=array([1,2,3])
print(a)

b=array([0.5,0.5,0.5])
print(b)

# add vectors

c=a-b
print(c)

# Vector L1 norm

from numpy import array
from numpy.linalg import norm
# define vector
a=array([1,2,3])
print(a)
# calculate norm
l1=norm(a,1)
l1

# Vector L2 norm

from numpy import array
from numpy.linalg import norm

a=array([1,2,3])
print(a)

# calculate norm
l2=norm(a)
l2

##  Triangular matrix

from numpy import array
from numpy import tril
from numpy import triu

# define square matrix
M=array([[12,21,23],
         [32,43,45],
         [67,88,66]])

print(M)
# Lower triangular matrix
lower=tril(M)
print(lower)

# Uppper triangular matrix
upper=triu(M)
print(upper)

# Diagonal Matrix

from numpy import array
from numpy import diag

M=array([[12,21,23],
         [32,43,45],
         [67,88,66]])

print(M)

# extract diagonal vector
d=diag(M)
d
# craete diagonal vector
D=diag(d)
D

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 

# Identity matrix
from numpy import identity
I = identity(3)
print(I)

# Orthogonal matrix - inverse of that matrix or transvrse of matrix
from numpy.linalg import inv
Q=array([[1,0],
        [0,-1]])
Q
# inverse
V=inv(Q)
print(Q.T)
print(V)

# identity equivalance
I=Q.dot(Q.T)
print(I)

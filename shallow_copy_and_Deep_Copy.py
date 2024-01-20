"""
Created on Sat Jun 10 08:08:24 2023

@author: Vaibhav Bhorkade

"""

'''
shallow copy and Deep Copy

assignment statements(obj_b=obj_a) not real

'''
# Assignment operation
# This will only create a new variable with the same reference.
list_a=[1,2,3,4,5]
list_b=list_a

list_a[0]=-10
print(list_a)
print(list_b)

# Shallow copy
# One level deep . Modifying on level 1 does not affect other list
# Use copy.copy() or object specific copy functions/copy constructors
import copy
list_a=[1,2,3,4,5]
list_b=copy.copy(list_a)

# not affects the other list
list_a[0]=-10
print(list_a)
print(list_b)

# Applicable with single level list

# But with nested objects , modifying on level 2 or deeper does not affect the other
import copy
list_a=[[1,2,3,4,5],[6,7,8,9,10]]
list_b=copy.copy(list_a)

# Affect the other
list_a[0][0]=-10
print(list_a)
print(list_b)

# Deep copies
# Full independent clones . Use copy.deepcopy()
import copy
list_a=[[1,2,3,4,5],[6,7,8,9,10]]
list_b=copy.deepcopy(list_a)

# Affect the other
list_a[0][0]=-10
print(list_a)
print(list_b)


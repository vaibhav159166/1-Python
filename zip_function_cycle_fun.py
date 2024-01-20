# -*- coding: utf-8 -*-
"""
Created on Wed Apr 19 08:26:08 2023

@author: Vaibhav Bhorkade
"""
lst=["milk","egg","bread"]
for index in range(len(lst)):
    print(f" {index+1} {lst[index]}")
##---- same code using enumerate ---=
for index, item in enumerate(lst,start=1):
    print(f"{index} {item}")
##---- zip function ---
name=['dada','mama','kaka']
info=[9870,5040,3456]
for nm,inf in zip (name,info):
    print(nm,inf)
## ---- drawback of zip --- mismatch item not display

name=['dada','mama','kaka','baba']
info=[9870,5040,3456]
for nm,inf in zip (name,info):
    print(nm,inf)
# zip_longest 
from itertools import zip_longest
name=['dada','mama','kaka','baba']
info=[9870,5040,3456]
for nm,inf in zip_longest (name,info):
    print(nm,inf)
# use fill value
from itertools import zip_longest
name=['dada','mama','kaka','baba']
info=[9870,5040,3456]
for nm,inf in zip_longest(name,info,fillvalue=0):
    print(nm,inf)

# use all function

#count():- use in deep learniing
from itertools import count
counter=count()
print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))

#let us start from the 1 instead of 0
from itertools import count
counter=count(start=1)
print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))
###################################
#cycle()
#suppose you have repeated tasks to be done in a constant time  then we use cycle() iterator
import itertools
instructions=("eat","code","sleep")
for instruction in itertools.cycle(instructions):
    print(instruction)
#we can get the output in the infinite loop
################################

#repeat()
from itertools import repeat
for msg in repeat("keep patienece",times=3):
    print(msg)
#########################################
#group()
from itertools import combinations
player={'john','jain','sumit'}
for group in combinations(player,2):
    print(group)
#group are the variable not the special key word
from itertools import combinations
player={'john','jain','sumit'}
for x in combinations(player,2):
    print(x)
#################################

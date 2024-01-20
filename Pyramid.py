"""
Pyramid
"""

'''
# Rectangle Pyramid of 4X4

* * * * 
* * * * 
* * * * 
* * * * 

'''
for i in range(4):
    for j in range(4):
        print("*",end=' ')
    print()
    
'''
Triangle 
* * * * 
* * * 
* * 
* 

'''   
for i in range(4):
    for j in range(4-i):
        print("*",end=' ')
    print()

'''
* 
* * 
* * * 
* * * * 
'''
for i in range(4):
    for j in range(i+1):
        print("*",end=' ')
    print()


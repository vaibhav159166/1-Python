# -*- coding: utf-8 -*-
"""
Created on Fri Apr 21 08:13:40 2023

@author: Vaibhav 
"""
users=['admin','employee','manager','worker','staff']
password=['Admin@123','Employee@123','Manager@123',
          'Worker@123','Staff@123']
pass_hash_code=[]
count=0

import hashlib
for i in password:
    a=hashlib.sha512(i.encode('utf-8')).hexdigest()
    pass_hash_code.append(a)

def password_checker(): 
    global count
    n=input("\n Enter Password : ")
    n1=hashlib.sha512(n.encode('utf-8')).hexdigest()

    for n1 in pass_hash_code:
        index=password.index(n)
        user2=users[index]
        
        if user2=='admin':
            print("Hello admin , would you like to see a status report ")
        elif (user2=='employee'):
            print("Hello Employee")
        elif (user2=='manager'):
            print("Hello Manager")
        elif (user2=='worker'):
            print("Hello Worker")
        
        else:
           print("\n Access Denied")
           count = count + 1
           print(count)
        
            
while(count<3):
    password_checker()
else:
    print("\n You loose your chances ")
    print("\n Try Later ")

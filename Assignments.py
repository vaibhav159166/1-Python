#use the admine user 
users=["admine","employee","manager","worker","staff"]
for user in users:
    if user=="admin":
        print("hello admin ,would you like to see the status report")
    elif user=="employee":
        print("hello employe")
    elif user=="manager":
        print("hello manager")
    elif user=="worker":
        print("hello worker")
    else:
        print("hello staff")

##  check the new user and old user
current_user=["ali","ahemd","fahad","aun","rana"]
new_users=["ali","rana","bilai","huzi","dula"]
for new_user in new_users:
    if new_user in current_user:
        print("person will need to enter  a new uersname")
    else:
        print("saying that the username is avilable")



# user 
users=['admin','employee','manager','worker','staff']
for user in users:
    if user=="admin":
        print("Hello admin , would you like see status report ")
    elif user=="employee":
        print("Hello employee")
    elif user=="manager":
        print("Hello manager")
    elif user=="worker":
        print("Hello worker")
    else:
        print("Hello")
    
#####################################
current_users=['Ram','shyam','vaibhav']
new_users=['gaurav','Ram','ketan']
for new_user in new_users:
    if new_user in current_users:
        print("Person will need to enter new username ")
    else:
        print("Welcome ")
import hashlib
hashlib.sha256("Vaibhav@15916".encode('utf-8')).hexdigest()
'afc4703fe925d6e2251460a668ee20bf447b62e96b43c4d1483eb2a149b84590'
len(hashlib.sha256("Vaibhav@15916".encode('utf-8')).digest())






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
        print("It is a Good Password")
    else:
        print("It is a Bad Password ")


import json
import hashlib
from itertools import count

counter = count(start=1)

while True:
    choice = int(input("1) Login\n2) Sign up\n3) Exit\nEnter choice: "))
    
    if choice == 1:
        # Get username and password from user
        username = input("Enter Username: ")
        password = input("Enter Password: ")
    
        # Hash password
        hash_pass = hashlib.sha256(password.encode("utf-8")).hexdigest()
    
        try:
            # Load existing usernames and passwords from file
            with open('usersnpass.json', 'r') as f:
                user_dict = json.load(f)
        except json.JSONDecodeError:
            user_dict = {}
    
        # Check if username exists and password matches
        if username in user_dict and user_dict[username] == hash_pass:
            print("Login successful!")
            counter = count(start=1)
        else:
            # Increment the counter
            attempts = next(counter)
            if attempts >= 4:
                print("Too many attempts. Try again later.")
                break
            else:
                print("Invalid username or password.")
                
    elif choice == 2:
        # Get username and password from user
        username = input("Enter Username: ")
        password = input("Enter Password: ")
        if checkPassword(password):
        
            # Hash password
            hash_pass = hashlib.sha256(password.encode("utf-8")).hexdigest()
        
            try:
                # Load existing usernames and passwords from file
                with open('usersnpass.json', 'r') as f:
                    user_dict = json.load(f)
            except json.JSONDecodeError:
                user_dict = {}
        
            # Check if username already exists
            if username in user_dict:
                print("Username already exists. Please choose a different username.")
            else:
                # Add new username and hashed password to dictionary
                user_dict[username] = hash_pass
                with open('usersnpass.json', 'w') as f:
                    json.dump(user_dict, f)
                print("Signup successful!")
    
    elif choice == 3:
        break
    else:
        print("Invalid choice.")
        


# -*- coding: utf-8 -*-
"""
Created on Tue May 16 08:15:09 2023

@author: Vaibhav Bhorkade

NLP - Natural LAngauge Processing
-concerned with giving computers the ability
 to understand text and spoken words in much the
 same way human beings can.
 
 eg. Application - ChatGpt,Alexa,Bot,Whatsapp

Data Science 1)-NLP
             2)-Visulazation
             3)-Reinforcement
"""

# Tokenization 
txt="Welcome to the new year 2023"
x=txt.split()
print(x)

# install re
# pip install re
# Removing Special charachter
# ^ not or except all
# \ back slash - give :  r' 

import re

def remove_special_charachter(text):
    pat=r'[^a-zA-z0-9.,!?/:;\"\s]'
    return re.sub(pat, '',text)

remove_special_charachter("007 hi @ hello & I am $ Vaibhav#")

# Remove the Numbers
import re

def remove_numbers(text):
    pattern=r'[^a-zA-z.,!?/:;\"\s]'
    return re.sub(pattern, '',text)

remove_numbers("007 hi @ hello & I am $ Vaibhav#")

# Remove Particular part
txt="Welcome: to the , new year; 2023!"
import re
x=re.split(r'(?:,|;\s)\s*',txt)
print(x)

# Function to remove puncation
import string
def remove_punctuation(text):
    text=''.join([c for c in text if c not in string.punctuation])
    return text
remove_punctuation('Article : @First sentence of some , {importance} article ')

#  # #  # # # # # #  #  # # # #   # # # # # # #  # # #

# r - to count the the back slash
# ^ - except
# a-z : all letters bet a to z
# A-Z : all letters bet A to Z
# 0- 9 :all digit bet 0 to 9
# whitespace -\s

###############################################

# Stemming
# remove watched - ed removed
# remove going - ing removed
# remove s/es and ed
#PorterStemmer() -  

import nltk
def get_stem(text):
    stemmer=nltk.porter.PorterStemmer()
    text=' '.join([stemmer.stem(word) for word in text.split()])
    return text
get_stem("we are Going and eating ; watched")

# split

line='asdf fjdk; afed,fjek,asdf,foo'

re.split(r'(?:,|;|\s)\s',line)

# Pattern
txt="Welcome: to the , new year; 2023!"
pattern=r'(?:,|;|\s)\s*'
x=re.split(pattern,txt)
print(x)

# matching text at the start or end of string

filename='spam.txt'
filename.endswith('.txt')

# # # # # # # # # # # # # # # # # # # #
area_name='6 th lane west Andheri'
area_name.endswith('west Andheri')

## ## ##  ##  ##  ##  ##  ##  ##  ##  ##  #  # #
choices=('http:','ftp')
url='http://www.python.org'
url.startswith(choices)

# Slicing a string
S='ABCDEFGHIJKLMNOP'
print(S[2:7])   

print(S[5:7])  
print(S[5:-2])
print(S[-7:-2])
print(S[2:7:2])
print(S[6:1:-2])

# Slice at Begining
#omitting the start index starts the slice from 
# Meaning S[:stop]

print(S[:4])  

# 6 to all
print(S[6:])

# Reversse of string

print(S[::-1])

# Slice
filename='spam.txt'
filename[-4:]==".txt"

#
url='http://www.python.org'
url[:5]=='http' or url[:6]=='https:' or url[:4]=='http'


"""
Created on Wed May 17 08:10:25 2023

@author: Vaibhav Bhorkade

"""

# pipe operation = cocendination operator

# Matching names
from fnmatch import fnmatch,fnmatchcase
names=['Dat1.csv','Dat2.csv','config.ini','foo.ini','foo.csv']
[name for name in names if fnmatch(name,'Dat*.csv')]

# Matching names
from fnmatch import fnmatch,fnmatchcase
names=['Andheri East','Parle East','Dadar west']
[name for name in names if fnmatch(name,'*East')]

# address ending st

address=['5412 N CLARK ST','1056 W AADISON ST',
         '1039 W GRANVILLE AVE','2122 N CLACK ST',
         '4802 N BROADWAY']
[addre for addre in address if fnmatch(addre,'*ST')]

# check exact match
text='yeah,but no,but yeah,but no,but yeah'
# Exact match
text=='yeah'

import string
# Match at startor end
text.startswith('yeah')
text.endswith('no')

text.find('yeah')

# Search for the location of the first occurance
text.find('no')
text.find('No')
text.find('hello')
text

# Number date match
text1='11/27/2023'
text2='Nov 27,2023'

import re
# Simple matching : \d+ means match one or more digit
if re.match(r'\d+/\d+/\d+', text1):
    print('Yes')
else:
    print('No')
    
if re.match(r'\d+/\d+/\d+', text2):
    print('Yes')
else:
    print('No')

# date anather

dat='05-03-2023'
if re.match(r'\d{2}-\d{2}-\d{4}', dat):
    print('Yes')
else:
    print('No')

###################################################
# Practice

dxt="This is artificial inteligence era"
dxt.split()


print(dxt)

text="India: has greate , history; in 2023 india is leading to its florious future !"

# Split()/Seprate by all 
import re
x=re.split(r'(?:,|;|:\s)\s*',text)
print(x)

# Seprate by comma
import re
x=re.split(r'(?:,|,|,\s)\s*',text)
print(x)

# Check string 
import string
txt="Rama went to haridar to get Gangajal"
# Check text Gangajal
txt.endswith('jal')

from fnmatch import fnmatch,fnmatchcase
choices=('Apple','Mango')
[choice for choice in choices if fnmatch(choices,'*go')]


txt="I Like ",choices[1:]
print(txt)

# Extract date 
txt="I had visited pune on ''11-01-2023'"
if re.match(r'\d{2}-\d{2}-\d{4}', txt):
    print(txt)
else:
    print('No')
    
if re.match(r'\d+/\d+/\d+', txt):
    a=text1
    print(a)
    

x=re.split(r'(?:,|on|:\s)\s*',txt)
print(x)


# Searching and replacing

text='yeah,but no,but yeah,but no,but yeah'
text.replace('yeah', 'ya')

# Two date
txt="Today is 17/05/2003 and our exam start on 03/07/2023"
import re
re.sub(r'(\d+)/(\d+)/(\d+)',r'\3-\1-\2',txt)

# Compile method

datepat=re.compile(r'(\d+)/(\d+)/(\d+)')
datepat.sub(r'\3-\1-\2',txt)

txt="Today is 17/05/2003 and our exam start on 03/07/2023 to a 31/2/1920"
newtext,n=datepat.subn(r'\3-\1-\2',txt)
newtext
n

# Searching and replacing case sensitive text
text='Upper PYTHON,Lower PYTHON,Mixed PYTHON'
re.findall('PYTHON',text,flags=re.IGNORECASE)
re.sub('PYTHON','JAVA',text,flags=re.IGNORECASE)

"""
Created on Tue May 23 08:54:34 2023

@author: Vaibhav Bhorkade

"""
# Matched text , If you need to fix this, you might have to use a suitable 

import re
import string
import nltk
text='UPPER PYTHON, lower python ,Mixed Python'
def matchcase(word):
    def replace(m):
        text=m.group()
        if text.isupper():
            return word.upper()
        elif text.islower():
            return word.lower()
        elif text[0].isupper():
            return word.capitalize()
        else :
            return word
    return replace
re.sub('python',matchcase('snake'),text,flags=re.IGNORECASE)

# extraxct from comment
str_pat=re.compile(r'\"(.*)\"')
text1='computer says "no."'
str_pat.findall(text1)
#['no.']
text2='computer says "no." phone says "yes."' 
str_pat.findall(text2)              

# In above ex there is drawback so we diff pattern
str_pat=re.compile(r'\"(.*?)\"')
text1='computer says "no."'
str_pat.findall(text2)

# 
comment=re.compile(r'/\*(.*?)\*/')
text1='/*This is a comment */'
comment.findall(text1)

# multiline comment not match is pattrn
text2='''/* This is comment*/'''
comment.findall(text2)

# To fix problem 
comment=re.compile(r'/\*(())')

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

# Removing no. from the text
import re
def remove_numbers(text):
    result=re.sub(r'\d+','',text)
    return result
input_str='There are 3 bolls in this bag , and 12 in the '
remove_numbers(input_str)

# pip install inflect
# We can also convert the numbers into 

import inflect
p=inflect.engine()

# convert number into words
def convert_number(text):
    # split string into list of words
    temp_str=text.split()
    # initialise empty list
    new_string=[]
    for word in temp_str:
        # if word digit , convert 
        if word.isdigit():
            temp=p.number_to_words(word)
            new_string.append(temp)
            
            # append the word as it is
        else:
            new_string.append(word)
    # join the words of new string to form a string
    temp_str=' '.join(new_string)
    return temp_str
inp='Vaibhav UCS 2 1 M 1 0 21'
input_str='There are 3 bolls in this bag , and 12 in the '
convert_number(input_str)
convert_number(inp)

# Reverse each word of a string

stri='My Name is Jessa'
def Reverse_words(text):
    words=text.split(" ")
    new_word=[word[::-1] for word in words]
    
    res_str=" ".join(new_word)
    return res_str
Reverse_words(stri)

# check
stri='My Name is Jessa'
def Reverse_words(text):
    words=text.split(" ")
    new_word=[word[::-1] for word in words]
    return new_word
    
Reverse_words(stri) 

# Assume you have a file 
a=open('sample.txt')
b=a.read()
b.append(a)
b

lines=a.readlines()
lines

for line in lines:
    new_line=line

filename='sample.txt'
with open(filename) as file_object:
    lines=file_object.raedlines()
    for line in lines:
      print(line)

filename='sample.txt'
with open(filename) as file_object:
    lines=file_object.readlines()
    new_string=' '
    for line in lines:
        new_string += " "+line.rstrip()
    print(new_string)
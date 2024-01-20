"""
Created on Wed May 24 08:43:58 2023

@author: Vaibhav Bhorkade

"""

# Unicode 
# Normalizaing unicode text to standard representation 
# You are working with Unicode strings 

s1='Spicy Jalape\u00f1o'
s2='Spicy Jalapen\u0303o'
print(s1)
print(s2)
s1==s2

# unicodedata
import unicodedata

t1=unicodedata.normalize('NFC', s1)
t2=unicodedata.normalize('NFC', s2)

t1 == t2

print(ascii(t1))
# Spicy Jalape\xf10
t3=unicodedata.normalize('NFD', s1)
t4=unicodedata.normalize('NFD', s2)

t3==t4

print(ascii(t3))

# Normalization

t1=unicodedata.normalize('NFD', s1)
''.join(c for c in t1 if not unicodedata.combining(c))

# Working with unicode char in regular # expressions
# process text

import re
num=re.compile('\d+')
num.match('123')

# It is also matching combined
pat=re.compile('Stra\u00dfe',re.IGNORECASE)
pat
s='straße'
pat.match(s)
pat.match(s.upper())
s.upper()

# Straping Unwanted char from strings
# Whitespace straping

s='      helllo world \n'
s.strip()

# Left hand whitespace is removed
s.lstrip()

# Right hand side whitespace is removed
s.rstrip()

# Character straping

t='---------hello========='

# - part remove
t.lstrip('-')

# -= both are remove
t.strip('-=')

t.rstrip('=')

# 
"""
Created on Thu May 25 08:13:56 2023

@author: Vaibhav Bhorkade

"""
# s.strip() remove \n

s='      helllo world \n'
s=s.strip()
print(s)

# replace
s='      helllo world \n'
s.replace(' ', '')

s.replace('', ' ')

# Remove spaces

import re
s='      hello world \n'
re.sub('\s+',' ',s)

# the first step is to clean up the whitespaces , to do this ,
# make a small traslate  and use translate

s = 'pýtĥöñ\fis\tawesome\r\n'
print(s)

remap={
       ord('\t'): ' ',
       ord('\f'): ' ',
       ord('\r'): None
}
a=s.translate(remap)
a

# Removing all combining char 

import unicodedata
import sys

cmb_chrs=dict.fromkeys(c for c in range (sys.maxunicode)if unicodedata.combining(chr(c)))
b=unicodedata.normalize('NFD', a)
b

b.translate(cmb_chrs)

# another teq for decoding text
# Another encode 

a='pýtĥöñ is awesome\n'

b=unicodedata.normalize('NFD', a)
b.encode('ascii','ignore').decode('ascii')

####################################################

# Aligning the text string

text='Hello World'

text.ljust(20)

text.rjust(20)

text.center(20)

# 
text.rjust(20,'=')

text.center(20,'*')

# format method 
# Towards direction shift

# Towads right side
format(text,'>20')

# Towards left side
format(text,'<20')

# For center 
format(text,'^20')

# formating values
'{:>10s}{:>10s}'.format('hello', 'World')

# # # # # ## # # # # # # # # # # # # # # # # # # # # 

x=1.2345
format(x,'>10')
x
format(x,'^10.2f')

# Join
parts=['Is','chicago','Not','chicago?']
' '.join(parts)


'Is Chicago Not Chicago?'
','.join(parts)
'Is,Chicago,Not,Chicago?'
'IsChicagoNotChicago?'

# If you joim very few strings then can use + operator
a='Is Chicago'
b='Not Chicago'
a+ " "+ b

# .format method
print('{} {}'.format(a,b))

print(a+' '+b)

### Without concatnation operator

a='Hello' 'world'
print(a)

# Interpolating variables in string

s='{name} has {n} messages.'
s.format(name='Guido', n=37)

# 
s='{name} has {n} messages.'
name='Vaibhav'
n=37
s.format_map(vars())

# Extract or split after 10 spaces char
s='Look into my eyes , look into my eyes,the eyes,my eyes,Look at my eyes'

import textwrap

print(textwrap.fill(s,10))

print(textwrap.fill(s,20))

# Initial Indent
print(textwrap.fill(s,20 ,initial_indent='      '))

# Subsequent Indent
print(textwrap.fill(s,20,subsequent_indent='  '))


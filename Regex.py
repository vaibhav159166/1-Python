"""
Created on Tue Jun  6 07:58:28 2023

@author: Vaibhav Bhorkade

"""

from PyPDF2 import PdfFileReader

from PyPDF2 import PdfReader

reader=PdfReader('C:/1-python/Unit-1.pdf')

# Printing number of pages
print(len(reader.pages))

# getting a specific page 
page=reader.pages[1]

# extracting texty from page 
text=page.extract_text()
print(text)

#######################################
import re
chat2='HI: I havea problem with my order no 412889912'
pattern='order[^\d]*(\d)'
matches=re.findall(pattern,chat2)
matches



"""
Created on Wed Jun  7 08:13:51 2023

@author: Vaibhav Bhorkade

"""

# regex101.com - we can design a patturn

import re

# Extrate only mobile number from text 

text1="My mobile number is 9022709041"
text2="My alternate mobile number is 9999999911"
text3="My international no is (123)-232-21234"
text4="My international no is [123]-232-21234"

pat1=r"\d{10}"
mob_num=re.findall(pat1, text1)
mob_num

pat2=r"\d{10}"
mob_num1=re.findall(pat2, text2)
mob_num1

pat3=r"\(\d{3}\)-\d{3}-\d{5}"
mob_num2=re.findall(pat3, text3)
mob_num2

pat4=r"\[\d{3}\]-\d{3}-\d{5}"
mob_num3=re.findall(pat4, text4)
mob_num3

# Extract email from text

text1="My email is vaibhavbhorkade159166@gmail.com"
text2="My official email is vaibhavbhorkade060763@gmail.com"
text3="vaibhavbhorkadeABC15_9166@gmail.com"


pat1=r"[a-zA-Z_0-9]*@[a-z]*\.com"
email=re.findall(pat1, text1)
email

pat2=r"[a-zA-Z_0-9]*@[a-z]*\.com"
email=re.findall(pat2, text2)
email


pat2=r"[a-zA-Z_0-9]*@[a-z]*\.com"
email=re.findall(pat2, text3)
email


# yourname.surname@Sanjivani.org.in

text1='yourname.surname@Sanjivani.org.in'
text2='Vaibhav.Bhorkade@sanjivani.org.in'
pat=r"[a-zA-Z]*.[a-zA-Z]*@[a-zA-Z]*.[a-z]*"

col=re.findall(pat, text2)
col

# For finding order number from text

text1="Hi my order #496724 is not recived yet "
text2="Hi,I have problem with my order number 496724"
text3="Hi My order 496724 is having an issue"

pat=r"order[^\d]*\d*"

col=re.findall(pat, text1)
col

col=re.findall(pat, text2)
col

col=re.findall(pat, text3)
col

# for only number 
pat=r"order[^\d]*(\d*)"
match=re.findall(pat, text1)
match

match=re.findall(pat, text2)
match

match=re.findall(pat, text3)
match

####################################################
text="Hi my order #496724 is not recived yet "
def get_pattern_match(pattern,text):
    matches=re.findall(pattern, text)
    if matches:
        return matches
get_pattern_match('order[^\d]*(\d*)',text)

# Retrive email id and phone

chat1="Hi contact with me on 1234567890,abc@gmail.com"
get_pattern_match(r"\d{10}"+'[a-zA-Z_0-9]*@[a-z]*\.com',chat1)

##################################################



text='''Born	Elon Reeve Musk
June 28, 1971 (age 51)
Pretoria, Transvaal, South Africa
Education	University of Pennsylvania (BA, BS)
Title	
    Founder, CEO and chief engineer of SpaceX
    CEO and product architect of Tesla, Inc.
    Owner, CTO and chairman of Twitter
    President of the Musk Foundation
    Founder of the Boring Company, X Corp. and X.AI
    Co-founder of Neuralink, OpenAI, Zip2 and X.com (part of PayPal)
    Spouses	
    Justine Wilson
​
    ​(m. 2000; div. 2008)​
    Talulah Riley
​
    ​(m. 2010; div. 2012)​
​
    ​(m. 2013; div. 2016)​
    Partner	Grimes (2018–2021)[1]
    Children	10[a][3]
    Parents	
    Errol Musk (father)
    Maye Musk (mother)
    Family	Musk family
    Signature'''
def get_pattern_match(pattern,text):
    matches=re.findall(pattern,text)
    if matches:
        return matches
    
get_pattern_match(r'age (\d+)', text)
match=get_pattern_match(r'Born(.*)', text)

match=get_pattern_match(r'Born(.*)',text)
match[0].strip()

"""
Created on Thu Jun  8 08:18:50 2023

@author: Vaibhav Bhorkade

"""

text='''Born	Elon Reeve Musk
June 28, 1971 (age 51)
Pretoria, Transvaal, South Africa
Education	University of Pennsylvania (BA, BS)
Title	
    Founder, CEO and chief engineer of SpaceX
    CEO and product architect of Tesla, Inc.
    Owner, CTO and chairman of Twitter
    President of the Musk Foundation
    Founder of the Boring Company, X Corp. and X.AI
    Co-founder of Neuralink, OpenAI, Zip2 and X.com (part of PayPal)
    Spouses	
    Justine Wilson
​
    ​(m. 2000; div. 2008)​
    Talulah Riley
​
    ​(m. 2010; div. 2012)​
​
    ​(m. 2013; div. 2016)​
    Partner	Grimes (2018–2021)[1]
    Children	10[a][3]
    Parents	
    Errol Musk (father)
    Maye Musk (mother)
    Family	Musk family
    Signature'''
    
def extract_personal_information(text):
    age=get_pattern_match(r'age (\d+)',text)
    full_name=get_pattern_match('Born(.*)\n',text)
    birth_date=get_pattern_match('Born.*\n(.*)\(*age', text)
    birth_place=get_pattern_match('\(age.*\n(.*)', text)
    return {
        'age':age,
        'name':full_name,
        'birth_date':birth_date,
        'birth_place':birth_place
        }
extract_personal_information(text)


###################################################

text = '''Ambani in 2007
Born	Mukesh Dhirubhai Ambani
19 April 1957 (age 66)
Aden, Colony of Aden
(present-day Yemen)[1][2]
Nationality	Indian
Alma mater	
St. Xavier's College, Mumbai
Institute of Chemical Technology (B.E.)
Occupation(s)	Chairman and MD, Reliance Industries
Spouse	Nita Ambani ​(m. 1985)​[3]
Children	3
Parent	
Dhirubhai Ambani (father)
Relatives	Anil Ambani (brother)
Tina Ambani (sister-in-law)'''


def extract_personal_information(text):
    age = get_pattern_match(r'age (\d+)', text)
    full_name = get_pattern_match('Born(.*)\n', text)
    birth_date = get_pattern_match('Born.*\n(.*)\(*age', text)
    birth_place = get_pattern_match('\(age.*\n(.*)', text)
    return {
        'age': age,
        'name': full_name,
        'birth_date': birth_date,
        'birth_place': birth_place
    }


extract_personal_information(text)

# Extract twitter handles from text

text='''
Follow our leader Elon musk on twitter here: https://twitter.com/elonmusk, more information 
on Tesla's products can be found at https://www.tesla.com/. Also here are leading influencers 
for tesla related news,
https://twitter.com/teslarati
https://twitter.com/dummy_tesla
https://twitter.com/dummy_2_tesla
'''
pattern='https://twitter\.com/([a-zA-Z0-9_]+)'

re.findall(pattern,text)

# New extract
text='''Concentration of Risk: Credit Risk
Financial instruments that potentially subject us to a concentration of credit risk consist of cash, cash equivalents, marketable securities,
restricted cash, accounts receivable, convertible note hedges, and interest rate swaps. Our cash balances are primarily invested in money market funds
or on deposit at high credit quality financial institutions in the U.S. These deposits are typically in excess of insured limits. As of September 30, 2021
and December 31,'''

pattern='Concentration of Risk: ([^\n]*)'

re.findall(pattern, text)

text='''Tesla's gross cost of operating lease vehicles in FY2021 Q1 was $4.85 billion.
BMW's gross cost of operating vehicles in FY2021 S1 was $8 billion.'''

pattern='FY(\d{4} (?:Q[1-4]|S[1-2]))'

matches=re.findall(pattern, text)
matches

# extract phone number

text='''
Elon musk's phone number is 9991116666, call him if you have any questions on dodgecoin. Tesla's revenue is 40 billion
Tesla's CFO number (999)-333-7777.
'''

pattern='\(d{3}\)-d{3}-\d{4}|\d{10}'

matches=re.findall(pattern, text)
matches

# Extract
text = '''
Note 1 - Overview
Tesla, Inc. (“Tesla”, the “Company”, “we”, “us” or “our”) was incorporated in the State of Delaware on July 1, 2003. We design, develop, manufacture and sell high-performance fully electric vehicles and design, manufacture, install and sell solar energy generation and energy storage
products. Our Chief Executive Officer, as the chief operating decision maker (“CODM”), organizes our company, manages resource allocations and measures performance among two operating and reportable segments: (i) automotive and (ii) energy generation and storage.
Beginning in the first quarter of 2021, there has been a trend in many parts of the world of increasing availability and administration of vaccines
against COVID-19, as well as an easing of restrictions on social, business, travel and government activities and functions. On the other hand, infection
rates and regulations continue to fluctuate in various regions and there are ongoing global impacts resulting from the pandemic, including challenges
and increases in costs for logistics and supply chains, such as increased port congestion, intermittent supplier delays and a shortfall of semiconductor
supply. We have also previously been affected by temporary manufacturing closures, employment and compensation adjustments and impediments to
administrative activities supporting our product deliveries and deployments.
Note 2 - Summary of Significant Accounting Policies
Unaudited Interim Financial Statements
The consolidated balance sheet as of September 30, 2021, the consolidated statements of operations, the consolidated statements of
comprehensive income, the consolidated statements of redeemable noncontrolling interests and equity for the three and nine months ended September
30, 2021 and 2020 and the consolidated statements of cash flows for the nine months ended September 30, 2021 and 2020, as well as other information
disclosed in the accompanying notes, are unaudited. The consolidated balance sheet as of December 31, 2020 was derived from the audited
consolidated financial statements as of that date. The interim consolidated financial statements and the accompanying notes should be read in
conjunction with the annual consolidated financial statements and the accompanying notes contained in our Annual Report on Form 10-K for the year
ended December 31, 2020.
'''

pattern='Note \d - ([^\n]*)'
matches=re.findall(pattern,text)
matches

# Extract finacial period

text = '''
The gross cost of operating lease vehicles in FY2021 Q1 was $4.85 billion.
In previous quarter i.e. FY2020 Q4 it was $3 billion. 
'''

pattern='FY\d{4} Q[1-4]'

matches=re.findall(pattern, text)
matches

text = '''
The gross cost of operating lease vehicles in FY2021 Q1 was $4.85 billion.
In previous quarter i.e. fy2020 Q4 it was $3 billion. 
'''

pattern='FY\d{4} Q[1-4]'

matches=re.findall(pattern, text,flags=re.IGNORECASE)
matches

# Extract only finacial number
text = '''
The gross cost of operating lease vehicles in FY2021 Q1 was $4.85 billion.
In previous quarter i.e. FY2020 Q4 it was $3 billion. 
'''

pattern='\$([0-9\.]+)'

# Giving [0-9\.] all number use $ for particular
matches=re.findall(pattern, text,flags=re.IGNORECASE)
matches


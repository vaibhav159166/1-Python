"""
Created on Fri May 26 08:16:07 2023

@author: Vaibhav Bhorkade

"""

# Tokenization 

# nltk.download('punkt')

import nltk
nltk.download('punkt')
sentence_data='The first sentence is about Python. The Second is about Django. You can learn python an Django is here'
nltk_tokens=nltk.sent_tokenize(sentence_data)
print(nltk_tokens)

# Non-English Tokenization

import nltk
german_tokenizer=nltk.data.load('tokenizers/punkt/germon.pickle')
german_tokens=german_tokenizer.tokenize("Wie geht es Ihnen? Gut, danke.")
print(german_tokens)

# Word Tokenization
word_data="The first sentence is about Python. The Second is about Django."
nltk_tokens=nltk.word_tokenize(word_data)
print(nltk_tokens)

# stopwords - are,have,do
import nltk
nltk.download('stopwords')

german_tokenizer=nltk.data.load('tokenizers/punkt/japanese.pickle')
from nltk.corpus import stopwords
stopwords.words('english')

stopwords.words('german')

# Various langauage stopwords

from nltk.corpus import stopwords
print(stopwords.fileids())

###########################################

from nltk.corpus import stopwords
en_stops=set(stopwords.words('english'))

all_word=['There ','is','a','tree','near','the','river']
for word in all_word:
    if word not in en_stops:
        print(word)

##########################################

# Find synonyms words

import nltk
nltk.download('omw-1.4')
from nltk.corpus import wordnet

nltk.download('wordnet')

synonyms=[]

for syn in wordnet.synsets("Soil"):
    for lm in syn.lemmas():
        synonyms.append(lm.name())
print(set(synonyms))

# synonyms for tree
synonyms=[]
for syn in wordnet.synsets("tree"):
    for lm in syn.lemmas():
        synonyms.append(lm.name())
print(set(synonyms))

# Find Antonyms words

import nltk
nltk.download('omw-1.4')
from nltk.corpus import wordnet

nltk.download('wordnet')

antonyms=[]
for syn in wordnet.synsets("ahead"):
    for lm in syn.lemmas():
        if lm.antonyms():
            antonyms.append(lm.antonyms()[0].name())
            
print(set(antonyms))

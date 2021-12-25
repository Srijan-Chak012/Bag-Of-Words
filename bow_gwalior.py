#!/usr/bin/env python
# coding: utf-8


import time
start_time = time.time()
import nltk
nltk.download('punkt')
nltk.download('stopwords')


import string
filename = "gwalior.txt"
infile = open(filename, "r")
text = infile.read()
infile.close()

import sys

from nltk.tokenize import word_tokenize
tokens = word_tokenize(text)
#print(tokens)

words = [word for word in tokens if word.isalpha()]
#print(words)

from nltk.corpus import stopwords
stop_words = set(stopwords.words('english'))
#print(stop_words)

import re
nt = []
for token in words:
    token = re.sub(r'[^\w\s]', '', token)
    nt.append(token.lower())
ns = []
for stoken in stop_words:
    stoken = re.sub(r'[^\w\s]', '', stoken)
    ns.append(stoken.lower())

#print(nt)

#print(ns)

cwords = [cword for cword in nt if (cword not in ns)]
#print(cwords)

from nltk.stem import SnowballStemmer
sword = [];
for w in cwords:
    snowball = SnowballStemmer('english')
    sword.append(snowball.stem(w))
#print(sword)

final = {}
for w in sword:
    if(w not in final.keys()):
        final[w] = 1;
    else:
        final[w] = int(final[w]) + 1

# import pprint
# pprint.pprint(final)

for w in final.keys():
    print(w + ' : ' + str(final[w])) 

print("%s seconds" % (time.time() - start_time))
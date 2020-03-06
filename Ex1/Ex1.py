# TASK: you will have to perform the following steps to create a clean version of the data

#1. Read the CSV file
#2. In the content field, do the following:
#- Tokenize and lower-case the text (end result should be an array of tokens where each token is a lexical unit or a punctuation). For example, “He said: ‘Don’t go there!’” => (he, said, :, ‘, don’t, go, there, !, ‘)
#- Remove consecutive spaces and new lines
#- Find and replace URLs with <URL>
#- Find and replace dates with <DATE>
#- Find and replace numbers with <NUM>
#3. For the metadata fields:
#- Fill all empty fields with a placeholder NULL
#
#Next, perform an exploratory evaluation of the cleaned data and report the results. The exploration can include (but need not be limited to):
#- counting the number of URLs in the data
#- counting the number of dates in the data
#- counting the number of numeric values in the data
#- determining the 100 more frequent words that appear in the data
#- plotting the frequency of the 10000 most occuring words (do you seen any interesting patterns?)

#You will want to use the following python packages for performing these tasks:
#clean-text - for cleaning the text (https://pypi.org/project/clean-text/)
#datetime - for date/time conversions (https://docs.python.org/3/library/datetime.html)


import csv
import datetime
import urllib.request
import urllib.error
import nltk
from cleantext import clean
import re
import pandas as pd


def change_date(word):
    date_patterns = ['(\d+[-/]\d+[-/]\d+)']
    for pattern in date_patterns:
        try:
            #check that the pattern can be transformed
            re.sub(pattern, "<DATE>", word)
        except:
            return
            
with open('news_sample.csv', newline='') as csvfile:
    contentIdx = 0
    file = csv.reader(csvfile)
    head = file.__next__()
    for i in range(len(head)):
        if str(head[i]) == "content":
            contentIdx = i
    print(contentIdx)
    data = ""
    
    for row in file:
        content = row[contentIdx]
        content = clean(content, lower=True, no_line_breaks=True, no_urls=True, replace_with_url=" <URL> ", no_punct=True)
        content = content.split()
        #newContent = ""
        #for item in content:
        #    newContent += change_date(item) + " "
        change_date(content)
            
        content = clean(content, no_numbers=True, replace_with_number=" <NUM> ")
        data += content
        row[contentIdx] = content
        print(data)
    
    #hvis man vil tælle ord
    #data_tokens = nltk.word_tokenize(data)
    #freq = nltk.FreqDist(data_tokens)
    #print(freq.elements)

#split csv fil op i tilsvarerende tabeller i sql database
#https://www.postgresql.org/docs/9.2/sql-copy.html 

#df = pd.DataFrame(csvfile)#df = pd.DataFrame(csvfile)
#dele df op...
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

#If you don't yet have a working copy of Python of our computer, please see the exercises from last week. We recommend using Anaconda with Python 3.* (https://docs.conda.io/en/latest/miniconda.html).

#You will want to use the following python packages for performing these tasks:
#clean-text - for cleaning the text (https://pypi.org/project/clean-text/)
#datetime - for date/time conversions (https://docs.python.org/3/library/datetime.html)


import numpy as np
import pandas as pd
import nltk

data = pd.read_csv("news_sample.txt", ",")

data.head()

for col in data.columns: 
    print(col) 

for content in range(len(data['content'])):
    data.content[content] = data.content[content].lower()
    data.content[content] = nltk.word_tokenize(data.content[content])    

print(data['content'])
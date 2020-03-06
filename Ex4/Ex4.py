import csv
import datetime
import urllib.request
import urllib.error
import nltk
from cleantext import clean
import re
import numpy as np

def change_date(word):
    date_patterns = ['(\d+[-/]\d+[-/]\d+)']
    for pattern in date_patterns:
        try:
            #check that the pattern can be transformed
            re.sub(pattern, "<DATE>", word)
        except:
            return

def putinDic(dictionary, liste):
    liste = list(set(liste))
    liste.sort()
    ID = 0
    for j in range(len(liste)):
        info = str(liste[j])
        dictionary[info] = ID
        ID += 1

def simpleEntityToCSV(filename, idName, keyName, dictionary):
    file = open(filename,"w+")
    file.write("%s,%s\n" % (idName, keyName))
    for item in dictionary.items():
        file.write("%s,%s\n" %(str(item[1]), str(item[0])))
    file.close
     
with open('news_sample.csv', newline='', encoding='utf8') as csvfile:
    #initializes indexes for later extraction
    idIdx = 0
    domainIdx = 0
    typeIdx = 0
    urlIdx = 0
    contentIdx = 0
    scraped_atIdx = 0
    inserted_atIdx = 0
    updated_atIdx = 0
    titleIdx = 0
    authorsIdx = 0
    keywordsIdx = 0
    meta_keywordsIdx = 0
    meta_descriptionIdx = 0
    tagsIdx = 0
    summaryIdx = 0
    authorID = 0

    #This initializes the dictionary
    author = dict()
    domain = dict() 
    typ = dict()
    keyword = dict()   
    article = dict()

    #opens file and reads header into head
    csvfile = csv.reader(csvfile)
    head = csvfile.__next__()
    
    #Finds indexes of columns 
    for i in range(len(head)):
        if str(head[i]) == "id": #identification given to each article
            idIdx = i
        elif str(head[i]) == "domain": #simple form of the url
            domainIdx = i
        elif str(head[i]) == "type": #how reliable the source is
            typeIdx = i
        elif str(head[i]) == "url": #link to article itself
            urlIdx = i
        elif str(head[i]) == "content": #all the juice of the article
            contentIdx = i
        elif str(head[i]) == "scraped_at": #date of 
            scraped_atIdx = i
        elif str(head[i]) == "inserted_at":
            inserted_atIdx = i
        elif str(head[i]) == "updated_at":
            updated_atIdx = i
        elif str(head[i]) == "title":
            titleIdx = i
        elif str(head[i]) == "authors": #who made this source
            authorIdx = i
        elif str(head[i]) == "keywords":
            keywordsIdx = i
        elif str(head[i]) == "meta_keywords":
            meta_keywordsIdx = i
        elif str(head[i]) == "meta_description":
            meta_descriptionIdx = i
        elif str(head[i]) == "tags":
            tagsIdx = i
        elif str(head[i]) == "summary":
            summaryIdx = i

    #converts csv.reader type to 2d array
    data = np.array(list(csv.reader(csvfile)))
    
    #fills authors into author dictionary, sort to make sure they get the same id every time the code is run
    authorList = data[:,authorIdx]
    temp = []
    for i in authorList:
        something = i.split(", ")
        for j in something:
            temp.append(j)
    putinDic(author, temp)
    
    #fills metaKeywords into author dictionary, sort to make sure they get the same id every time the code is run
    tempKeywords = data[:,meta_keywordsIdx]
    keywords = []
    for words in tempKeywords:
        temp = re.split(r'[;,"\'\[\]]\s*', words)
        for word in temp:
            keywords.append(word)
    putinDic(keyword,keywords)

    #fills domains into author dictionary, sort to make sure they get the same id every time the code is run
    putinDic(domain,data[:,domainIdx])

    #fills types into author dictionary, sort to make sure they get the same id every time the code is run
    putinDic(typ,data[:,typeIdx])

    #example of how to extract and print data from dictionaries, to be used for riding into .csv files
    simpleEntityToCSV("author_entity.csv", "author_id", "author_name", author)
    simpleEntityToCSV("keyword_entity.csv", "keyword_id", "keyword", keyword)
    simpleEntityToCSV("domain_entity.csv", "domain_id", "domain_url", domain)
    simpleEntityToCSV("type_entity.csv", "type_id", "type_name", typ)

#split csv filer op i tilsvarerende tabeller i sql database
#Keyword(keyword_id,keyword) done 
#Author(author_id,author_name) done 
#Domain(domain_id, domain_url) done 
#Type(type_id,type_name) done 
#Article(article_id, title, content, summary, meta_description, type_id, inserted_at, updated_at, scaped_at)
#Webpage(url,article_id,domain_id) 
#Tags(article_id, keyword_id) 
#Written_by(article_id,author_id) 
#commando i post gress: https://www.postgresql.org/docs/9.2/sql-copy.html 


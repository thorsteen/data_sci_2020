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
    #liste = liste.split(", ") #split on something here or have it premade
    #print(liste)
    ID = 0
    for j in range(len(liste)):
        info = str(liste[j])
        dictionary[info] = ID
        ID += 1
     
with open('news_sample.csv', newline='') as csvfile:
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

    file = csv.reader(csvfile)
    head = file.__next__()
    #NULL,id,domain,type,url,content,scraped_at,inserted_at,updated_at,title,authors,keywords,meta_keywords,meta_description,tags,summary
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
    

    #This initializes the dictionary
    author = dict()
    domain = dict() 
    typ = dict()
    keyword = dict()   
    article = dict()

    data = list(csv.reader(csvfile))
    data = np.array(data)
    
    authorList = data[:,authorIdx]
    temp = []
    for i in authorList:
        something = i.split(", ")
        for j in something:
            temp.append(j)
    temp = list(set(temp))
    putinDic(author, temp)
    
    tempKeywords = data[:,meta_keywordsIdx]
    keywords = []
    for words in tempKeywords:
        temp = re.split(r'[;,"\'\[\]]\s*', words)
        for word in temp:
            keywords.append(word)
    keywords = list(set(keywords))
    putinDic(keyword,keywords)

    domains = list(set(data[:,domainIdx]))
    putinDic(domain,domains)

    typs = list(set(data[:,typeIdx]))
    putinDic(typ,typs)

    for item in author.items():
        print("Author: %-35s has id: %4s" %(str(item[0]), str(item[1])))


    #for row in file:
     #   for i in range(len(row)):
            #if i == idIdx:
            #    print(row[i])
            #elif i == domainIdx:
            #    domains = row[i].split(".")
            #    print(domains)
            #    for j in range(len(domains)):
            #        domainName = str(domains[j])
            #        domain[domainName] = domainID
            #        domainID += 1
            #elif i == typeIdx:
            #elif str(head[i]) == "url": #link to article itself`
            #elif i == contentIdx:
            #    content = row[contentIdx]
            #    content = clean(content, lower=True, no_line_breaks=True, no_urls=True, replace_with_url=" <URL> ", no_punct=True)
            #    content = content.split()
            #    #newContent = ""
            #    #for item in content:
            #    #    newContent += change_date(item) + " "
            #    change_date(content)
            #        
            #    content = clean(content, no_numbers=True, replace_with_number=" <NUM> ")
            #    row[contentIdx] = content
            #elif i == scraped_atIdx:
            #elif i == inserted_atIdx:
            #elif i == updated_atIdx:
            #elif i == titleIdx:
            #elif i == authorIdx: 
            #    authors = row[i].split(", ")
            #    for j in range(len(authors)):
            #        authorName = str(authors[j])
            #        author[authorName] = authorID
            #        authorID += 1
            #elif i == keywordsIdx:
            #elif i == meta_descriptionIdx
            #elif i == tagsIdx:
            #elif i == summaryIdx:
    


#split csv filer op i tilsvarerende tabeller i sql database
#Keyword(keyword_id,keyword) 
#Author(author_id,author_name) 
#Domain(domain_id, domain_url) 
#Type(type_id,type_name) 
#Article(article_id, title, content, summary, meta_description, type_id, inserted_at, updated_at, scaped_at)
#Webpage(url,article_id,domain_id) 
#Tags(article_id, keyword_id) 
#Written_by(article_id,author_id) 
#commando i post gress: https://www.postgresql.org/docs/9.2/sql-copy.html 


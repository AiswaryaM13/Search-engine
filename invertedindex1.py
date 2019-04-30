from __future__ import division
from bs4 import BeautifulSoup, Comment
from nltk.stem.snowball import SnowballStemmer
from nltk.corpus import stopwords
from urlparse import urljoin
#import math
import numpy as np
import json
import time
import types


list = dict()

def checkForStopwords(checkword):
    stopword = set(stopwords.words('english'))
    if checkword in stopword:
        return True
    else:
        return False


def stemWords(stemMe):
    stemOutput = SnowballStemmer('english')
    stemMe = stemOutput.stem(stemMe)
    return stemMe


def processText(links,doc_num):
    for link in links:
        words = link.lower().split()
        for s in words:
            #s = word.encode('utf-8')
            if s.isalnum() and len(s) < 15:
                if not checkForStopwords(s):
                    s = stemWords(s)
                    if s in list:  # adding the word to the dictionary if it is alphanumeric
                        if doc_num in list[s]:
                            list[s][doc_num] += 1  # increment the count if the word already exists
                        else:
                            list[s][doc_num] = 1  # add the word and set count =1 if seen for the first time
                    else:
                        list1={doc_num:1}
                        list[s]=list1
            else:
                p = ""
                for a in s:  # traverse character by character if the word is not alphanumeric
                    if a.isalnum():
                        p = p + a
                    else:
                        if not checkForStopwords(p) and len(p) < 15:
                            p = stemWords(p)
                            if p in list:  # adding the word to the dictionary if it is alphanumeric
                                if doc_num in list[p]:
                                    list[p][doc_num] += 1  # increment the count if the word already exists
                                elif p!="":
                                    list[p][doc_num] = 1  # add the word and set count =1 if seen for the first time
                            else:
                                list1={doc_num:1}
                                list[p]=list1
                            p = ""
                if not checkForStopwords(p) and len(p) < 15:
                    p = stemWords(p)
                    if p in list:  # adding the word to the dictionary if it is alphanumeric
                        if doc_num in list[p]:
                            list[p][doc_num] += 1  # increment the count if the word already exists
                        elif p!="":

                            [p][doc_num] = 1  # add the word and set count =1 if seen for the first time
                    else:
                        list1={doc_num:1}
                        list[p]=list1

fileBasePath = "/Users/therohan_21/Python Projects/project3/WEBPAGES_RAW/"
print('Indexing: This will take a while')
for i in range(75):
    fName1 = '%d' %i
    if i<=73:
        N = 500
    else:
        N = 497
    for j in range(N):
        fName2 = '%d' %j
        docNum = fName1 + '/' + fName2
        filePath = fileBasePath + fName1 + '/' + fName2
        with open(filePath,"r") as f:
            duplicate=False
            soup = BeautifulSoup(f.read(),"lxml")

            if  soup.head is not None:
                text = soup.head.findAll(text=True)
                visible_text=[term.string.encode('utf-8') for term in text]
                head=processText(visible_text, docNum)

            if soup.body is not None and not duplicate:
                text = soup.body.findAll(text = True)
                visible_text = [term.string.encode('utf-8') for term in text]
                body = processText(visible_text, docNum)

            if not duplicate:
                urls = []
                for text in soup.find_all('a'):
                    if 'href' in text.attrs:
                        new_url = text.attrs['href']
                        # relative url changes to absolution url
                        if new_url.startswith('/'):
                            urls.append(new_url.encode('utf-8'))
                urls = processText(urls, docNum)
print "Number of unique words:",len(list)
with open('Report', 'w') as fl:
    fl.write(json.dumps(list))


#x = sorted(list.items(), key=lambda x:(-x[1],x[0]))
#for i in x:
    # p = stemWords(i[0])
    # print(p)
    #print("%s\t%s" %i)


basePath= "/Users/therohan_21/Python Projects/project3/WEBPAGES_RAW/bookkeeping.json"
with open(basePath) as json_data:
    d = json.load(json_data)
# first do stemming of Informatics
#let info be the stemmed version of Informatics



info = 'irvine'
stemOutput = SnowballStemmer('english')
info = stemOutput.stem(info)
with open('Search Result irvine', 'w') as fl:
    fl.write("SEARCH QUERY-> irvine\n\n")
    if info in list:
        b = list[info]
        for path in b:
            print path
            print d[path]

            fl.write(d[path])
            fl.write("\n\n")

info = 'informatics'
stemOutput = SnowballStemmer('english')
info = stemOutput.stem(info)
with open('Search Result informatics', 'w') as fl:
    fl.write("SEARCH QUERY-> informatics\n\n")
    if info in list:
        b = list[info]
        for path in b:
            print path
            print d[path]

            fl.write(d[path])
            fl.write("\n\n")
fl.close()

info = 'mondego'
stemOutput = SnowballStemmer('english')
info = stemOutput.stem(info)
with open('Search Result mondego', 'w') as fl:
    fl.write("SEARCH QUERY-> mondego\n\n")
    if info in list:
        b = list[info]
        for path in b:
            print path
            print d[path]

            fl.write(d[path])
            fl.write("\n\n")
fl.close()

info = 'graduate'
stemOutput = SnowballStemmer('english')
info = stemOutput.stem(info)
with open('Search Result graduate', 'w') as fl:
    fl.write("SEARCH QUERY-> graduate\n\n")
    if info in list:
        b = list[info]
        for path in b:
            print path
            print d[path]

            fl.write(d[path])
            fl.write("\n\n")
fl.close()

info = 'bren'
stemOutput = SnowballStemmer('english')
info = stemOutput.stem(info)
with open('Search Result bren', 'w') as fl:
    fl.write("SEARCH QUERY-> bren\n\n")
    if info in list:
        b = list[info]
        for path in b:
            print path
            print d[path]

            fl.write(d[path])
            fl.write("\n\n")
fl.close()
json_data.close()

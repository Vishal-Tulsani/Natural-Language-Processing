from bs4 import BeautifulSoup
import requests
import spacy
import nltk

nlp=spacy.load('en')
verb=[]
adjective=[]
other=[]
url='https://www.geeksforgeeks.org/python-language-introduction/'
page = requests.get(url)
soup = BeautifulSoup(page.text,'html.parser')
text=soup.text
data=text[13953:15000]
p_data=nlp(data)

for i in p_data:
    if i.pos_ == 'VERB':
        verb.append(i)
    elif i.pos_ == 'ADJ':
        adjective.append(i)
    else:
        other.append(i)

print('\n')
print('\n')
print("verbs in the data are:-",verb)
print('\n')
print("@#@#@#@#@#@#@#@#@#@#@#@#@#@#@#@#@#@#@#@#@#@#@#@#@")
print('\n')
print("@#@#@#@#@#@#@#@#@#@#@#@#@#@#@#@#@#@#@#@#@#@#@#@#@")
print('\n')
print("adjective in data are:-",adjective)
print('\n')
print("@#@#@#@#@#@#@#@#@#@#@#@#@#@#@#@#@#@#@#@#@#@#@#@#@")
print('\n')
print("@#@#@#@#@#@#@#@#@#@#@#@#@#@#@#@#@#@#@#@#@#@#@#@#@")
print(other)        

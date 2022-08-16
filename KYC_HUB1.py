#!/usr/bin/env python
# coding: utf-8

# In[2]:


pip install -U bs4


# In[1]:


pip install -U pandas


# In[2]:


pip install -U requests


# # TASK 1

# In[2]:


from bs4 import BeautifulSoup as bs 
import requests
#import pandas as pd
#import nltk
#import re
#from translate import Translator
additional_Advisor_Data=[]
headers= {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36'}
url="https://www.gov.br/economia/pt-br/acesso-a-informacao/institucional/quem-e-quem/gabinete/quem-e-quem-do-gabinete-do-ministro"
response=requests.get(url,headers=headers)
soup=bs(response.content,"html.parser")
roster_table = soup.find('table', class_ = 'plain')
print(type(roster_table))
for person in roster_table.find_all('tbody'):
    rows = person.find_all('tr')
    for row in rows:
        name = row.find_all('td')[-1].text
        university = row.find_all('td')[-2].text
        print(name,university)
print(type(name))


# # TASK 2

# In[4]:


from bs4 import BeautifulSoup
import requests
import json
import re
import pandas as pd

pd.set_option('display.max_columns', None)
pd.set_option('display.max_colwidth', None)

headers= {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36'}

url = 'https://www.iomfsa.im/enforcement/disqualified-directors/'

df_list = []
r = requests.get(url, headers=headers)
soup = BeautifulSoup(r.text, 'xml')
# print(soup)
dismissed_dirs = soup.select('section.accordion-item')
for d in dismissed_dirs:
#     print(d)
    name = d.find('strong', text=re.compile('^Name:')).next_sibling
    address = d.find('strong', text=re.compile('^Address')).next_sibling
    dob = d.find('strong', text=re.compile('^Date of Birth:')).next_sibling
    pod = d.find('strong', text=re.compile('^Period of Disqualification:')).next_sibling
    dod = d.find('strong', text=re.compile('^Dates of Disqualification:')).parent.text
    particulars = d.find('strong', text=re.compile('^Particulars')).find_next('a').text
    df_list.append((name, address, dob, pod, dod, particulars))

df = pd.DataFrame(df_list, columns = ['name', 'address', 'dob', 'pod', 'dod', 'particulars'])
    
#print(df)
#print('--------------')
print(df.to_dict(orient='records'))
print(df.to_json(r'C:\Users\91938\Documents\Export_DataFrame.json'))


# In[ ]:





# -*- coding: utf-8 -*-
"""
@author: Sagar Bhatt
"""


from lxml import html
import requests
from random import random
import math
import pandas as pd

page = requests.get('https://www.cheatsheet.com/gear-style/20-questions-to-ask-siri-for-a-hilarious-response.html')
tree = html.fromstring(page.content)

quotes = tree.xpath('//h2/text()')

for x in range(0,len(quotes)):
    if r'\xao' in quotes[x]:
        quotes[x]=quotes[x][quotes[x].index(r'\xao')+4:len(quotes(x))]
    else:
        quotes[x]=quotes[x][quotes[x].index('.')+2:len(quotes[x])]

df = pd.DataFrame({'Quotes': quotes})
df.index = df.index+1
df.to_csv('quotes.csv', encoding='utf-8-sig')

# Alternative method of writing CSV using 'import csv', for a file that contains only questions
# with open('quotes0.csv', 'w') as f:
#     writer = csv.writer(f)
#     writer.writerow(quotes)
    
# Code to read random question from file
# randomQues = pd.read_csv('quotes.csv').loc[math.floor(61*random()),'Quotes']

randomQues = quotes[math.floor(61*random())]

headers = {
    'Content-Type': 'application/json',
}

data = '{"value1":"'+randomQues+'"}'

response = requests.post(
    'https://maker.ifttt.com/trigger/sendgmail/with/key/cT789ZN_IqL0KD6YLlnwIz', 
      headers=headers, data=data)
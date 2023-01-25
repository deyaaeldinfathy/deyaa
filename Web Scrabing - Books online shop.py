# -*- coding: utf-8 -*-
"""
Created on Wed Jan 25 18:21:57 2023

@author: Deyaa.Elden
"""

# The source of this is https://www.youtube.com/watch?v=MH3641s3Roc&t=18s

import requests
from bs4 import BeautifulSoup
import pandas as pd

# to forloop all pages
books=[]
for i in range(1,51):
    url=f'https://books.toscrape.com/catalogue/page-{i}.html'
    response = requests.get(url)
    response=response.content
    
    soup= BeautifulSoup(response,'html.parser')
    
    # All the books are under ol, so we want to find it
    
    ol=soup.find('ol')
    
    # The details of the books are under (article) which is under (ol)
    
    articles=ol.find_all('article' , class_='product_pod')
    
    #print(articles)
    
    
    for article in articles :
        image=article.find('img')
        title=image.attrs['alt']
        # print(title)
        star=article.find('p')
        star=star['class'][1]
        # print(star)
        price=article.find('p', class_='price_color').text
        # to remove the currency sympol and float
        price=float(price[1:])
        # print(price)
        books.append([title,price,star])
        # print(books)
        
        
df=pd.DataFrame(books,columns=['title','price','star'])
df.to_csv('books.csv')


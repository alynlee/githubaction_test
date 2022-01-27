#crawling

import requests #요청해서 text를 가지고 오는 
from bs4 import BeautifulSoup #가지고온 text를 parsing해서 가공해주는 lib

url = ' https://ridibooks.com/category/new=releases/2200'
response = requests.get(url)
response.encoding = 'utf-8'
html = response.text

soup = BeautifulSoup(html, 'html.parser')

bookservices = soup.select('.title_text')
for no, book in enumerate(bookservices, 1) : 
  print(no, book.text.strip())

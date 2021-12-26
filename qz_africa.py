import requests
from bs4 import BeautifulSoup

r = requests.get('https://qz.com/africa/latest/')

soup = BeautifulSoup(r.text, 'lxml')

title = []

for article in soup.find_all('div',   class_="esSAQ _8S5gh"):
    title.append(article.text)

link = []

for a in soup.find_all('a', class_="eBKpx", href=True):
    link.append(a['href'])

for i in range(len(link)):
    link[i] = 'https://qz.com' + link[i]
    
for i in range(len(title)):
    print("Title: ", title[i])
    print("Link: ", link[i], "\n")
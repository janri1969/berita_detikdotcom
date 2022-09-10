import requests
from bs4 import BeautifulSoup

html_doc = requests.get('https://detik.com')
soup = BeautifulSoup(html_doc.text, 'html.parser')

populer_area = soup.find(attrs={'class': 'box cb-mostpop'})
#populer_area = soup.find(attrs={'class': 'list-content'})

#titles = populer_area.findAll(attrs={'class': 'media__title'})
titles = populer_area.findAll(attrs={'class': 'media__link'})

for title in titles:
    print(title.text)


#print(populer_area)

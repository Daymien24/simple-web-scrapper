import requests
from bs4 import BeautifulSoup


URL = 'https://allegro.pl/kategoria/boze-narodzenie-choinki-11981?bmatch=baseline-eyesa2-dict43-hou-1-2-0205'

page = requests.get(URL)
print(page)
soup = BeautifulSoup(page.text, 'lxml')
try:
    for article in soup.findAll('article'):
        print(article.h2.text)
        cena = article.find('span', '_9c44d_1zemI').text
        print(cena)
except Exception as e:
    print("AJAJAJAJAJAAJ MIKORASON")
    



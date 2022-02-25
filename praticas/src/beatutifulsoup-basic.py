:e
from  bs4 import BeautifulSoup
from urllib.request import urlopen

def playingWebScraping():
    html = urlopen("http://quotes.toscrape.com/").read().decode('utf-8')

    soup = BeautifulSoup(html, features='lxml')
    print(soup.h1)
    print('\n', soup.p)

    all_href = soup.find_all('a')
    all_href = [l['href'] for l in all_href]
    print('\n', all_href)


playingWebScraping();

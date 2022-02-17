from bs4 import BeautifulSoup
from urllib.request import urlopen
from lxml import html
import requests

def playingWebScraping():
    html = urlopen("https://github.com/fga-eps-mds/Projeto01").read().decode('utf-8')

    soup = BeautifulSoup(html, features='html.parser')
    print('\n', soup.p)
    


playingWebScraping();

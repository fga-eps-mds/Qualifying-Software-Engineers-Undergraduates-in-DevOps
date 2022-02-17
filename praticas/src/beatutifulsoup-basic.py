from bs4 import BeautifulSoup
from urllib.request import urlopen
from selenium import webdriver


def captura_dados ():
# if has Chinese, apply decode()
    html = urlopen("https://autenticacao.unb.br/sso-server/login?service=https%3A%2F%2Fsig.unb.br%2Fsigaa%2Flogin%2Fcas").read().decode('utf-8')
    soup = BeautifulSoup(html, features='lxml')
    all_img = soup.findAll('img')
    all_img = [img['src'] for img in all_img]
    print('\n', all_img)
    print('\n', soup.p)

    all_href = soup.find_all('a')
    all_href = [l['href'] for l in all_href]
    print('\n', all_href)

captura_dados()
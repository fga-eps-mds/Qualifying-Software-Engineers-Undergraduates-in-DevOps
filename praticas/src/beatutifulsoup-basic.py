from bs4 import BeautifulSoup
import requests

def dados(url):
    response = requests.get(url)
    html = response.text
    soup = BeautifulSoup(html, 'html.parser') 

    tabela = soup.findAll("td")
    print(tabela)

dados("https://brasil.io/dataset/gastos-deputados/cota_parlamentar/")

 
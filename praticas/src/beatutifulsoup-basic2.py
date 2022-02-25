from bs4 import BeautifulSoup
from urllib.request import urlopen

# if has Chinese, apply decode()
html = urlopen("https://www.york.ac.uk/teaching/cws/wws/webpage1.html").read().decode('utf-8')

soup = BeautifulSoup(html, 'html.parser')
print(soup.prettify())
print('\n', soup.p)

all_href = soup.find_all('a')
all_href = [l['href'] for l in all_href]
print('\n', all_href)
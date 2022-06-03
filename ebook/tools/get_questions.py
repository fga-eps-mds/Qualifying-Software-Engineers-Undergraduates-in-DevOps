import urllib.request
from bs4 import BeautifulSoup
import sys
from inspect import cleandoc


def fetch_links(tag, br=''):
    questions = []
    for filter in ['Votes', 'Frequent']:
        base_url = f'https://{br}stackoverflow.com'
        url = f"{base_url}/questions/tagged/{tag}?tab={filter}"
        html = urllib.request.urlopen(url)

        soup = BeautifulSoup(html, features="html.parser")

        links = [(link.text, base_url+link.attrs['href'])
                 for link
                 in soup.find_all(attrs={"class": "question-hyperlink"})]
        questions.extend(links[:10])

    return list(dict.fromkeys(questions).keys())[:10]


def main():
    en = fetch_links(sys.argv[1])
    br = fetch_links(sys.argv[1], br='pt.')
    result = cleandoc("""
    | Top 10 questões (ingles/global) | Top 10 questões (portugues) |
    | ------------------------------- | --------------------------- |
    """)+'\n'
    for i in range(10):
        result += f'| [{en[i][0]}]({en[i][1]}) | [{br[i][0]}]({br[i][1]}) |\n'
    print(result)
    # print(len(en))
    # print(len(br))


if __name__ == "__main__":
    main()

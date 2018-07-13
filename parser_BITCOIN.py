import urllib.request

from bs4 import BeautifulSoup


def site(url):
    
    response = urllib.request.urlopen(url)
    return response.read()

def parse(html):
    
    soup = BeautifulSoup (html, "lxml")

    data = soup.find('div', class_='large-10 columns contain-to-grid')
    data = data.find('li', id='btcprice').text

    print(data)


def parser_BITCOIN():
    parse(site('https://freebitco.in/?op=signup_page'))



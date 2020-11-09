import requests
from bs4 import BeautifulSoup
import lxml

class BookScraper:

    def __init__(self, url_link):
        self.url_link = url_link

    def get_href(self):
        response = requests.get(self.url_link)
        soup = BeautifulSoup(response.text, 'lxml')
        url_link = soup.find_all('li', {'class':"col-xs-6 col-sm-4 col-md-3 col-lg-3"})
        links = []

        for link in url_link:
            a = link.find('a')
            links.append("http://books.toscrape.com/catalogue/"+ str(a['href']))

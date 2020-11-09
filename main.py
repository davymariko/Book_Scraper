import requests
from bs4 import BeautifulSoup
import lxml
import time
from operator import add

def get_href_links(url_link):
    response = requests.get(url_link)
    soup = BeautifulSoup(response.text, 'lxml')
    href_links = soup.find_all('li', {'class':"col-xs-6 col-sm-4 col-md-3 col-lg-3"})
    url_pattern = "http://books.toscrape.com/catalogue/" 

    links = [url_pattern + str(link.find('a')['href']) for link in href_links]
    
    return links


if __name__ == "__main__":
    url = 'http://books.toscrape.com/catalogue/page-1.html'
    previous = 1
    links = []

    for i in range(1, 51):
        url = url.replace(str(previous), str(i))
        previous = i
        links.append(get_href_links(url))
        time.sleep(1)

    print(len(sum(links, [])))

    

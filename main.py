import requests
from bs4 import BeautifulSoup
import lxml
import time

if __name__ == "__main__":
    url = 'http://books.toscrape.com/catalogue/page-1.html'
    previous = 1
    links = []
    for i in range(1, 51):
        url = url.replace(str(previous), str(i))
        previous = i
        links.append(url)

    response = requests.get(links[2])
    soup = BeautifulSoup(response.text, 'lxml')
    url_link = soup.find_all('li', {'class':"col-xs-6 col-sm-4 col-md-3 col-lg-3"})

    for link in url_link:
        a = link.find('a')
        print("http://books.toscrape.com/catalogue/"+ str(a['href']))
        time.sleep(1)

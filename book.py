import requests
from bs4 import BeautifulSoup
import lxml
import re

def get_description(delicious_soup):
    price = delicious_soup.find_all('p')

    return (price[3].text)
    

def get_title(delicious_soup):
    title = delicious_soup.find('h1')
    
    return (title.text)


def get_upc(delicious_soup):
    upc = delicious_soup.find_all('td')

    return (upc[0].text)


def get_price_tax(delicious_soup):
    price_tax = delicious_soup.find_all('td')

    return (float(re.findall(r"\d+\.\d+", price_tax[2].text)[0]))


def get_price_tax_exclu(delicious_soup):
    price_tax_exclu = delicious_soup.find_all('td')

    return (float(re.findall(r"\d+\.\d+", price_tax_exclu[3].text)[0]))
    

def get_number_available(delicious_soup):
    number_available = delicious_soup.find_all('td')

    return (int(re.findall(r'\d+', number_available[5].text)[0]))


def get_category(delicious_soup):
    category = delicious_soup.find_all('li')

    return (category[2].text.strip())

def get_image_url(delicious_soup):
    image = delicious_soup.find_all('img')
    # this will return src attrib from img tag that is inside 'a' tag
    link_pattern ="http://books.toscrape.com/"

    return (link_pattern + str(image[0]['src'][6:]))


def get_rating(delicious_soup):
    # ratings = delicious_soup.find_all()
    pass


if __name__ == "__main__":
    url = "http://books.toscrape.com/catalogue/art-and-fear-observations-on-the-perils-and-rewards-of-artmaking_559/index.html"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')

    print(get_description(soup))
    print(get_title(soup))
    print(get_upc(soup))
    print(get_price_tax(soup))
    print(get_price_tax_exclu(soup))
    print(get_number_available(soup))
    print(get_category(soup))
    print(get_image_url(soup))


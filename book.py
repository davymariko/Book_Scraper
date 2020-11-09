import requests
from bs4 import BeautifulSoup
import lxml
import re

def get_description(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')
    price = soup.find_all('p')
    check = 0
    print("Description: \n" , price[3].text)
    

def get_title(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')
    title = soup.find('h1')
    print("TITLE: " , title.text)


def get_upc(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')
    upc = soup.find_all('td')
    print("UPC : " , upc[0].text)


def get_price_tax(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')
    price_tax = soup.find_all('td')
    print("Prix avec taxe inclus : " , price_tax[2].text)


def get_price_tax_exclu(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')
    price_tax_exclu = soup.find_all('td')
    print("Prix avec taxe exclus : " , price_tax_exclu[3].text)


def get_number_available(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')
    number_available = soup.find_all('td')
    print("Available in stock : " , re.findall(r'\d+', number_available[5].text)[0])


def get_category(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')
    category = soup.find_all('li')
    print(category[2].text.strip())

def get_image_url(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')
    image = soup.find_all('div', {'class':'item active'})
    print(image[1]['src'])


if __name__ == "__main__":
    url = "http://books.toscrape.com/catalogue/art-and-fear-observations-on-the-perils-and-rewards-of-artmaking_559/index.html"
    get_description(url)
    get_title(url)
    get_upc(url)
    get_price_tax(url)
    get_price_tax_exclu(url)
    get_number_available(url)
    get_category(url)
    get_image_url(url)


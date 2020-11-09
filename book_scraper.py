import requests
from bs4 import BeautifulSoup
import lxml
import re

class BookScraper:

    def __init__(self, url_link):
        self.url_link = url_link
        self.soup = BeautifulSoup(requests.get(url_link).text, 'lxml')

    
    def get_description(self):
        """Une fonction qui permet d'avoir la description du livre
        """
        self.description = self.soup.find_all('p')[3].text


    def get_title(self):
        """Une fonction qui permet d'avoir le titre du livre
        """
        self.title = self.soup.find('h1').text

    
    def get_upc(self):
        self.upc = self.soup.find_all('td')[0].text


    def get_price_tax(self):
        price = self.soup.find_all('td')
        self.price_tax = float(re.findall(r"\d+\.\d+", price[2].text)[0])


    def get_price_tax_exclu(self):
        price = self.soup.find_all('td')
        self.price_tax_exclu = float(re.findall(r"\d+\.\d+", price[3].text)[0])

    
    def get_number_available(self):
        number = self.soup.find_all('td')
        self.number_available = int(re.findall(r'\d+', number[5].text)[0])


    def get_category(self):
        self.category = self.soup.find_all('li')[2].text.strip()

    
    def get_image_url(self):
        image = self.soup.find_all('img')
        link_pattern ="http://books.toscrape.com/"
        self.image_url = link_pattern + str(image[0]['src'][6:])


    def get_rating(self):
        ratings = self.soup.find_all('p', {'class': 'star-rating'})

        if ratings[0]['class'][1] == 'One':
            self.rating = 1
        elif ratings[0]['class'][1] == 'Two':
            self.rating = 2
        elif ratings[0]['class'][1] == 'Three':
            self.rating = 3
        elif ratings[0]['class'][1] == 'Four':
            self.rating = 4
        else:
            self.rating = 5



if __name__ == "__main__":
    Book = BookScraper('http://books.toscrape.com/catalogue/suddenly-in-love-lake-haven-1_835/index.html')
    Book.get_rating()
    Book.get_category()
    Book.get_title()
    Book.get_description()
    Book.get_image_url()
    Book.get_number_available()
    Book.get_price_tax()
    Book.get_price_tax_exclu()
    Book.get_rating()
    Book.get_upc()

    #Testing rating
    print(Book.rating)

    #Testing category
    print(Book.category)

    #Testing title
    print(Book.title)

    #Testing descriptin
    print(Book.description)
    
    #Testing image_url
    print(Book.image_url)

    #Testing number available
    print(Book.number_available)

    #Testing price with tax
    print(Book.price_tax)

    #Testing price with no tax
    print(Book.price_tax_exclu)

    #Testing upc
    print(Book.upc)
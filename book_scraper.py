import requests
from bs4 import BeautifulSoup
import lxml
import re

class BookScraper:

    def __init__(self, url_link):
        self.url_link = url_link
        self.soup = BeautifulSoup(requests.get(url_link).text, 'lxml')

    
    def get_description(self):
        """
        Une fonction qui permet d'avoir la description du livre
        """
        try:
            description = self.soup.select("article.product_page > p")[0].text
        except:
            description = "No Description"

        self.description = description

        return self.description


    def get_title(self):
        """
        Une fonction qui permet d'avoir le titre du livre
        """
        self.title = self.soup.h1.text

        return self.title

    
    def get_upc(self):
        """
        Une fonction qui permet d'avoir l'universal_ product_code (upc) du livre
        """
        self.upc = self.soup.find('table', {'class': 'table table-striped'}).find('td').text

        return self.upc


    def get_price_tax_exclu(self):
        """
        Une fonction qui permet d'avoir le prix taxe exclus du livre
        """
        price = self.soup.find('table').find_all('td')[2].text
        self.price_tax_exclu = re.findall(r"\d+\.\d+", price)[0]

        return float(self.price_tax_exclu)
        # self.price_tax = float(re.findall(r"\d+\.\d+", price.text)[0])


    def get_price_tax(self):
        """
        Une fonction qui permet d'avoir le prix taxe inclus du livre
        """
        price = self.soup.find('table').find_all('td')[3].text.replace(",",".")
        self.price_tax_inclu = re.findall(r"\d+\.\d+", price)[0]

        return float(self.price_tax_inclu)

    
    def get_number_available(self):
        """
        Une fonction qui permet d'avoir le nombre de livre disponible en stock
        """
        number = self.soup.find_all('td')[5].text
        self.number_available = int(re.findall(r'\d+', number)[0])

        return self.number_available


    def get_category(self):
        """
        Une fonction qui permet d'avoir la catégorie du livre
        """
        category = self.soup.find('ul' , {'class':'breadcrumb'})
        self.category = category.find_all('li')[2].text.strip()

        return self.category

    
    def get_image_url(self):
        """
        Une fonction qui permet d'avoir le lien d'image du livre
        """
        image = self.soup.find('div', {'class':'item'}).find('img')
        link_pattern ="http://books.toscrape.com/"
        self.image_url = link_pattern + str(image['src'][6:])

        return self.image_url


    def get_rating(self):
        """
        Une fonction qui permet d'avoir l'evaluation sur 5 du livre
        """
        ratings = self.soup.find('p', {'class': 'star-rating'})['class']
        ratings_dict = {"One": 1, "Two": 2, "Three": 3, "Four": 4, "Five": 5}

        self.rating = ratings_dict[ratings[1]]

        return self.rating

        # if ratings[0]['class'][1] == 'One':
        #     self.rating = 1
        # elif ratings[0]['class'][1] == 'Two':
        #     self.rating = 2
        # elif ratings[0]['class'][1] == 'Three':
        #     self.rating = 3
        # elif ratings[0]['class'][1] == 'Four':
        #     self.rating = 4
        # else:
        #     self.rating = 5

    
    # def get_all(self):
    #     self.get_upc()
    #     self.get_title()
    #     self.get_price_tax()
    #     self.get_price_tax_exclu()
    #     self.get_number_available()
    #     self.get_description()
    #     self.get_category()
    #     self.get_rating()
    #     self.get_image_url()

    
    def save_all_in_dict(self):
        data = [self.url_link, self.get_upc(), self.get_title(), 
            self.get_price_tax(), self.get_price_tax_exclu(),
            self.get_number_available(), self.get_description(),
            self.get_category(), self.get_rating(), self.get_image_url()]

        return data
        



if __name__ == "__main__":
    book = BookScraper('http://books.toscrape.com/catalogue/suddenly-in-love-lake-haven-1_835/index.html')
    
    # # Testing rating
    # print(book.get_rating())

    # #Testing category
    # print(book.get_category())

    # #Testing title
    # print(book.get_title())

    # #Testing descriptin
    # print(book.get_description())
    
    # #Testing image_url
    # print(book.get_image_url())

    # #Testing number available
    # print(book.get_number_available())

    # # Testing price with tax
    # print(book.get_price_tax())

    # #Testing price with no tax
    # print(book.get_price_tax_exclu())

    # # Testing upc
    # print(book.get_upc())

    # del book.__dict__['soup']

    # print(book.__dict__)


    # book.save_all_in_dict()
    # print(*book.data, sep='\n')
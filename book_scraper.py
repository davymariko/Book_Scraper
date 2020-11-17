import requests
from bs4 import BeautifulSoup
import lxml
import re

class BookScraper:

    def __init__(self, url_link):
        self.url_link = url_link
        self.soup = BeautifulSoup(requests.get(url_link).text, 'lxml')

    
    def set_description(self):
        """
        Une fonction qui permet d'avoir la description du livre
        """
        try:
            description = self.soup.select("article.product_page > p")[0].text
        except:
            description = "No Description"

        self.description = description


    def set_title(self):
        """
        Une fonction qui permet d'avoir le titre du livre
        """
        self.title = self.soup.h1.text

    
    def set_upc(self):
        """
        Une fonction qui permet d'avoir l'universal_ product_code (upc) du livre
        """
        self.upc = self.soup.find('table', {'class': 'table table-striped'}).find('td').text


    def set_price_tax_exclu(self):
        """
        Une fonction qui permet d'avoir le prix taxe exclus du livre
        """
        price = self.soup.find('table').find_all('td')[2].text
        self.price_tax_exclu = re.findall(r"\d+\.\d+", price)[0]


    def set_price_tax(self):
        """
        Une fonction qui permet d'avoir le prix taxe inclus du livre
        """
        price = self.soup.find('table').find_all('td')[3].text.replace(",",".")
        self.price_tax_inclu = re.findall(r"\d+\.\d+", price)[0]

    
    def set_number_available(self):
        """
        Une fonction qui permet d'avoir le nombre de livre disponible en stock
        """
        number = self.soup.find_all('td')[5].text
        self.number_available = int(re.findall(r'\d+', number)[0])


    def set_category(self):
        """
        Une fonction qui permet d'avoir la catégorie du livre
        """
        category = self.soup.find('ul' , {'class':'breadcrumb'})
        self.category = category.find_all('li')[2].text.strip()

    
    def set_image_url(self):
        """
        Une fonction qui permet d'avoir le lien d'image du livre
        """
        image = self.soup.find('div', {'class':'item'}).find('img')
        link_pattern ="http://books.toscrape.com/"
        self.image_url = link_pattern + str(image['src'][6:])


    def set_rating(self):
        """
        Une fonction qui permet d'avoir l'evaluation sur 5 du livre
        """
        ratings = self.soup.find('p', {'class': 'star-rating'})['class']
        ratings_dict = {"One": 1, "Two": 2, "Three": 3, "Four": 4, "Five": 5}

        self.rating = ratings_dict[ratings[1]]

    
    def save_all_in_dict(self) -> list:
        self.set_upc()
        self.set_title()
        self.set_price_tax()
        self.set_price_tax_exclu()
        self.set_number_available()
        self.set_description()
        self.set_category()
        self.set_rating()
        self.set_image_url()
        data = [self.url_link, self.upc, self.title, self.price_tax_exclu, 
            self.price_tax_inclu, self.number_available, self.description,
            self.category, self.rating, self.image_url]

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

    # 
    pass
import re
from scrapper.link_request.page_request import page_content


class BookScraper:

    def __init__(self, book_url):
        self.book_url = book_url
        self.soup = page_content(book_url)

    @property
    def description(self):
        """
        Une fonction qui retourne la description du livre
        """
        try:
            description = self.soup.select("article.product_page > p")[0].text
        except:
            description = "No Description"

        return description

    @property
    def title(self):
        """
        Une fonction qui retourne le titre du livre
        """
        try:
            title = self.soup.h1.text
        except:
            title = "No Title"

        return title

    @property
    def uni_product_code(self):
        """
        Une fonction qui retourne l'universal_ product_code (upc) du livre
        """
        try:
            upc = self.soup.find('table', {'class': 'table table-striped'})
            upc = upc.find('td').text
        except:
            upc = "No UPC"

        return upc

    @property
    def price_tax_exclu(self):
        """
        Une fonction qui retourne le prix taxe exclus du livre
        """
        try:
            price = self.soup.find('table').find_all('td')[2].text
            price_tax_exclu = re.findall(r"\d+\.\d+", price)[0]
        except:
            price_tax_exclu = "No Price"

        return price_tax_exclu

    @property
    def price_tax_inclu(self):
        """
        Une fonction qui retourne le prix taxe inclus du livre
        """
        try:
            price = self.soup.find('table').find_all('td')[3]
            price = price.text.replace(",", ".")
            price_tax_inclu = re.findall(r"\d+\.\d+", price)[0]
        except:
            price_tax_inclu = "No Price"

        return price_tax_inclu

    @property
    def number_available(self):
        """
        Une fonction qui retourne le nombre de livre disponible en stock
        """
        try:
            number = self.soup.find_all('td')[5].text
            number_available = int(re.findall(r'\d+', number)[0])
        except:
            number_available = "No Number Available"

        return number_available

    @property
    def category(self):
        """
        Une fonction qui retourne la catégorie du livre
        """
        try:
            category = self.soup.find('ul', {'class': 'breadcrumb'})
            category = category.find_all('li')[2].text.strip()
        except:
            category = "No Category Available"

        return category

    @property
    def image_url(self):
        """
        Une fonction qui retourne le lien d'image du livre
        """
        try:
            image = self.soup.find('div', {'class': 'item'}).find('img')
            link_pattern = "http://books.toscrape.com/"
            image_url = link_pattern + str(image['src'][6:])
        except:
            image_url = "No Image URL available"
        
        return image_url

    @property
    def rating(self):
        """
        Une fonction qui retourne l'evaluation sur 5 du livre
        """
        try:
            ratings = self.soup.find('p', {'class': 'star-rating'})['class']
            ratings_dict = {"One": 1, "Two": 2, "Three": 3,
                "Four": 4, "Five": 5}
            rating = ratings_dict[ratings[1]]
        except:
            rating = "No Rating available"

        return rating

    @property
    def save_all_in_list(self):
        """
        Une fonction qui retourne une liste contenant
        toutes les données sur un livre
        """
        data = [self.book_url, self.uni_product_code, self.title,
        self.price_tax_exclu, self.price_tax_inclu, self.number_available,
        self.description, self.category, self.rating, self.image_url]

        return data
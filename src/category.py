from .page_request import page_content
from .book_scraper import BookScraper

class CategoryClass:

    def __init__(self, category_url: str):
        self.category_url = category_url

    
    def books_data_per_category(self) -> list:
        """
        Fonction qui permet d'avoir tous les données des livres se trouvant dans une catégorie
        
        :param books_urls: Une liste contenant tous les liens des livres à scraper
        """

        books_urls = self.book_urls_per_category()

        books_data = []

        for book_link in books_urls:
            book = BookScraper(book_link)
            books_data.append(book.save_all_in_list())

        return books_data


    def book_urls_per_category(self) -> list:
        """
        Fonction qui retourne tous les liens des livres se trouvant dans une catégorie

        :param website_url: Un string contenant le lien de la première page de recherche
        """
        result = []

        soup = page_content(self.category_url)

        if soup == False:
            print("Page Request Failed")
        else:
            page = soup.find("li", {'class': 'current'})
            result.append(self.get_href_links(self.category_url))

            if page != None:
                page_count = int(page.text.split()[-1])
                previous = 2
                url_pattern = self.category_url
                url_pattern = url_pattern.replace("index.html", "")
                page = "page-2.html"

                for count in range(2,page_count+1):
                    page = page.replace(str(previous), str(count))
                    url = url_pattern + page
                    result.append(self.get_href_links(url))
                    previous = count

        return sum(result, [])


    def get_href_links(self, page_url: str) -> list:
        """
        Fonction qui permet d'avoir les liens href souhaites se trouvant dans une page

        :param page_url: Une liste contenant tous les liens des livres à scraper
        """
        soup = page_content(page_url)

        href_links = []

        if soup == False:
            print("Get href Links FAILED")
        else:
            href_links = soup.find_all('li', {'class':"col-xs-6 col-sm-4 col-md-3 col-lg-3"})
            url_pattern = "http://books.toscrape.com/catalogue"

        links = [url_pattern + str(link.find('a')['href'][8:]) for link in href_links]

        return links



def get_category_urls(website_url: str) -> list:
    """
    Fonction qui retourne tous les liens des catégories de livre se trouvant sur le site
    
    :param website_url: Le lien du site web à scraper
    """

    soup = page_content(website_url)

    if soup == False:
        print("FAIL")
    else:
        category = soup.find('ul', {'class':'nav nav-list'}).find('ul').find_all('li')

    try:
        result = [[cat.text.strip(), (website_url+cat.find('a')['href'])] for cat in category]
    except:
        result = []
        print("Fail to get all category urls")

    return result
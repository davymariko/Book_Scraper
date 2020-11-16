import requests
from bs4 import BeautifulSoup
import lxml
import time
from book_scraper import BookScraper

def book_urls_per_category(category_url):
    """
    Fonction qui permet d'avoir tous les liens des livres se trouvant dans une catégorie

    :param website_url: Un string contenant le lien de la première page de recherche
    """
    response = requests.get(category_url)
    result = []

    if response.ok:
        soup = BeautifulSoup(response.text, 'lxml')
        page = soup.find("li", {'class': 'current'})
        result.append(get_href_links(category_url))

        if page != None:
            page_count = int(page.text.split()[-1])
            previous = 2
            url = category_url.replace("index.html", "page-2.html")

            for count in range(2,page_count+1):
                url = url.replace(str(previous), str(count))
                result.append(get_href_links(url))
                previous = count


    return sum(result, [])


def book_data_per_category(books_urls):
    """
    Fonction qui permet d'avoir tous les données des livres se trouvant dans une catégorie

    :param books_urls: Une liste contenant tous les liens des livres à scraper
    """

    books_data = []

    for book_link in books_urls:
        book = BookScraper(book_link)
        books_data.append(book.save_all_in_dict())

    return books_data


def get_href_links(page_url):
    """
    Fonction qui permet d'avoir les liens href souhaites se trouvant dans une page

    :param page_url: Une liste contenant tous les liens des livres à scraper
    """
    response = requests.get(page_url)
    soup = BeautifulSoup(response.text, 'lxml')
    href_links = soup.find_all('li', {'class':"col-xs-6 col-sm-4 col-md-3 col-lg-3"})
    url_pattern = "http://books.toscrape.com/catalogue" 

    links = [url_pattern + str(link.find('a')['href'][8:]) for link in href_links]
    
    return links


def get_category_urls(website_url):
    """
    Fonction qui permet d'avoir tous les liens des catégories de livre se trouvant sur le sote

    :param website_url: Le lien du site web à scraper
    """
    response = requests.get(website_url)
    soup = BeautifulSoup(response.text, 'lxml')
    category = soup.find('ul', {'class':'nav nav-list'}).find('ul').find_all('li')

    return [[cat.text.strip(), (website_url+cat.find('a')['href'])] for cat in category]


if __name__ == "__main__":
    # print(*get_category_url("http://books.toscrape.com/"), sep="\n")

    # res = book_urls_per_category("http://books.toscrape.com/catalogue/category/books/nonfiction_13/index.html")

    # print(*res, sep="\n")
    # print(len(res))

    print(*get_href_links("http://books.toscrape.com/catalogue/category/books/nonfiction_13/page-4.html"), sep="\n")
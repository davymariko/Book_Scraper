from category import get_category_urls
from category import get_href_links
from category import book_urls_per_category
from category import book_data_per_category
from book_scraper import BookScraper
from save_data import save_csv
from save_data import save_image
import time

def this_function():
    print("Test this")
    

if __name__ == "__main__":
    book_data = []
    print("Bienvenue à Bookscraper\n\n")

    categories = get_category_urls("http://books.toscrape.com/")

    for category_name, category_url in categories:
        book_links = book_urls_per_category(category_url)

        book_data = book_data_per_category(book_links)

        save_csv(category_name, book_data)

        save_image(book_links)
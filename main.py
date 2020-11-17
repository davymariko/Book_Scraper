from category import get_category_urls
from category import get_href_links
from category import book_urls_per_category
from category import books_data_per_category
from book_scraper import BookScraper
from save_data import save_csv
from save_data import save_image
from threading import Thread
import time
    

if __name__ == "__main__":
    book_data = []
    print("Bienvenue à Bookscraper\n\n")
    start_time = time.time()

    categories = get_category_urls("http://books.toscrape.com/")

    check = 1
    for category_name, category_url in categories:
        book_links = book_urls_per_category(category_url)

        print(check)

        print("Book Links: --- %s seconds ---" % (time.time() - start_time))
        
        book_data = books_data_per_category(book_links)

        print("Book Data: --- %s seconds ---" % (time.time() - start_time))

        save_csv(category_name, book_data)

        print("Save CSV: --- %s seconds ---" % (time.time() - start_time))

        # book_image_urls = [url[9] for url in book_data]

        # print("Image url list: --- %s seconds ---" % (time.time() - start_time))

        # save_image(book_image_urls)

        # print("Save Image: --- %s seconds ---" % (time.time() - start_time))

        check += 1

    print("--- %s seconds ---" % (time.time() - start_time))
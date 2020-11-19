from scrapper.models.category import CategoryClass, get_category_urls
from scrapper.export.save_data import save_csv
from scrapper.link_request.page_request import save_image
import time


def main():
    print("Bienvenue à Bookscraper\n\n")
    start_time = time.time()

    categories = get_category_urls("http://books.toscrape.com/")

    book_data = []

    for category_name, category_url in categories:
        this_category = CategoryClass(category_url)
        book_data = this_category.books_data_per_category()
        save_csv(category_name, book_data)
        book_image_urls = [url[9] for url in book_data]
        save_image(book_image_urls)

    print("--- %s seconds ---" % (time.time() - start_time))


if __name__ == "__main__":
    main()
import pandas as pd
import requests
import os
from book_scraper import BookScraper

PATH = os.getcwd()
os.chdir(PATH)

def save_csv(category_name, books_list):
    """
    Fonction qui permet de sauvegarder les livres d'une categorie specifique dans un fichier csv

    :param category_name: Un string qui specifie la categorie de la liste des livres à sauvegarder
    :param books_list: Une liste de donnees de livres d'une categorie specifique
    """

    location = "Assets/CSV_Files/" + category_name.replace(' ', '_')

    os.makedirs(location)

    # Create the pandas DataFrame
    df = pd.DataFrame(books_list, columns = ['Product Page Url', 'UPC', 'Title', 
        'Price Including Tax', 'Price Excluding Tax', 'Number Available',
        'Product Description', 'Category', 'Rating', 'Image Url'])
    
    # Save dataframe
    df.to_csv(location +'/File.csv')


def save_image(book_links):
    """
    Fonction qui permet de sauvegarder l'image du livre visite

    :param book_links: Liste contenant les liens de livres
    """
    location = "Assets/Images/" 
    for link in book_links:
        book = BookScraper(link)
        image_url = book.get_image_url()
        response = requests.get(image_url)
        file_location = location + image_url.split("/")[-1]
        file = open(file_location, "wb")
        file.write(response.content)
        file.close()
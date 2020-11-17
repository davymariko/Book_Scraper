import pandas as pd
import requests
import os
from book_scraper import BookScraper
import urllib.request
import csv

PATH = os.getcwd()
os.chdir(PATH)

def save_csv(category_name: str, books_data_list: list) -> None:
    """
    Fonction qui permet de sauvegarder les livres d'une categorie specifique dans un fichier csv

    :param category_name: Un string qui specifie la categorie de la liste des livres à sauvegarder
    :param books_list: Une liste de donnees de livres d'une categorie specifique
    """

    location = "Assets/CSV_Files/" + category_name.replace(' ', '_')

    os.makedirs(location)

    # Creer un DataFrame Pandas
    df = pd.DataFrame(books_data_list, columns = ['Product Page Url', 'UPC',
        'Title', 'Price Including Tax', 'Price Excluding Tax', 'Number Available',
        'Product Description', 'Category', 'Rating', 'Image Url'])
    
    # Sauvegarder le dataframe en csv
    df.to_csv(location +'/File.csv')


def save_image(image_urls: list) -> None:
    """
    Fonction qui permet de sauvegarder l'image du livre visite

    :param image_urls: Liste contenant les liens des images des livres selectionnés 
    """
    location = "Assets/Images/" 
    for link in image_urls:
        file_location = location + link.split("/")[-1]
        urllib.request.urlretrieve(link, file_location)
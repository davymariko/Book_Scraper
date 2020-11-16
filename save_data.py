import pandas as pd
import requests
import os

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


def save_image(image_url):
    """
    Fonction qui permet de sauvegarder l'image du livre visite

    :param image_url: Le lien de l'image à sauvegarder
    """
    response = requests.get(image_url)
    location = "Assets/Images/"

    file = open(location, "wb")
    file.write(response.content)
    file.close()
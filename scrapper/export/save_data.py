import pandas as pd
import os


def save_csv(category_name, books_data_list):
    """
    Fonction qui permet de sauvegarder les livres d'une categorie
    specifique dans un fichier csv

    :param category_name: Un string qui specifie la categorie 
    de la liste des livres à sauvegarder
    :param books_list: Une liste de donnees des 
    livres d'une categorie specifique
    """

    location = "Assets/CSV_Files/" + category_name.replace(' ', '_')

    if os.path.exists(location +'/File.csv'):
        return
    elif not os.path.exists(location):
        os.makedirs(location)

    # Creer un DataFrame Pandas
    df = pd.DataFrame(books_data_list, columns = ['Product Page Url', 'UPC',
        'Title', 'Price Including Tax', 'Price Excluding Tax', 
        'Number Available', 'Product Description', 'Category', 
        'Rating', 'Image Url'])
    # Sauvegarder le dataframe en csv
    df.to_csv(location +'/File.csv')
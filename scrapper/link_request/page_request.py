from bs4 import BeautifulSoup
import urllib.request
import os
import re


def page_content(page_url):
    """
    Une fonction qui retourne le contenu beautifulsoup d'une page web
    en cas de cas succès et False au cas contraire

    :param page_url: le lien de la page web
    """
    try:
        response = urllib.request.urlopen(page_url)
    except Exception as e:
        print(f'Error while downloading the page {page_url}.\n')
        print(f'Message: {e}')

    return BeautifulSoup(response, 'lxml')


def save_image(images_data):
    """
    Fonction qui permet de sauvegarder l'image du livre visite
    :param images_data: Liste contenant les liens des images et
    les titre des livres selectionnés qui seront les noms des images
    """
    location = "Assets/Images/"
    if not os.path.exists(location):
        os.makedirs(location)
    
    for image_url, book_name in images_data:
        book_name = re.sub(r"[^a-zA-Z0-9]+", ' ', book_name)
        image_name = book_name.replace(" ", "_") + '.png'
        file_location = location + image_name

        if os.path.exists(file_location):
            print(f"\"{file_location}\" already exists")
            print(f"Image URL: {image_url}")

        try:
            urllib.request.urlretrieve(image_url, file_location)
        except Exception as e:
            print(f'[Echec] Telecharger fichier au lien: {image_url}')
            print(f"Message: {e}")
from bs4 import BeautifulSoup
import urllib.request
import os

# PATH = os.getcwd()
# os.chdir(PATH)


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
    

def save_image(image_urls):
    """
    Fonction qui permet de sauvegarder l'image du livre visite

    :param image_urls: Liste contenant les liens des images 
    des livres selectionnés 
    """
    location = "Assets/Images/"
    if not os.path.exists(location):
        os.makedirs(location)
        
    for link in image_urls:
        file_location = location + link.split("/")[-1]
        try:
            urllib.request.urlretrieve(link, file_location)
        except:
            print(f'Echec: Telecharger fichier au lien: {link}')


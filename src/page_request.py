import requests
from bs4 import BeautifulSoup
import lxml

def page_content(page_url : str):
    """
    Une fonction qui retourne le contenu beautifulsoup d'une page web en cas de cas succès et False au cas contraire

    :param page_url: le lien de la page web
    """

    response = requests.get(page_url)

    if response.status_code == 200:
        result = BeautifulSoup(response.text, 'lxml')
    else:
        result = False

    return result


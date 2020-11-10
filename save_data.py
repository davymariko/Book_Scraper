import pandas as pd
import requests


def save_data(data_list):

    # Create the pandas DataFrame
    df = pd.DataFrame(data_list, columns = ['Product Page Url', 'UPC', 'Title', 
        'Price Including Tax', 'Price Excluding Tax', 'Number Available',
        'Product Description', 'Category', 'Rating', 'Image Url'])
    
    # Save dataframe
    df.to_csv('Assets/File.csv') 


def save_image(image_url, name):
    response = requests.get(image_url)
    location = "Assets/Images/" + name + '.png'
    
    file = open(location, "wb")
    file.write(response.content)
    file.close()

if __name__ == "__main__":
    save_image("http://books.toscrape.com/media/cache/58/bb/58bb81b052b6ad90adcd57e95da99a50.jpg", "This book")
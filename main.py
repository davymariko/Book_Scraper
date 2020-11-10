
def this_function():
    print("Test this")

def that_function():
    print("Test that")
    

if __name__ == "__main__":
    print("Bienvenue à Bookscraper\n\nVeuillez faire un choix:")
    print("1. Avoir des données des livres par catégorie\n2. Avoir des données de tous les livres")

    key = int(input(""))

    if key == 1:
        this_function()
    elif key == 2:
        that_function()
    else:
        print("Wrong choice")
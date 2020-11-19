# Book_Scraper
Premier Projet de mon parcours DA-Python (OpenClassrooms)

## Description 
Le challenge est de scraper le site web [Book To Scrape](http://books.toscrape.com/) afin de tirer les informations nécessaires concernant chaque livre dans chaque catégorie. Les informations sont sauvergardées dans des fichiers csv (un par catégorie); Les images sont sauvegardées dans un dossier à part.

## Environnement
* L'installation de `Python 3` est nécessaire pour la réalisation de ce projet
* L'outil de développment utilisé et recommandé: `vscode`

## Installation
1. Cloner, en premier, le projet sur votre bureau ou environnement local
2. Installer les pre-requis pour ce projet en lançant la commande:
```bash
pip install -r requirements.txt
```

## Execution
Pour lancer le programme lancer le fichier 
```bash
python -m scrapper
```

## La Mission
** Fictif **

Un responsable d'équipe m'a chargé de développer une version bêta d'un système pour suivre les prix des livres chez [Books To Scrape](http://books.toscrape.com/), un revendeur de livres en ligne. En pratique, dans cette version bêta, mon programme n'effectuera pas une véritable surveillance en temps réel des prix sur la durée. Il s'agira simplement d'une application exécutable à la demande visant à récupérer les prix au moment de son exécution.

Plus de details sur la mission sur [OpenClassrooms](https://openclassrooms.com/en/paths/322/projects/832/assignment)

## Etapes
1. Scraper la page du site pour avoir les différentes catégories de livres
2. Itérer dans la liste diférentes catégories et créer une classe CategoryClass avec comme argument un lien vers une catégorie
3. A chaque iteration, on récupère des informations sur tous les livres de chaque catégorie
4. A chaque iteration, on sauvegarde les données des livres par catégorie dans des fichiers distincts et les images des livres visités dans un seul même dossier

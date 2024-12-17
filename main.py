from bs4 import BeautifulSoup

# Extraction des informations souhaitées avec Beautiful Soup
with open("index.html", "r") as file:
    soup = BeautifulSoup(file, "html.parser")

# Extraction du titre de la page
title = soup.title.string
print("Titre de la page:", title)

# Extraction du texte de la balise h1
h1_text = soup.find("h1").string
print("Texte de la balise h1:", h1_text)

# Dictionnaire pour stocker les produits
all_products = dict()

# Extraction des noms et des prix des produits dans la liste
products = soup.find_all("li")
for product in products:
    name = product.find("h2").string
    price_str = product.find("p", class_="price").string
    # On sépare la chaine avec " " en liste de mots
    price_list = price_str.split(" ")
    # On récupère le prix (= deuxième mot)
    all_products[name] = {"prix": price_list[1]}

# Extraction des descriptions des produits dans la liste
descriptions_list = []
for product in products:
    # La description eest le dernier élément de la liste des paragraphes
    description = product.find_all("p")[-1].string
    all_products[name]["description"] = description

# Affichage des informations extraites
print("Produits:", all_products)
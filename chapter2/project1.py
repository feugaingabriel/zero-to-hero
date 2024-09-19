# Initialisation des variables

name_article = "Ordinateur"
quantity = 78
price = 98.6


# Affichage
print("name_article", name_article)
print("quantite ", quantity)
print("price ", price)

# Mise a jour des articles(prix et quantite)

new_quantity = quantity + 90
new_price = price*0.2

# entree user avec conversion 
price_saisi = input("enter votre prix \n")

price_saisi = float(price_saisi)

name_article1 = "clavier"
name_article2 = "clavier"

print(name_article1 == name_article2)

print(name_article1 is name_article2)

print(id(name_article1))
print(id(name_article2))



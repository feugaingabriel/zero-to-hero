"""
# Les Operateurs en python

* Les operateurs permettent de realiser des operations sur des valeurs ou des variables. ils se classent en plusieurs categories:

### les operateurs arithmetiques:
<p>Ils permettent d'effectuer des operation de mathematique de base</p>

- Addition
- soustraction
- Multiplication
- Division (/)
- Division entiere (//)
- modulo (%)
- puissance(**)


"""


a = 10
b = 3
print("a+b = ", a+b)
print("a-b = ", a-b)
print("a*b = ", a*b)
print("a/b = ", a/b)
print("a//b = ", a//b)
print("a % b = ", a%b)
print("a**b = ", a**b)


"""

## Les operateurs logiques
<p>Ils permettent de faire des comparaisons logiques entre des expressions</p>

- Et (and) retourne True si les deux expressions sont vraie
- Ou (or) retourne True si au moins une des deux expressions est vraie
- Non (not): inverse la valeur logique de l'expression


"""


a = True
b = False
print(" a and b => ", a and b)
print(" a or b => ", a or b)
print(" not a => ",  not a)
print(" not b => ",  not b)


"""
## les operateurs d'affectations
<p>Ils permettent d'assigner des valeurs aux variables</p>
 
--> = assigne une valeur a la variable
--> += additionne et assigne
--> -= soustrait et assigne
--> *= multiplie et assigne
--> /= divise et assigne
--> %= effectue le modulo et assigne


"""

test = 24
test +=4 # son equivalence est :  test = test + 4
print(test)



test -=7 # son equivalence est test = test-7
print(test)

test *=3  # son equivalence est test = test*3
print(test)


"""
## Precedence et associativite des operateurs

La precedence d'un operateur determine l'ordre dans lequel les operations sont
effectuees. les operateurs avec une plus haute precedence sont evalues avant ceux avec un plus base.

"""


test_prioritaire = 6-8*5+5**2
print(test_prioritaire)


"""

## Associativite

<p>L'associativite determine l'ordre dans lequel les operateurs de meme precedence sont evalues.
 En generale python evalue les operateurs de gauche a droite (associativite a gauche). Ce pendant 
 pour certaines operateurs comme la puissance l'associativite est a droite</p>

"""

print(2**3**2)
# associativite a droite ==> 2**(3**2) = 2**9=512


"""

## Les objects Mutable et immutables

<p>En python les objects peuvent etre mutables ou immutable</p>

- Object Mutable: leurs valeurs peuvent etre modifiees apres leurs creation
- Object Immutable: leurs valeurs ne peuvent pas etre modifier apres leurs creations

1-  Object Mutable
<p>Exemple d'object mutable</p>

- Listes (list): les elements d'une liste peuvent etre modifiea.
- les dictionnaires (dict): Les valeurs d'un dictionnaires peuvent etre changees.

"""


my_list = [4,6,8]
print(my_list)
my_list[2]=7

print(my_list)



"""
### Objects Immutables

- Nombres entiers (int)
- chaines de caracteres (str)
- tuple (tuple)

"""

# nombre = 678
# nombre[1]=4
# print(nombre)
# chaine = "Python"
# chaine[3]=7
# print(chaine)



"""

## Operateurs is et id
- is: compare si deux objects sont les meme en memoire
- id(): retourne l'identifiant unique d'un object (adresse memoire)
"""


a = [1,2,3]
b=a
print(" a is b ==>", a is b)
print("id(a) = ", id(a))
print("id(b) = ", id(b))

c = [1,2,3]
print(" a == c -->", a==c)
print(" a is c -->", a is c)
print(" id(a) -->", id(a))
print(" id(c) -->", id(c))


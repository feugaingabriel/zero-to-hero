"""
    Les types de donnees fondamentaux
    -- 1- Les nombres(entiers, flottant, nbre complexe, operation(division, addition, soustraction, modulo, puissant **))

    -- 2 - Chaines de caracteres(
      definition =>  "..." , '...',
      operation => concatenation(+), repetition(*): repete une chaine de caracteres plusieurs, indexation([]),methode(len, split)

    )

    -- Booleens(
        operation: operateurs logique(not,or,and), comparaison( egalite==,different !=,inferieur <, superieur > inferieur ou egal <= et superieur ou egale >=)

    )

    -- None : representation de l'absence d'une valeur

"""

repetition = "je suis presse"

print(repetition*3)

indexation = "je suis pas ton egale"

print(indexation[-2])

methode = "j'apprends le python"

print(len(methode))


#### Conversion des types
## Il y a deux types de convertion (la conversion implicite: essaie automatiquement de convertir des types donnes compatible exple: int + float=>float), 

var_int = 78
var_float = 76.90
resultat = var_int + var_float
print("resultat ", resultat)

## la conversion explicite

print("resultat en utilisant le casting ", int(resultat))
x = 7

if x > 5:
    print("x est supérieur à 5")  # Cette ligne s'exécute
    if x % 2 == 0:
        print("x est pair")
    else:
        print("x est impair")  # Cette ligne s'exécute car 7 est impair


# valeur = valeur_si_vrai if condition else valeur_si_faux

age =17

status = "majeur" if age>=18 else "mineur"

print(status)


if age>=18:
    print("Majeur")
else:
    print("Mineur")
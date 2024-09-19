# initialisation de la variable

note_user = input("saisissez votre note compreise entre 0 et 100 \n")

note_user1 = float(note_user)
note_user1 = int(note_user1)
print(note_user1)



# validation de la note


if note_user1<0 or note_user1>100:
    print("Votre note doit etre superieura zero et inferieur = 100")
else:
    if note_user1 >=90 and note_user1<100:
        print("Excellent 😘😘😘😘😘")
    elif note_user1 >=80 and note_user1<90:
        print("Très bien")
    elif note_user1>=70 and note_user1<80:
        print("Bien")
    
    elif note_user1 >=60 and note_user1<70:
        print("Passable")
    elif note_user1>=50 and note_user1<60:
        print("Mediocre")
    
    # if note_user1 <50:
    else:
        print("Echec 😒😒")
    
    
        
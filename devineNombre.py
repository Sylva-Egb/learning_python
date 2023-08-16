from random import randint

vies = 3
nbr = randint(0,51)
print('----------------------------BIENVENU(E) DANS MON JEU DEVINE-MOI!--------------------------')
print('Le principe est tout bonnement simple. \nNous avons généré un nombre aléatoire qu\'il vous reviendra de deviner')
print('ATTENTION VOUS AVEZ 3 chances!')

while True:
    if vies == 3:
        print('Vous êtes à votre premier essai.\n')
    elif vies == 2:
        print(f'ATTENTION! il vous reste {vies} essai\n UN INDICE: Je suis un entier compris entre 0 et 50.\nSHUUUT! Ne le dites a personne\n')
    elif vies ==1:
        print(f"OUPS! On arrive aux portes du jeu.\nIl ne vous reste que {vies} essai.\n")
    choix = int(input("Entrez le nombre à deviner : "))
    if choix == nbr: 
        print("Bravo vous avez entré la bonne valeur\n")
        break
    elif choix < nbr:
        print("Vous avez entré une valeur en dessous du nombre à deviner\n")
    else:
        print("Vous avez entré une valeur au dessus du nombre à deviner\n")
    vies = vies-1
    if vies == 0:
        print(f"Vous avez perdu désolé. Le nombre était {nbr}")
        break
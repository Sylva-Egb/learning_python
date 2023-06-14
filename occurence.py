while True:
    mot = input("entrez votre mot/phrase(Vous pouvez aussi bien rentrer un paragraphe) :\n ")
    concur= input('entrez la lettre dont vous voulez connaitre l\'occurence : ')
    if(mot.count(concur)>0):
        print(f"La lettre/le mot ' {concur} ' se retrouve {mot.count(concur)} fois dans le mot/phrase/paragraphe")
    else:
        print(f"Aucune occurence de {concur}")
    choix = input("Voulez vous continuer o pour Oui n pour Non : ")

    if choix == 'n' or choix == 'N':
        break
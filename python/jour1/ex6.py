# ex_6 : Écrivez une fonction qui détecte toutes les dates au format JJ/MM/AAAA dans une
# chaîne de caractères et les retourne dans une liste.
# test : print(detecter_dates("Les dates importantes sont 12/05/2022 et 23/11/2023."))
# Output: ['12/05/2022', '23/11/2023']

def detecter_dates(chaine):

    date = "/".join(chaine.split()[-1].split("/"))
    print (date)
    
detecter_dates("Les dates importantes sont 12/05/2022 et 23/11/2023.")
# ex_2: Créez une fonction qui compte le nombre d'occurrences de chaque lettre dans une
# chaîne de caractères.
# test: print(compter_lettres("hello")) # Output: {'h': 1, 'e': 1, 'l': 2, 'o': 1}

def compter_lettres(chaine):
    
    lettres = {}

    for i in chaine:
        if i in lettres:
            lettres[i] += 1
        else:
            lettres[i] = 1

    print(str(lettres))
    
compter_lettres('hello')
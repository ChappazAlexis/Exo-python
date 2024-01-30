# Listes

# ex_7 : Écrire une fonction en Python qui prend une liste en entrée et retourne la liste
# inversée.
# test : print(inverser_liste([1, 2, 3, 4, 5])) # Affiche [5, 4, 3, 2, 1]

def inverser_liste(list):

    list.reverse()
    print(list)

inverser_liste([1,2,3,4,5])
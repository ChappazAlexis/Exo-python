# ex_8 : Écrire une fonction qui prend deux listes et renvoie une nouvelle liste contenant
# uniquement les éléments communs aux deux listes.
# test : print(elements_communs([1, 2, 3, 4], [2, 4, 6, 8])) # Affiche [2, 4]

def elements_communs(list1, list2):

    list1_set = set(list1)
    list2_set = set(list2)

    if (list1_set & list2_set):
        print(list1_set & list2_set)
    else:
        print("pas d'élément commun")

elements_communs([1,2,3,4,5],[1,3,5,7,9])
# ex_9 : Écrire une fonction qui compte combien de fois un élément apparaît dans une liste.
# test : print(compter_occurrences([1, 4, 2, 7, 4, 4, 3], 4)) # Affiche 3

def compter_occurrences(liste, element):
    
    occurrences = liste.count(element)
    print(occurrences)

compter_occurrences([1, 2, 3, 4, 5, 4, 4], 4)
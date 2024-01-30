# ex_21: Écrivez une fonction qui prend deux ensembles de nombres. La fonction doit
# retourner un nouvel ensemble qui est l'intersection des deux ensembles donnés, mais en
# éliminant tous les éléments qui sont des multiples de 3.
# set1 = {1, 2, 3, 4, 6, 9}
# set2 = {2, 3, 5, 6, 7, 9}
# print(intersection_without_multiples_of_three(set1, set2))
# {2}

set1 = {1, 2, 3, 4, 6, 9}
set2 = {2, 3, 5, 6, 7, 9}

set1.union(set2)

print (set1.union(set2))
# ex_13 : Écrivez une fonction max_min_moyenne qui prend un tuple de nombres et
# retourne un tuple contenant le maximum, le minimum et la moyenne des nombres. Testez
# cette fonction avec un tuple de votre choix.
# test : test_tuple = (10, 20, 30, 40, 50)
# resultat = max_min_moyenne(test_tuple)
# print("Max, Min, Moyenne:", resultat)

def max_min_moyenne(*args):

    size = len(args)

    maxi = max(args)
    mini = min(args)
    moy = sum(args) / size
    
    print (maxi)
    print (mini)
    print (moy)
    
max_min_moyenne(10,20,30,40,50)
# ex_12 : Essayez de modifier le troisième élément du tuple mon_tuple créé précédemment
# en une autre valeur, par exemple "python". Expliquez l'erreur, si elle se produit.

def mon_tuple():

    mon_tuple = (1, "chat", 3.14, True)
    mon_tuple[1] = "python"

    print (mon_tuple[2])
    
mon_tuple()

        # TypeError: 'tuple' object does not support item assignment
        # Ce n'est pas possible de modifier les valeurs d'un tuple après sa création.
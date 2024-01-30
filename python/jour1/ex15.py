# ex_15 : On vous donne une liste de tuples nommée data. Chaque tuple contient un
# identifiant unique sous forme de chaîne, un nombre, et une chaîne de caractères pouvant
# être soit "actif" soit "inactif". Par exemple : data = [("id1", 10, "actif"), ("id2", 15, "inactif"), ...].
# Votre tâche est de créer une fonction traiter_data qui effectue les opérations suivantes :
# Filtrez pour ne garder que les tuples où le statut est "actif".
# Triez les tuples filtrés par le nombre en ordre décroissant.
# Retournez une nouvelle liste de tuples, mais chaque tuple doit uniquement contenir
# l'identifiant et le nombre, sans le statut.

# test :
# # Test
# data = [("id1", 10, "actif"), ("id2", 15, "inactif"), ("id3", 20, "actif")]
# resultat = traiter_data(data)
# print(resultat)

# Dictionnaires (dict)
# ex_19: Vous avez deux dictionnaires, dictionnaire1 avec les clés "un", "deux", "trois" et leurs
# valeurs respectives 1, 2, 3, et dictionnaire2 avec les clés "quatre", "cinq", "six" et leurs
# valeurs 4, 5, 6. Fusionnez ces deux dictionnaires en un seul.

def merge(d1, d2):
    result = d1.copy()
    result.update(d2)
    return result

dic1 = {"un": 1, "deux": 2, "trois": 3}
dic2 = {"quatre": 4, "cinq": 5, "six": 6}

merged_dict = merge(dic1, dic2)
print(merged_dict)
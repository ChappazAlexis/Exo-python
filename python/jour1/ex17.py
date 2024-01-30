# ex_17: À partir du dictionnaire livre créé dans l'exercice 1, modifiez la valeur de l'année de
# publication à 1865. Ajoutez ensuite une nouvelle paire clé-valeur : genre avec la valeur
# "Roman".

livre = {"titre": "Les misérables", "auteur": "Victor Hugo", "date": 1862}

auteur_livre = livre["auteur"]
print(auteur_livre)

livre.update({"date": 1865})
livre.update({"genre": "roman"})

print (livre)
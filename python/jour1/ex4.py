# ex_4 : Créez une fonction qui remplace tous les espaces d'une chaîne par des tirets.
# test : print(remplacer_espaces("Bonjour le monde")) # Output: Bonjour-le-monde

def remplacer_espaces(chaine):
    
    sans_espace = chaine.replace(" ", "-")
    print(sans_espace)
    
remplacer_espaces('salut a tous')
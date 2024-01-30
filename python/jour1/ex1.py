# ex_1 :Écrivez une fonction en Python qui prend une chaîne de caractères en entrée et
# retourne la chaîne inversée.
# test : print(inverser_chaine("Bonjour")) # Output: ruojnoB

def inverser_chaine(chaine):
    reversed = chaine [::-1]
    print(reversed)
    
inverser_chaine('Bonjour')

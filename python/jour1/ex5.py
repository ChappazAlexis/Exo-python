# ex_5: Écrivez une fonction qui prend une chaîne de caractères et retourne le mot le plus
# long de cette chaîne.
# test : print(trouver_le_plus_long_mot("Le python est un excellent langage de
# programmation")) # Output: programmation

def plus_long(chaine):

    longest = ''
    for mot in chaine.split():
        if len(mot) > len(longest):
            longest = mot

    print(longest)
    
plus_long('python est un langage de programmation')
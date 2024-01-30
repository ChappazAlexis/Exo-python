# ex_3: Écrivez une fonction qui vérifie si une chaîne est un palindrome (se lit de la même
# façon dans les deux sens).
# test: print(est_palindrome("radar")) # Output: True
# print(est_palindrome("python")) # Output: False

def est_palindrome(chaine):
    
    reversed = chaine [::-1]

    if (reversed == chaine):
        print("palindrome")
    else:
        print("pas palindrome")
    
est_palindrome('radar')
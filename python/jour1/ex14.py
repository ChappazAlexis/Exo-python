# ex_14 : Créez une liste de tuples nommée étudiants, où chaque tuple contient le nom d'un
# étudiant et sa note (par exemple, ("Alice", 88)). Écrivez une fonction qui trie cette liste en
# fonction des notes des étudiants de manière décroissante.
# test :
# etudiants = [("Alice", 88), ("Bob", 95), ("Charlie", 78)]
# etudiants_tries = trier_etudiants(etudiants)
# print("Etudiants triés:", etudiants_tries)

def trier_etudiants(*etudiants):
    
    etudiants_tries = sorted(etudiants, key=lambda x: x[1], reverse=True)

    for etudiant in etudiants_tries:
        print(f"{etudiant[0]} {etudiant[1]}")

trier_etudiants(("Alice", 88), ("Bob", 95), ("Charlie", 78))
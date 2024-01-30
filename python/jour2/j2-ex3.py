import psutil

def memory():
    # Afficher l'utilisation de la mémoire
    memory_info = psutil.virtual_memory()
    print(f"\nMémoire : {memory_info.used / (1024 ** 2):.2f} Mo utilisés sur {memory_info.total / (1024 ** 2):.2f} Mo")

# Appel de la fonction
memory()

import random
from collections import Counter
import sys
#import networkx as nx 

# Définir le nombre de sommets dans le graphe
NOMBRE_DE_SOMMETS = 5

def generer_graphe_aleatoire():
    # Créer un dictionnaire pour la liste d'adjacence
    liste_dadjacence = {i: set() for i in range(1, NOMBRE_DE_SOMMETS + 1)}

    # Ajouter des sommets adjacents aléatoires pour chaque sommet
    for i in range(1, NOMBRE_DE_SOMMETS + 1):
        # Définir un nombre aléatoire de sommets voisins pour le sommet 'i'
        nb_sommets = random.randrange(1, NOMBRE_DE_SOMMETS)

        # Ajouter des voisins tant que le nombre de voisins est inférieur à nb_sommets
        while len(liste_dadjacence[i]) < nb_sommets:
            som_a_ajouter = random.randrange(1, NOMBRE_DE_SOMMETS + 1)

            # Éviter les boucles (éviter de connecter le sommet à lui-même) et éviter les doublons
            if som_a_ajouter != i and som_a_ajouter not in liste_dadjacence[i]:
                liste_dadjacence[i].add(som_a_ajouter)  # Ajouter l'adjacence du sommet actuel
                liste_dadjacence[som_a_ajouter].add(i)  # Ajouter l'adjacence inverse (bidirectionnelle)

    return liste_dadjacence


# Fonction pour afficher la liste d'adjacence d'un graphe
def afficher_liste_dadjacence(graphe):
    for i, voisins in graphe.items():
        print(f"Sommet {i} est relié à {', '.join(map(str, voisins))}")
        

        # Algorithme Bron-Kerbosch
def bron_kerbosch2(R, P, X, G):
    # Si P et X sont vides, alors R est une clique maximale
    if not P and not X:
        print("Clique maximale trouvée:", R)
        return

    # Choisir un pivot u dans P ∪ X (ici, on choisit un sommet parmi P ∪ X)
    u = next(iter(P.union(X)))

    # Pour chaque sommet v dans P \ N(u), on explore récursivement
    for v in list(P - set(G[u])):
        bron_kerbosch2(
            R.union([v]),
            P.intersection(G[v]),
            X.intersection(G[v]),
            G
        )
        # Mettre à jour P et X
        P.remove(v)
        X.add(v)


# Test Exemple d'utilisation sur un graphe aléatoire 
if __name__ == "__main__":
    # Test avec le graph aleatoire (fonction generer_graphe_aleatoire)
    G = generer_graphe_aleatoire()

    print("Graph ***********:")
    afficher_liste_dadjacence(G)

    # Initialisation des ensembles R, P et X
    P = set(G.keys())  # Tous les sommets du graphe sont candidats
    R = set()  # Aucune clique au départ
    X = set()  # Aucune exploration effectuée

    # Appel à l'algorithme Bron-Kerbosch2 avec pivot
    bron_kerbosch2(R, P, X, G)

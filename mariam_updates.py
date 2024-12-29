import graphlib
import random
from collections import Counter
import sys 
from igraph import Graph 
import pandas as pd 


NOMBRE_DE_SOMMETS = 5
PROBABILITE = 0.5


def generer_graphe_aleatoire():
    """    Générer la liste d'adjacence d'un graphe sous forme de dictionnaire. """

    liste_dadjacence = {i: [] for i in range(NOMBRE_DE_SOMMETS)}  # Initialisation de la liste d'adjacence

    # Ajouter des arêtes avec probabilité p
    for i in range(NOMBRE_DE_SOMMETS):
        for j in range(i + 1, NOMBRE_DE_SOMMETS):    # On évite les boucles
            if random.random() < PROBABILITE:
                liste_dadjacence[i].append(j)
                liste_dadjacence[j].append(i)  # Graphe non orienté

    return liste_dadjacence

def afficher_liste_dadjacence(graphe):
    """ Affiche la liste d'adjacence d'un graphe sous forme de dictionnaire. """

    for i in range(len(graphe)):
        print(f"Liste d'adjacence du sommet {i} est relié à : {graphe[i]}")

        #***************************graphe de Stanfort************************

def convertir_en_liste_dadjacence(graph):
    return {vertex.index: graph.neighbors(vertex.index) for vertex in graph.vs}

# Charger de graphe ego-Facebook
facebook_graphe = Graph.Read_Edgelist('facebook_combined.txt', directed=False)
# Charger de graphe email
email_graphe = Graph.Read_Edgelist('email-Eu-core.txt', directed=False)
# Charger graphe de lastfm
charger_fichire = pd.read_csv("lastfm_asia_edges.csv")
lastfm_graphe = Graph.DataFrame(charger_fichire, directed=False)

#debut de la partie 2 *********************************************************************


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
    GF = convertir_en_liste_dadjacence(facebook_graphe)
    GE = convertir_en_liste_dadjacence(email_graphe)
    GS = convertir_en_liste_dadjacence(lastfm_graphe)


    print("Graph ***********:")
    print(afficher_liste_dadjacence(G))
    print("************************fin de la liste ***********:")

    # Initialisation des ensembles R, P et X
    #P = set(G.keys())
    #P = set(GF.keys()) 
    #P = set(GE.keys()) 
    P = set(GS.keys())  # Tous les sommets du graphe sont candidats
    R = set()  # Aucune clique au départ
    X = set()  # Aucune exploration effectuée

    # Appel à l'algorithme Bron-Kerbosch2 avec pivot
   
    bron_kerbosch2(R, P, X, GS)

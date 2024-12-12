import random
from matplotlib import pyplot as plt
import pandas as pd
from igraph import Graph

# Définir le nombre de sommets dans le graphe
NOMBRE_DE_SOMMETS = 5
PROBABILITE = 0.5

import random

# _______________________________ Partie des graphes aléatoires _______________________________


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


def calculer_degre_max(graphe):
    """ Calcule le degré maximal dans un graphe """

    max_degre = 0
    # Parcours de chaque sommet et de sa liste de voisins
    for voisins in graphe.values():
        if len(voisins) > max_degre:
            max_degre = len(voisins)

    print("Le degré maximal du graphe est :", max_degre)


def grahique_occ_de_chaque_degre(graphe):
    """ Un graphique donnant pour chaque degré du graphe le nombre de sommets ayant ce degré  """

    degres = [len(voisins) for voisins in graphe.values()]  # Calcul des degrés pour chaque sommet

    # Trouver le degré maximal
    max_degre = max(degres)

    print("\nPour chaque degré du graphe le nombre de sommets ayant ce degré")

    for i in range(max_degre + 1):  # On affiche pour tous les degrés possibles
        print(f"Pour le degré {i} : {degres.count(i)} sommets")

        # Comptage des fréquences des degrés
        distribution = {}

    for degre in degres:
        distribution[degre] = distribution.get(degre, 0) + 1

    # Tracer le graphique
    plt.bar(distribution.keys(), distribution.values(), color='skyblue', edgecolor='black')
    plt.xlabel("Degré")
    plt.ylabel("Nombre de sommets")
    plt.title("Distribution des degrés dans le graphe")
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.show()


def nb_chemin_de_longueur2(graphe):
    """ Calcule le nombre de chemins de longueur 2 dans le graphe """
    cpt = 0
    for u in graphe:
        for v in graphe[u]:
            for w in graphe[v]:
                if w not in graphe[u] and w != u:
                    cpt += 1
    return cpt // 2  # On divise par 2 car chaque chemin est compté deux fois


# _______________________________ Partie des graphes aléatoires _______________________________

# Charger de graphe ego-Facebook
facebook_graphe = Graph.Read_Edgelist('facebook_combined.txt', directed=False)

# Charger de graphe email
email_graphe = Graph.Read_Edgelist('email-Eu-core.txt', directed=False)

# Charger graphe de lastfm
charger_fichire = pd.read_csv("lastfm_asia_edges.csv")
lastfm_graphe = Graph.DataFrame(charger_fichire, directed=False)


def calculer_degre_max_stanford(graphe):
    """" Cette fonction permet de renvoyer le dégré maximal d'un graphe de Stanfort"""
    degrees = graphe.degree()
    degre_max = max(degrees)
    return degre_max

import matplotlib.pyplot as plt

def nb_occ_de_chaque_degre_stanfort(graphe):
    degrees = graphe.degree()  # Liste des degrés de tous les nœuds
    plt.hist(degrees, bins=range(min(degrees), max(degrees)+1), edgecolor='black')  # Histogramme des degrés
    plt.title("Distribution des degrés")
    plt.xlabel("Degré")
    plt.ylabel("Nombre de nœuds")
    plt.show()

def nb_chemin_de_longeur2_stanfort(graphe):
    cpt = 0
    for u in graphe.vs:
        voisin_u = graphe.neighbors(u.index)
        for v in voisin_u:
            for w in graphe.neighbors(v):
                if u.index != w and not graphe.are_adjacent(u.index, w):  # Si u et w ne sont pas reliés directement
                    cpt += 1
    return cpt // 2  #On divise par 2 car chaque chemin est compté deux fois


#   _______________________________ DEUXIEME PARTIE _______________________________


def bron_kerbosch2(R, P, X, G):
    """ Algorithme Bron-Kerbosch """

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



if __name__ == "__main__" :

    graphe= generer_graphe_aleatoire()

    afficher_liste_dadjacence(graphe)
    # calculer_degre_max(graphe)
    grahique_occ_de_chaque_degre(graphe)
    #adjacency_list = [[1,4,2], [2, 1,3,5], [3, 2,4], [4,1,3], [5, 2]]
    #print("Nombre de chemins induits de longueur 2 :",nb_chemin_de_longueur2(graphe))

    #_____________2e_partie____________

    #P = set(graphe.keys())  # Tous les sommets du graphe sont candidats
    #R = set()  # Aucune clique au départ
    #X = set()  # Aucune exploration effectuée
    #bron_kerbosch2(R, P, X, graphe)



    pass

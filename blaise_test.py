import pandas as pd
from igraph import Graph

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

def nb_occ_de_chaque_degre_stanfort(graph):
    degrees = graph.degree()  # Liste des degrés de tous les nœuds
    plt.hist(degrees, bins=range(min(degrees), max(degrees)+1), edgecolor='black')  # Histogramme des degrés
    plt.title("Distribution des degrés")
    plt.xlabel("Degré")
    plt.ylabel("Nombre de nœuds")
    plt.show()

def nb_chemin_de_longeur2_stanfort(graph):
    cpt = 0
    for u in graph.vs:
        voisin_u = graph.neighbors(u.index)
        for v in voisin_u:
            for w in graph.neighbors(v):
                if u.index != w and not graph.are_adjacent(u.index, w):  # Si u et w ne sont pas reliés directement
                    cpt += 1
    return cpt // 2  #On divise par 2 car chaque chemin est compté deux fois


# Exemple d'utilisation
path_count = nb_chemin_de_longeur2_stanfort(facebook_graphe)
print(f"Nombre de chemins induits de longueur 2 dans le graphe Facebook : {path_count}")

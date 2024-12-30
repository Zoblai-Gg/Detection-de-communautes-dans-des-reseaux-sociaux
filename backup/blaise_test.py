import pandas as pd
from igraph import Graph

# Charger de graphe ego-Facebook
facebook_graphe = Graph.Read_Edgelist('facebook_combined.txt', directed=False)

# Charger de graphe email
email_graphe = Graph.Read_Edgelist('email-Eu-core.txt', directed=False)

# Charger graphe de lastfm
charger_fichire = pd.read_csv("../lastfm_asia_edges.csv")
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
#____________________________________3eme partie _____________________

def calculer_graphes_gi(graphe, ordre):
    """
    Calcule les graphes Gi selon l'ordre donné.
    :param graphe: Liste d'adjacence du graphe initial.
    :param ordre: Ordre des sommets (liste).
    :return: Liste des graphes Gi (liste de listes d'adjacence).
    """
    n = len(ordre)
    graphes_gi = []

    for i in range(n):
        # Conserver uniquement les sommets de {v_i, ..., v_n}
        sommets_restants = set(ordre[i:])
        graphe_gi = {v: [u for u in voisins if u in sommets_restants] for v, voisins in graphe.items() if v in sommets_restants}
        graphes_gi.append(graphe_gi)

    return graphes_gi


    # Étape 2 : Définir un ordre aléatoire des sommets
    #ordre = list(graphe.keys())
    #random.shuffle(ordre)
    #print("\nOrdre des sommets :", ordre)


def calculer_maximal_independent_sets(G, ordre):
    """
    Calcul de tous les ensembles indépendants maximaux pour chaque graphe Gi.
    :param G: Liste d'adjacence du graphe initial.
    :param ordre: Ordre des sommets.
    :return: Liste des ensembles indépendants maximaux pour chaque Gi.
    """
    n = len(ordre)
    graphes_gi = calculer_graphes_gi(G, ordre)  # Obtenir les Gi
    ensembles_independants = []

    for i, graphe_gi in enumerate(graphes_gi, start=1):
        print(f"\nEnsembles indépendants maximaux pour G_{i} (sommets {ordre[i-1:]}):")
        # Utiliser Bron-Kerbosch pour chaque Gi
        independants_gi = list(bron_kerbosch_independant(set(), set(graphe_gi.keys()), set(), graphe_gi))
        ensembles_independants.append(independants_gi)
        for independant in independants_gi:
            print(independant)

    return ensembles_independants

#-------------------------------------------------------------------

#fonctions pours grand graphes

def calculer_degre_max_stanford(graphe):
    """" Cette fonction permet de renvoyer le dégré maximal d'un graphe de Stanfort"""
    degrees = graphe.degree()
    degre_max = max(degrees)
    return degre_max

def nb_occ_de_chaque_degre_stanfort(graphe):

    # Liste des degrés de tous les nœuds
    degrees = graphe.degree()

    # Compter les occurrences de chaque degré
    occurrences = Counter(degrees)
    print("Occurrences des degrés :")
    for degre, count in sorted(occurrences.items()):
        print(f"Pour le degré {degre}: {count} sommets")

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



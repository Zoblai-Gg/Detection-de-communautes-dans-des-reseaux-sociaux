import random

# Définir le nombre de sommets dans le graphe
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


def convertir_en_liste_dadjacence(graph):
    return {vertex.index: graph.neighbors(vertex.index) for vertex in graph.vs}
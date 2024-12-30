from collections import Counter
from matplotlib import pyplot as plt

def calculer_degre_max(graphe):
    """ Calcule le degré maximal dans un graphe """

    max_degre = 0
    # Parcours de chaque sommet et de sa liste de voisins
    for voisins in graphe.values():
        if len(voisins) > max_degre:
            max_degre = len(voisins)

    return max_degre

def grahique_occ_de_chaque_degre(graphe):
    """ Un graphique donnant pour chaque degré du graphe le nombre de sommets ayant ce degré  """

    degres = [len(voisins) for voisins in graphe.values()]  # Calcul des degrés pour chaque sommet

    occurrences = Counter(degres)
    print("Occurrences des degrés :")
    for degre, count in sorted(occurrences.items()):
        print(f"Pour le degré {degre}: {count} sommets")


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


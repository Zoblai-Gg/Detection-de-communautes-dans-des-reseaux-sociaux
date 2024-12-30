from bron_kerbosch import bron_kerbosch_independant


def calculer_graphes_gi(graphe, ordre):
    """
    Calcule les graphes Gi selon l'ordre donné.

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

def calculer_ensembles_independants_maximaux(graphes_gi):
    """
    Calcule tous les ensembles indépendants maximaux pour chaque graphe Gi.

    :param graphes_gi: Liste des graphes Gi (liste de listes d'adjacence).
    :return: Liste des ensembles indépendants maximaux pour chaque Gi    """

    i = 0
    for Gi in graphes_gi:
        # Initialiser les ensembles R, P, et X
        R = set()  # Ensemble indépendant en construction
        P = set(Gi.keys())  # Tous les sommets de Gi
        X = set()  # Aucun sommet exclu au départ

        # Calculer les ensembles indépendants maximaux pour Gi
        i = i + 1
        print("Pour G{}",i)

        for ensemble in bron_kerbosch_independant(R, P, X, Gi):
            print(ensemble)
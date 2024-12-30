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

def bron_kerbosch_independant(R, P, X, G):
    """
            Variante de l'algorithme de Bron-Kerbosch pour les ensembles indépendants maximaux.

            :param R: Ensemble en cours de construction (indépendant).
            :param P: Ensemble des candidats potentiels à ajouter à R.
            :param X: Ensemble des sommets à exclure.
            :param G: Graphe sous forme de liste d'adjacence.
            :yield: Un ensemble indépendant maximal.       """

    if not P and not X:
        # Si P et X sont vides, R est un ensemble indépendant maximal
        yield R
        return

    # Choisir un pivot (un sommet parmi P ∪ X)
    u = next(iter(P.union(X)))

    # Pour chaque sommet v dans P \ N(u), explorer récursivement
    for v in list(P - set(G.get(u, []))):
        yield from bron_kerbosch_independant(
            R.union([v]),
            P.intersection(set(G.get(v, []))),
            X.intersection(set(G.get(v, []))),
            G
        )
        # Mettre à jour P et X
        P.remove(v)
        X.add(v)
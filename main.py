import random

from analyseGraphe import calculer_degre_max, grahique_occ_de_chaque_degre, nb_chemin_de_longueur2
from bron_kerbosch import bron_kerbosch2
from generationGraphe import generer_graphe_aleatoire, convertir_en_liste_dadjacence, afficher_liste_dadjacence
from stanford_graphs import calculer_graphes_gi, calculer_ensembles_independants_maximaux

import pandas as pd
from igraph import Graph

# Charger de graphe ego-Facebook
facebook_graphe = Graph.Read_Edgelist('facebook_combined.txt', directed=False)

# Charger de graphe email
email_graphe = Graph.Read_Edgelist('email-Eu-core.txt', directed=False)

# Charger graphe de lastfm
charger_fichire = pd.read_csv("lastfm_asia_edges.csv")
lastfm_graphe = Graph.DataFrame(charger_fichire, directed=False)


if __name__ == "__main__" :

    #=========================== PARTIE 1 DU PROJET ==========================
    print("===================== PARTIE GRAPHE ALEATOIRE (partie 1) =====================" )

    graphe= generer_graphe_aleatoire()
    afficher_liste_dadjacence(graphe)
    print("Le degré maximal du graphe est :", calculer_degre_max(graphe))
    grahique_occ_de_chaque_degre(graphe)
    # test à la main : graphe = [[1,4,2], [2, 1,3,5], [3, 2,4], [4,1,3], [5, 2]]
    print("Nombre de chemins induits de longueur 2 :",nb_chemin_de_longueur2(graphe))

    print("===================== PARTIE GRAPHE DE STANDFORD (partie 1) =====================" )

    facebook_graphe = convertir_en_liste_dadjacence(facebook_graphe)
    print("Le degré maximal du graphe est :", calculer_degre_max(facebook_graphe))
    grahique_occ_de_chaque_degre(facebook_graphe)
    print("Nombre de chemins induits de longueur 2 :", nb_chemin_de_longueur2(facebook_graphe))


    email_graphe = convertir_en_liste_dadjacence(email_graphe)
    print("Le degré maximal du graphe est :", calculer_degre_max(email_graphe))
    grahique_occ_de_chaque_degre(email_graphe)
    print("Nombre de chemins induits de longueur 2 :", nb_chemin_de_longueur2(email_graphe))


    lastfm_graphe = convertir_en_liste_dadjacence(lastfm_graphe)
    print("Le degré maximal du graphe est :", calculer_degre_max(lastfm_graphe))
    grahique_occ_de_chaque_degre(lastfm_graphe)
    print("Nombre de chemins induits de longueur 2 :", nb_chemin_de_longueur2(lastfm_graphe))

    #=========================== PARTIE 2 DU PROJET ==========================
    print("===================== PARTIE GRAPHE ALEATOIRE (partie 2) =====================" )

    R = set()  # Aucune clique au départ
    X = set()  # Aucune exploration effectuée

    P = set(graphe.keys())  # Tous les sommets du graphe sont candidats
    bron_kerbosch2(R, P, X, graphe)

    print("===================== PARTIE GRAPHE DE STANDFORD (partie 2) =====================" )
    print("résultats pour le graphe de facebook")
    P = set(facebook_graphe.keys())
    #bron_kerbosch2(R, P, X, facebook_graphe)

    print("résultats pour le graphe de email")
    P = set(email_graphe.keys())
    bron_kerbosch2(R, P, X, email_graphe)

    print("résultats pour le graphe de lastfm")
    P = set(lastfm_graphe.keys())
    bron_kerbosch2(R, P, X, lastfm_graphe)

    #=========================== PARTIE 3 DU PROJET ==========================
    print("===================== PARTIE GRAPHE ALEATOIRE (partie 3) =====================" )

    ordre = list(graphe.keys())
    random.shuffle(ordre)
    print("\nOrdre des sommets choisi aléatoirement :", ordre)
    graphes_Gi = calculer_graphes_gi(graphe,ordre)

    for i, graphe_gi in enumerate(graphes_Gi):
        print(f"G_{i + 1} (avec sommets {ordre[i:]}):")
        for sommet, voisins in graphe_gi.items():
            print(f"  {sommet}: {voisins}")

    print("===================== PARTIE GRAPHE DE STANDFORD (partie 3) =====================" )

    print("résultats pour le graphe de facebook (Non afficher lié à au nombre important de la liste )")

    ordre = list(facebook_graphe.keys())
    random.shuffle(ordre)
    print("\nOrdre des sommets choisi aléatoirement :", ordre)
    graphes_Gi_facebook = calculer_graphes_gi(facebook_graphe,ordre)



    print("résultats pour le graphe de email (Non afficher lié à au nombre important de la liste )")

    ordre = list(email_graphe.keys())
    random.shuffle(ordre)
    print("\nOrdre des sommets choisi aléatoirement :", ordre)
    graphes_Gi_email = calculer_graphes_gi(email_graphe,ordre)


    print("résultats pour le graphe de lastfm (Non afficher lié à au nombre important de la liste )")

    ordre = list(lastfm_graphe.keys())
    random.shuffle(ordre)
    print("\nOrdre des sommets choisi aléatoirement :", ordre)
    graphes_Gi_lastfm = calculer_graphes_gi(lastfm_graphe,ordre)

    #=========================== PARTIE 2 BONUS ==========================

    print("===================== PARTIE GRAPHE DE STANDFORD (Bonus) =====================" )

    print("Ensembles indépendants maximaux trouvés :\n")
    calculer_ensembles_independants_maximaux(graphes_Gi)

    print("===================== PARTIE GRAPHE DE STANDFORD (Bonus) =====================" )

    print("résultats pour le graphe de facebook")
    print("Ensembles indépendants maximaux trouvés :\n")
    calculer_ensembles_independants_maximaux(graphes_Gi_facebook)

    print("résultats pour le graphe de email")
    print("Ensembles indépendants maximaux trouvés :\n")
    calculer_ensembles_independants_maximaux(graphes_Gi_email)

    print("résultats pour le graphe de lastfm")
    print("Ensembles indépendants maximaux trouvés :\n")
    calculer_ensembles_independants_maximaux(graphes_Gi_lastfm)
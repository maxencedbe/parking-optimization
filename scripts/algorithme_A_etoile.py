from copy import deepcopy
import time

from heuristique import heuristique
from cout import cout, cout_actuel
from enfants_noeud import enfants_noeud

def algorithme_A_etoile(Noeud_de_depart, Voiture_cible):

    # Initialisation des données
    dimensions, k, Emplacements_voitures = Noeud_de_depart
    n, p = dimensions
    a, b = Voiture_cible
    temps_debut = time.time()

    # Délai maximal de recherche
    delai_max = 60*60

    # Indice permettant de retrouver la position de la voiture cible au sein des différents noeuds parcourus
    indice_voiture_cible = 0
    for i in range (len(Emplacements_voitures)):
        if Emplacements_voitures[i] == Voiture_cible:
            indice_voiture_cible = i

    # Liste contenant les noeuds à visiter ainsi que leur valeur de f correspondante, classés selon leur valeur par f
    Noeuds_a_visiter_poids = [(Noeud_de_depart, 0 + heuristique(Noeud_de_depart, indice_voiture_cible))]

    # Liste contenant les noeuds à visiter, classés selon leur valeur par f
    Noeuds_a_visiter = [Noeud_de_depart]

    # Liste contenant au fur et à mesure les noeuds déjà visités
    Noeuds_visites = []

    # Liste contenant les relations "père fils" entre les différents noeuds ainsi que le coût pour passer entre ces deux noeuds
    Relation_pere_fils=[]
    while Noeuds_a_visiter != []:

        # Vérification du délai d'exécution
        temps_ecoule = time.time()- temps_debut
        if temps_ecoule > delai_max:
            break

        # On choisit le noeud le plus prometteur
        Noeud_actuel = Noeuds_a_visiter_poids[0][0]

        # print('Noeud à visiter')
        # print(creer_parking(Noeud_actuel))
        # # print(temps_ecoule)
        # print()

        if Noeud_actuel[2][indice_voiture_cible] == (n*p-(p-1), n*p-(p-1)-p) or Noeud_actuel[2][indice_voiture_cible] == (n*p-(p-1)-p, n*p-(p-1)): # La voiture cible est située à la sortie
            return Noeuds_a_visiter_poids[0][1]

        else:
            Noeuds_visites.append(Noeud_actuel)

            # On génère les fils du noeud actuel
            Enfants = enfants_noeud(Noeud_actuel)
            for Fils in Enfants:
                if Fils not in Noeuds_a_visiter and Fils not in Noeuds_visites:
                    Relation_pere_fils.append((Noeud_actuel, Fils, cout(Noeud_actuel, Fils)))
                    f = cout_actuel(Noeud_de_depart, Fils, Relation_pere_fils) + heuristique(Fils, indice_voiture_cible)

                    # On place les différents fils du noeud actuel dans la liste des noeuds à visiter, en fonction de leur valeur par f
                    m = 0
                    while m < len(Noeuds_a_visiter_poids) and f >= cout_actuel(Noeud_de_depart, Noeuds_a_visiter_poids[m][0], Relation_pere_fils) + heuristique(Noeuds_a_visiter_poids[m][0], indice_voiture_cible):
                        m += 1
                    Noeuds_a_visiter_poids.insert(m, (Fils, cout_actuel(Noeud_de_depart, Fils, Relation_pere_fils) + heuristique(Fils, indice_voiture_cible)))
                    Noeuds_a_visiter.insert(m, Fils)

        # On retire le noeud actuel de la liste des noeuds à visiter
        Noeuds_a_visiter_poids.remove((Noeud_actuel, cout_actuel(Noeud_de_depart, Noeud_actuel, Relation_pere_fils) + heuristique(Noeud_actuel, indice_voiture_cible)))
        Noeuds_a_visiter.remove(Noeud_actuel)

    # Si aucun chemin n'a été trouvé c'est qu'on ne peut pas sortir la voiture de la disposition actuelle et on renvoie alors un coût arbitraire immense de telle sorte que ce parking ne soit jamais choisi lors de la sélection
    return 10**3

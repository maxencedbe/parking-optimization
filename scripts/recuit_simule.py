import random
import numpy as np

from time import time
from generer_aleatoire import generer_parking_aleatoire, generer_voisin_aleatoire
from cout_moyen import cout_moyen
from enfants_noeud import enfants_noeud
from creer_parking import creer_parking

def recuit_simule(n, p, k):

    # Initialisation des données
    temps_debut = time.time()
    temperature_initiale = 0
    cout_initial = 0
    Noeud_initial = generer_parking_aleatoire(n, p, k)
    cout_initial = cout_moyen(Noeud_initial)

    # Cas d'un parking où aucune voiture ne peut se déplacer
    while cout_initial == 10**3:
        Noeud_initial = generer_parking_aleatoire(n, p, k)
        cout_initial = cout_moyen(Noeud_initial)

    # Génération d'une température initiale
    for i in range (3):
        delta_cout = abs((cout_initial - cout_moyen(random.choice(enfants_noeud(Noeud_initial)))))
        if delta_cout > temperature_initiale:
            temperature_initiale = delta_cout
    temperature_initiale = temperature_initiale*10


    # Initialisation de la boucle
    temperature = temperature_initiale
    compteur_stagnation = 0
    Noeud_actuel = Noeud_initial

    # Application de l'algorithme
    while temperature > temperature_initiale*(0.9)**40:

        for i in range (10):

            # Stagnation
            if compteur_stagnation == 200:
                break

            # Génération d'un voisin
            Voisin = generer_voisin_aleatoire(Noeud_actuel)

            # Évaluation des solutions

            # print('Température ', temperature)
            # print('Coût noeud actuel', cout_noeud_actuel)
            # print(creer_parking(noeud_actuel))
            # print('Stagnation', compteur_stagnation)
            # print()

            cout_actuel = cout_moyen(Noeud_actuel)
            cout_voisin = cout_moyen(Voisin)
            while cout_voisin == 1000:
                Voisin = generer_voisin_aleatoire(Noeud_actuel)
                cout_voisin = cout_moyen(Voisin)
            delta_cout = cout_voisin - cout_actuel
            if delta_cout < 0:
                Noeud_actuel = Voisin
                compteur_stagnation = 0
            elif delta_cout == 0:
                compteur_stagnation += 1
            else:
                if np.exp(-delta_cout/temperature) > random.uniform(0,1):
                    Noeud_actuel = Voisin
                    compteur_stagnation = 0
                else:
                    compteur_stagnation += 1

        # Refroidissement
        temperature = 0.9*temperature

    temps = time.time()-temps_debut

    return creer_parking(Noeud_actuel), cout_actuel, temps
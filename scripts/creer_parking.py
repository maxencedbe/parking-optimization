import numpy as np

def creer_parking(Noeud):

    # Initialisation des données
    dimensions, k, Emplacements_Voitures = Noeud
    n, p = dimensions
    P = np.zeros((n, p))

    # Placement des voitures
    for Voiture in Emplacements_Voitures:
        a, b = Voiture
        q1, r1 = divmod(a, p)
        q2, r2 = divmod(b, p)

        # Avant de la voiture
        if r1 == 0:
            P[q1-1][p-1] = 2
        else:
            P[q1][r1-1] = 2

        # Arrière de la voiture
        if r2 == 0:
            P[q2-1][p-1] = 1
        else:
            P[q2][r2-1] = 1

    return P
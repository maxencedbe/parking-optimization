import numpy as np
import copy

from creer_parking import creer_parking

def enfants_noeud(Noeud):

    # Initialisation des données
    dimensions, k, Emplacements_voitures = Noeud
    n, p = dimensions
    Enfants = []
    P = creer_parking(Noeud)

    # Avancer
    for i in range (len(Emplacements_voitures)):
        a, b = Emplacements_voitures[i]
        q1, r1 = divmod(a, p)
        q2, r2 = divmod(b, p)

        if a == b-1:
            if r1 != 1:
                if P[q1][r1-2] == 0:
                    S = copy.deepcopy(Noeud)
                    S[2][i] = (a-1, b-1)
                    Enfants.append(S)
        if a == b+1:
            if r1 != 0:
                if P[q1][r1] == 0:
                    S = copy.deepcopy(Noeud)
                    S[2][i] = (a+1, b+1)
                    Enfants.append(S)
        if a == b-p:
            if r1 == 0:
                if q1 != 1:
                    if P[q1-2][p-1] == 0:
                        S = copy.deepcopy(Noeud)
                        S[2][i] = (a-p, b-p)
                        Enfants.append(S)
            else:
                if q1 != 0:
                    if P[q1-1][r1-1] == 0:
                        S = copy.deepcopy(Noeud)
                        S[2][i] = (a-p, b-p)
                        Enfants.append(S)
        if a == b+p:
            if r1 == 0:
                if q1 != n:
                    if P[q1][p-1] == 0:
                        S = copy.deepcopy(Noeud)
                        S[2][i] = (a+p, b+p)
                        Enfants.append(S)
            else:
                if q1 != n-1:
                    if P[q1+1][r1-1] == 0:
                        S = copy.deepcopy(Noeud)
                        S[2][i] = (a+p, b+p)
                        Enfants.append(S)

    # Reculer
    for i in range (len(Emplacements_voitures)):
        a, b = Emplacements_voitures[i]
        q1, r1 = divmod(a, p)
        q2, r2 = divmod(b, p)

        if a == b-1:
            if r2 == p-1:
                if P[q2][p-1] == 0:
                    S = copy.deepcopy(Noeud)
                    S[2][i] = (a+1, b+1)
                    Enfants.append(S)
            elif r2 != 0:
                if P[q2][r2] == 0:
                    S = copy.deepcopy(Noeud)
                    S[2][i] = (a+1, b+1)
                    Enfants.append(S)
        if a == b+1:
            if r2 != 1:
                if P[q2][r2-2] == 0:
                    S = copy.deepcopy(Noeud)
                    S[2][i] = (a-1, b-1)
                    Enfants.append(S)
        if a == b-p:
            if r2 == 0:
                if q2 != n:
                    if P[q2][p-1] == 0:
                        S = copy.deepcopy(Noeud)
                        S[2][i] = (a+p, b+p)
                        Enfants.append(S)

            else:
                if q2 != n-1:
                    if P[q2+1][r2-1] == 0:
                        S = copy.deepcopy(Noeud)
                        S[2][i] = (a+p, b+p)
                        Enfants.append(S)
        if a == b+p:
            if r2 == 0:
                if q2 != 1:
                    if P[q2-2][p-1] == 0:
                        S = copy.deepcopy(Noeud)
                        S[2][i] = (a-p, b-p)
                        Enfants.append(S)
            else:
                if q2 != 0:
                    if P[q2-1][r2-1] == 0:
                        S = copy.deepcopy(Noeud)
                        S[2][i] = (a-p, b-p)
                        Enfants.append(S)

    # Tourner avant droit
    for i in range (len(Emplacements_voitures)):
        a, b = Emplacements_voitures[i]
        q1, r1 = divmod(a, p)
        q2, r2 = divmod(b, p)

        if a == b-1:
            if r1 != 1 :
                if q1 >= 2:
                    if P[q1-1][r1-1] == 0 and P[q1][r1-2] == 0 and P[q1-1][r1-2] == 0 and P[q1-2][r1-2] == 0:
                        S = copy.deepcopy(Noeud)
                        S[2][i] = (a-1-2*p, b-2-p)
                        Enfants.append(S)

        if a == b+1:
            if r1 != 0:
                if q1 <= n-3:
                    if P[q1+1][r1-1] == 0 and P[q1][r1] == 0 and P[q1+1][r1] == 0 and P[q1+2][r1] == 0:
                        S = copy.deepcopy(Noeud)
                        S[2][i] = (a+1+2*p, b+2+p)
                        Enfants.append(S)
        if a == b-p:
            if q1 >= 1:
                if 1 <= r1 <= p-2:
                    if P[q1][r1] == 0 and P[q1-1][r1-1] == 0 and P[q1-1][r1] == 0 and P[q1-1][r1+1] == 0:
                        S = copy.deepcopy(Noeud)
                        S[2][i] = (a-p+2, b-2*p+1)
                        Enfants.append(S)
        if a == b+p:
            if r1 == 0:
                if q1 <= n-1:
                    if P[q1-1][p-2] == 0 and P[q1][p-1] == 0 and P[q1][p-2] == 0 and P[q1][p-3] == 0:
                        S = copy.deepcopy(Noeud)
                        S[2][i] = (a+p-2, b+2*p-1)
                        Enfants.append(S)
            elif r1 >= 3:
                if q1 <= n-2:
                    if P[q1][r1-2] == 0 and P[q1+1][r1-1] == 0 and P[q1+1][r1-2] == 0 and P[q1+1][r1-3] == 0:
                        S = copy.deepcopy(Noeud)
                        S[2][i] = (a+p-2, b+2*p-1)
                        Enfants.append(S)

    # Tourner avant gauche
    for i in range (len(Emplacements_voitures)):
        a, b = Emplacements_voitures[i]
        q1, r1 = divmod(a, p)
        q2, r2 = divmod(b, p)

        if a == b-1:
            if r1 != 1:
                if q1 <= n-3:
                    if P[q1+1][r1-1] == 0 and P[q1][r1-2] == 0 and P[q1+1][r1-2] == 0 and P[q1+2][r1-2] == 0:
                        S = copy.deepcopy(Noeud)
                        S[2][i] = (a-1+2*p, b-2+p)
                        Enfants.append(S)
        if a == b+1:
            if q1 >= 2:
                if 1<= r1 <= p-1:
                    if P[q1-1][r1-1] == 0 and P[q1][r1] == 0 and P[q1-1][r1] == 0 and P[q1-2][r1] == 0:
                        S = copy.deepcopy(Noeud)
                        S[2][i] = (a+1-2*p, b+2-p)
                        Enfants.append(S)
        if a == b-p:
            if r1 == 0:
                if q1 >= 2:
                    if P[q1-1][p-2] == 0 and P[q1-2][p-1] == 0 and P[q1-2][p-2] == 0 and P[q1-2][p-3] == 0:
                        S = copy.deepcopy(Noeud)
                        S[2][i] = (a-p-2, b-2*p-1)
                        Enfants.append(S)
            elif r1 >= 3:
                if q1 >= 1:
                    if P[q1][r1-2] == 0 and P[q1-1][r1-1] == 0 and P[q1-1][r1-2] == 0 and P[q1-1][r1-3] == 0:
                        S = copy.deepcopy(Noeud)
                        S[2][i] = (a-p-2, b-2*p-1)
                        Enfants.append(S)
        if a == b+p:
            if q1 <= n-2:
                if 1 <= r1 <= p-2:
                    if P[q1][r1] == 0 and P[q1+1][r1-1] == 0 and P[q1+1][r1] == 0 and P[q1+1][r1+1] == 0:
                        S = copy.deepcopy(Noeud)
                        S[2][i] = (a+p+2, b+2*p+1)
                        Enfants.append(S)

    # Tourner arrière droit
    for i in range (len(Emplacements_voitures)):
        a, b = Emplacements_voitures[i]
        q1, r1 = divmod(a, p)
        q2, r2 = divmod(b, p)

        if a == b-1:
            if q2 >= 2:
                if 1 <= r2 <= p-1:
                    if P[q2-1][r2-1] == 0 and P[q2][r2] == 0 and P[q2-1][r2] == 0 and P[q2-2][r2] == 0:
                        S = copy.deepcopy(Noeud)
                        S[2][i] = (a+2-p, b+1-2*p)
                        Enfants.append(S)
        if a == b+1:
            if q2 <= n-3:
                if r2 >= 2:
                    if P[q2+1][r2-1] == 0 and P[q2][r2-2] == 0 and P[q2+1][r2-2] == 0 and P[q2+2][r2-2] == 0:
                        S = copy.deepcopy(Noeud)
                        S[2][i] = (a-2+p, b-1+2*p)
                        Enfants.append(S)
        if a == b-p:
            if q2 <= n-2:
                if 1 <= r2 <= p-2:
                    if P[q2][r2] == 0 and P[q2+1][r2-1] == 0 and P[q2+1][r2] == 0 and P[q2+1][r2+1] == 0:
                        S = copy.deepcopy(Noeud)
                        S[2][i] = (a+2*p+1, b+p+2)
                        Enfants.append(S)
        if a == b+p:
            if r2 == 0:
                if q2 >= 2:
                    if P[q2-1][p-2] == 0 and P[q2-2][p-1] == 0 and P[q2-2][p-2] == 0 and P[q2-2][p-3] == 0:
                        S = copy.deepcopy(Noeud)
                        S[2][i] = (a-2*p-1, b-p-2)
                        Enfants.append(S)
            elif r2 >= 3:
                if q2 >= 1:
                    if P[q2][r2-2] == 0 and P[q2-1][r2-1] == 0 and P[q2-1][r2-2] == 0 and P[q2-1][r2-3] == 0:
                        S = copy.deepcopy(Noeud)
                        S[2][i] = (a-2*p-1, b-p-2)
                        Enfants.append(S)

    # Tourner arrière gauche
    for i in range (len(Emplacements_voitures)):
        a, b = Emplacements_voitures[i]
        q1, r1 = divmod(a, p)
        q2, r2 = divmod(b, p)

        if a == b-1:
            if q1 <= n-3:
                if r1 <= p-2:
                    if P[q1+1][r1] == 0 and P[q1][r1+1] == 0 and P[q1+1][r1+1] == 0 and P[q1+2][r1+1] == 0:
                        S = copy.deepcopy(Noeud)
                        S[2][i] = (a+2+p, b+1+2*p)
                        Enfants.append(S)
        if a == b+1:
            if q2 >= 2:
                if r2 >= 2:
                    if P[q2-1][r2-1] == 0 and P[q2][r2-2] == 0 and P[q2-1][r2-2] == 0 and P[q2-2][r2-2] == 0:
                        S = copy.deepcopy(Noeud)
                        S[2][i] = (a-2-p, b-1-2*p)
                        Enfants.append(S)
        if a == b-p:
            if r2 == 0:
                if q2 <= n-1:
                    if P[q2-1][p-2] == 0 and P[q2][p-1] == 0 and P[q2][p-2] == 0 and P[q2][p-3] == 0:
                        S = copy.deepcopy(Noeud)
                        S[2][i]=(a+2*p-1,b+p-2)
                        Enfants.append(S)
            elif r2 >= 3:
                if q2 <= n-2:
                    if P[q2][r2-2] == 0 and P[q2+1][r2-1] == 0 and P[q2+1][r2-2] == 0 and P[q2+1][r2-3] == 0:
                        S = copy.deepcopy(Noeud)
                        S[2][i] = (a+2*p-1, b+p-2)
                        Enfants.append(S)
        if a == b+p:
            if 1 <= r2 <= p-2:
                if q2 >= 1:
                    if P[q2][r2] == 0 and P[q2-1][r2-1] == 0 and P[q2-1][r2] == 0 and P[q2-1][r2+1] == 0:
                        S = copy.deepcopy(Noeud)
                        S[2][i] = (a-2*p+1, b-p+2)
                        Enfants.append(S)

    # Avancer avant droit
    for i in range (len(Emplacements_voitures)):
        a, b = Emplacements_voitures[i]
        q1, r1 = divmod(a, p)
        q2, r2 = divmod(b, p)

        if a == b-1:
            if q1 >= 1:
                if r1 >= 3:
                    if P[q1][r1-2] == 0 and P[q1-1][r1-1] == 0 and P[q1-1][r1-2] == 0 and P[q1-1][r1-3] == 0:
                        S = copy.deepcopy(Noeud)
                        S[2][i] = (a-2-p, b-2-p)
                        Enfants.append(S)
        if a == b+1:
            if 1 <= r1 <= p-2:
                if q1 <= n-2:
                    if P[q1][r1] == 0 and P[q1+1][r1-1] == 0 and P[q1+1][r1] == 0 and P[q1+1][r1+1] == 0:
                        S = copy.deepcopy(Noeud)
                        S[2][i] = (a+2+p, b+2+p)
                        Enfants.append(S)
        if a == b-p:
            if r1 != 0:
                if q1 >= 2:
                    if P[q1-1][r1-1] == 0 and P[q1][r1] == 0 and P[q1-1][r1] == 0 and P[q1-2][r1] == 0:
                        S = copy.deepcopy(Noeud)
                        S[2][i] = (a+1-2*p, b+1-2*p)
                        Enfants.append(S)
        if a == b+p:
            if r1 == 0:
                if q1 <= n-2:
                    if P[q1][p-1] == 0 and P[q1-1][p-2] == 0 and P[q1][p-2] == 0 and P[q1+1][p-2] == 0:
                        S = copy.deepcopy(Noeud)
                        S[2][i]=(a+2*p-1, b+2*p-1)
                        Enfants.append(S)
            elif r1 >= 2:
                if q1 <= n-3:
                    if P[q1+1][r1-1] == 0 and P[q1][r1-2] == 0 and P[q1+1][r1-2] == 0 and P[q1+2][r1-2] == 0:
                        S = copy.deepcopy(Noeud)
                        S[2][i] = (a+2*p-1,b+2*p-1)
                        Enfants.append(S)

    # Avancer avant gauche
    for i in range (len(Emplacements_voitures)):
        a, b = Emplacements_voitures[i]
        q1, r1 = divmod(a, p)
        q2, r2 = divmod(b, p)

        if a == b-1:
            if q1 <= n-2:
                if r1 >= 3:
                    if P[q1][r1-2] == 0 and P[q1+1][r1-1] == 0 and P[q1+1][r1-2] == 0 and P[q1+1][r1-3] == 0:
                        S = copy.deepcopy(Noeud)
                        S[2][i] = (a-2+p, b-2+p)
                        Enfants.append(S)
        if a == b+1:
            if 1 <= r1 <= p-2:
                if q1 >= 1:
                    if P[q1][r1] == 0 and P[q1-1][r1-1] == 0 and P[q1-1][r1] == 0 and P[q1-1][r1+1] == 0:
                        S = copy.deepcopy(Noeud)
                        S[2][i] = (a+2-p, b+2-p)
                        Enfants.append(S)
        if a == b-p:
            if r1 == 0:
                if q1 >= 3:
                    if P[q1-2][p-1] == 0 and P[q1-1][p-2] == 0 and P[q1-2][p-2] == 0 and P[q1-3][p-2] == 0:
                        S = copy.deepcopy(Noeud)
                        S[2][i] = (a-2*p-1, b-2*p-1)
                        Enfants.append(S)
            elif r1 >= 2:
                if q1 >= 2:
                    if P[q1-1][r1-1] == 0 and P[q1][r1-2] == 0 and P[q1-1][r1-2] == 0 and P[q1-2][r1-2] == 0:
                        S = copy.deepcopy(Noeud)
                        S[2][i] = (a-2*p-1, b-2*p-1)
                        Enfants.append(S)
        if a == b+p:
            if 1 <= r1 <= p-1:
                if q1<= n-3:
                    if P[q1+1][r1-1] == 0 and P[q1][r1] == 0 and P[q1+1][r1] == 0 and P[q1+2][r1] == 0:
                        S = copy.deepcopy(Noeud)
                        S[2][i] = (a+1+2*p, b+1+2*p)
                        Enfants.append(S)

    # Reculer arrière droit
    for i in range (len(Emplacements_voitures)):
        a, b = Emplacements_voitures[i]
        q1, r1 = divmod(a, p)
        q2, r2 = divmod(b, p)

        if a == b-1:
            if r1 <= p-3:
                if q1 >= 1:
                    if P[q1][r1+1] == 0 and P[q1-1][r1] == 0 and P[q1-1][r1+1] == 0 and P[q1-1][r1+2] == 0:
                        S = copy.deepcopy(Noeud)
                        S[2][i] = (a+2-p, b+2-p)
                        Enfants.append(S)
        if a == b+1:
            if r2 >= 3:
                if q2 <= n-2:
                    if P[q2][r2-2] == 0 and P[q2+1][r2-1] == 0 and P[q2+1][r2-1] == 0 and P[q2+1][r2-1] == 0:
                        S = copy.deepcopy(Noeud)
                        S[2][i] = (a-2+p, b-2+p)
                        Enfants.append(S)
        if a == b-p:
            if 1 <= r1 <= p-1:
                if q1 <= n-4:
                    if P[q1+2][r1-1] == 0 and P[q1+1][r1] == 0 and P[q1+2][r1] == 0 and P[q1+3][r1] == 0:
                        S = copy.deepcopy(Noeud)
                        S[2][i] = (a+2*p+1, b+2*p+1)
                        Enfants.append(S)
        if a == b+p:
            if r2 == 0:
                if q2 >= 3:
                    if P[q2-2][p-1] == 0 and P[q2-1][p-2] == 0 and P[q2-2][p-2] == 0 and P[q2-3][p-2] == 0:
                        S = copy.deepcopy(Noeud)
                        S[2][i] = (a-2*p-1,b-2*p-1)
                        Enfants.append(S)
            elif r2 >= 2:
                if q2 >= 2:
                    if P[q2-1][r2-1] == 0 and P[q2][r2-2] == 0 and P[q2-1][r2-2] == 0 and P[q2-2][r2-2] == 0:
                        S = copy.deepcopy(Noeud)
                        S[2][i] = (a-2*p-1, b-2*p-1)
                        Enfants.append(S)

    # Reculer arrière gauche
    for i in range (len(Emplacements_voitures)):
        a, b = Emplacements_voitures[i]
        q1, r1 = divmod(a, p)
        q2, r2 = divmod(b, p)

        if a == b-1:
            if q1 <= n-2:
                if r1 <= p-3:
                    if P[q1][r1+1] == 0 and P[q1+1][r1] == 0 and P[q1+1][r1+1] == 0 and P[q1+1][r1+2] == 0:
                        S = copy.deepcopy(Noeud)
                        S[2][i] = (a+2+p, b+2+p)
                        Enfants.append(S)
        if a == b+1:
            if r2 >= 3:
                if q2 >= 1:
                    if P[q2][r2-2] == 0 and P[q2-1][r2-1] == 0 and P[q2-1][r2-2] == 0 and P[q2-1][r2-3] ==0 :
                        S = copy.deepcopy(Noeud)
                        S[2][i] = (a-2-p, b-2-p)
                        Enfants.append(S)
        if a == b-p:
            if r2 == 0:
                if q2 <= n-2:
                    if P[q2][p-1] == 0 and P[q2-1][p-2] == 0 and P[q2][p-2] == 0 and P[q2+1][p-2] == 0:
                        S = copy.deepcopy(Noeud)
                        S[2][i] = (a+2*p-1, b+2*p-1)
                        Enfants.append(S)
            elif r2 >= 2:
                if q2 <= n-3:
                    if P[q2+1][r2-1] == 0 and P[q2][r2-2] == 0 and P[q2+1][r2-2] == 0 and P[q2+2][r2-2] == 0:
                        S = copy.deepcopy(Noeud)
                        S[2][i] = (a+2*p-1, b+2*p-1)
                        Enfants.append(S)
        if a == b+p:
            if r2 != 0:
                if q2 >= 2:
                    if P[q2-1][r2-1] == 0 and P[q2][r2] == 0 and P[q2-1][r2] == 0 and P[q2-2][r2] == 0:
                        S = copy.deepcopy(Noeud)
                        S[2][i] = (a-2*p+1, b-2*p+1)
                        Enfants.append(S)

    return Enfants
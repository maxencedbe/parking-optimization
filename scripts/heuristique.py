def heuristique(Noeud_de_depart, indice_voiture_cible):

    # Initialisation des données
    dimensions, k, Emplacements_voitures = Noeud_de_depart
    n, p = dimensions
    a, b = Emplacements_voitures[indice_voiture_cible]
    q1, r1 = divmod(a, p)
    q2, r2 = divmod(b, p)

    # Détermination du plus court chemin
    if a == b-1:
        if q1 < n-2:
            return abs(r1-2)+4+abs(n-(q1+1+2))
        else:
            return abs(r1-2)+4+abs(n-1-(q1+1-2))

    if a == b+1:
        if q2 < n-2:
            return abs(r2-2)+4+abs(n-(q2+1+2))
        else:
            return abs(r2-2)+4+abs(n-1-(q2+1-2))

    if a == b+p:
        if r1 == 1:
            return abs(n-(q1+1))
        elif r1 == 2:
            if q1 <= n-2:
                return 4+abs(n-(q1+1+2))
            elif q1 > n-2:
                return 4+abs(n-(q1+1-2))
        elif r1 == 3:
            if q1 <= n-3:
                return 4+abs(n-2-(q1+1+2))+4
            else:
                return 4+abs(n-2-(q1+1-2))+4
        elif r1 != 0:
            if q1 <= n-3:
                return 4+abs(2-(r1-2))+4+abs(n-(q1+1+3))
            else:
                return 4+abs(2-(r1-2))+4+abs(n-(q1+1))
        else:
            if n == 4:
                return 4+4+abs(n-q1)
            else:
                if q1-1 <= n-3:
                    return 4+abs(2-(p-2))+4+abs(n-(q1+3))
                else:
                    return 4+abs(2-(p-2))+4+abs(n-q1)

    if a == b-p:
        if r2 == 1:
            return abs((n-1)-q2)
        elif r2 == 2:
            if q2 <= n-2:
                return 4+abs(n-(q2+1+2))
            elif q2 > n-2:
                return 4+abs(n-(q2+1-2))
        elif r2 == 3:
            if q2 <= n-3:
                return 4+abs(n-2-(q2+1+2))+4
            else:
                return 4+abs(n-2-(q2+1-2))+4
        elif r2 != 0:
            if q2 <= n-3:
                return 4+abs(2-(r2-2))+4+abs(n-(q2+1+3))
            else:
                return 4+abs(2-(r2-2))+4+abs(n-(q2+1))
        else:
            if n == 4:
                return 4+4+abs(n-q2)
            else:
                if q2-1 <= n-3:
                    return 4+abs(2-(p-2))+4+abs(n-(q2+3))
                else:
                    return 4+abs(2-(p-2))+4+abs(n-q2)
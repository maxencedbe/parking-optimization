def cout(Noeud_1, Noeud_2):

    # Initialisation des données
    dimensions, k, Emplacements_voitures_1 = Noeud_1
    dimensions, k, Emplacements_voitures_2 = Noeud_2
    n, p = dimensions

    # Indice de la voiture qui s'est déplacée
    i0 = 0
    for i in range (len(Emplacements_voitures_1)):
        if Emplacements_voitures_1[i] != Emplacements_voitures_2[i]:
            i0 = i

    # Position de la voiture dans chaque parking
    a1, b1 = Emplacements_voitures_1[i0]
    a2, b2 = Emplacements_voitures_2[i0]

    # Cas où la voiture ne s'est pas déplacée
    if a2 == a1 and b2 == b1:
        return 0

    # Autres cas
    if a1 == b1-1:
        if a2 == a1-1 and b2 == b1-1:
            return 1
        if a2 == a1+1 and b2 ==b1+1:
            return 1
        else:
            return 4

    if a1 == b1+1:
        if a2 == a1+1 and b2 == b1+1:
            return 1
        if a2 == a1-1 and b2 == b1-1:
            return 1
        else:
            return 4

    if a1 == b1-p:
        if a2 == a1-p and b2 == b1-p:
            return 1
        if a2 == a1+p and b2 == b1+p:
            return 1
        else:
            return 4

    if a1 == b1+p:
        if a2 == a1+p and b2 == b1+p:
            return 1
        if a2 == a1-p and b2 == b1-p:
            return 1
        else:
            return 4
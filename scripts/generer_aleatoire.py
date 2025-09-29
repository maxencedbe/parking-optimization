import random

from enfants_noeud import enfants_noeud

def generer_parking_aleatoire(n, p, k):

    # Initialisation des données
    Emplacements_voitures = []

    # Génération d'emplacements aléatoires
    while len(Emplacements_voitures) != k:

        a = random.randint(1, n*p)

        if a//p == 0:
            if a%p == 1:
                b = random.choice((a+1, a+p))
            elif a%p == 0:
                b = random.choice((a-1, a+p))
            else:
                b = random.choice((a+1, a-1, a+p))

        elif a//p == p-1:
            if a%p == 1:
                b = random.choice((a+1, a-p))
            elif a%p == 0:
                b = random.choice((a-1, a-p))
            else:
                b = random.choice((a+1, a-1, a-p))

        elif a%p == 1:
            if a//p == 0:
                b = random.choice((a+1, a+p))
            elif a//p == p-1:
                b = random.choice((a+1, a-p))
            else:
                b = random.choice((a+1, a+p, a-p))

        elif a%p == 0:
            if a//p == 1:
                b = random.choice((a-1, a+p))
            elif a//p == p:
                b = random.choice((a-1, a-p))
            else:
                b = random.choice((a-1, a+p, a-p))

        else:
            b = random.choice((a+1, a-1, a+p, a-p))

        # Vérification de colisions
        test = True
        for Voiture in Emplacements_voitures:
            if a == Voiture[0] or a == Voiture[1] or b == Voiture[0] or b == Voiture[1]:
                test = False
        if test == True:
            Emplacements_voitures.append((a, b))

    return [(n, p), k, Emplacements_voitures]


def generer_voisin_aleatoire(Noeud):

    Enfants = enfants_noeud(Noeud)
    voisin_aleatoire = random.choice(Enfants)

    return voisin_aleatoire
from numpy import random

from enfants_noeud import enfants_noeud

def generer_voisin_aleatoire(Noeud):

    Enfants = enfants_noeud(Noeud)
    voisin_aleatoire = random.choice(Enfants)

    return voisin_aleatoire
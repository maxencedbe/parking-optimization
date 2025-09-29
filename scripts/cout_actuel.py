from cout import cout

def cout_actuel(Noeud_de_depart, Noeud_actuel, Relation_pere_fils):

    # Initialisation des données
    c = 0
    Noeud = Noeud_actuel

    # Calcul du poids
    while Noeud != Noeud_de_depart:
        for elt in Relation_pere_fils:
            if elt[1] == Noeud :
                Noeud = elt [0]
                c += elt[2]
    c += cout(Noeud_de_depart, Noeud)

    return c
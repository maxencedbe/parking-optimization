from algorithme_A_etoile import algorithme_A_etoile

def cout_moyen(Noeud):

    # Initialisation des données
    dimensions, k, Emplacements_voitures = Noeud
    n, p = dimensions
    c = 0
    c_moy = 0

    # Cas où le nombre de voitures annoncé ne correspond pas au nombre de voitures présentes dans le parking
    if k != len(Emplacements_voitures):
        print ('Erreur : le nombre de voitures annoncé ne correspond pas aux nombres de voitures présentes dans le parking.')
        return None

    # Calcul du coût total
    for Voiture in Emplacements_voitures:
        c += algorithme_A_etoile(Noeud, Voiture)

    # Calcul du coût moyen
    c_moy = c / k

    return c_moy
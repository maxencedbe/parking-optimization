import pygame

def dessiner_parking(Noeud):

    # Initialisation des données
    dimensions, nb_voitures, Emplacements_voitures = Noeud
    n, p = dimensions

    # Initialisation de pygame
    pygame.init()

    # Définition des dimensions de la fenêtre
    largeur_fenetre = p * 100
    hauteur_fenetre = n * 100
    taille_fenetre = (largeur_fenetre, hauteur_fenetre)

    # Création de la fenêtre
    fenetre = pygame.display.set_mode(taille_fenetre)

    # Définition des couleurs
    couleur_case = (255, 255, 255)
    couleur_bord = (0, 0, 0)
    couleur_voiture = (197, 153, 117)
    couleur_symbole = (0, 0, 0)

    while True:
        # Gestion des événements
        for evenement in pygame.event.get():
            if evenement.type == pygame.QUIT:
                pygame.quit()
                return

        # Effacement de la fenêtre
        fenetre.fill(couleur_bord)

        # Dessin de la grille
        for i in range(n):
            for j in range(p):
                pygame.draw.rect(fenetre, couleur_case, (j*100+1, i*100+1, 98, 98))

        # Dessin des bordures
        for i in range(n+1):
            pygame.draw.line(fenetre, couleur_bord, (0, i*100), (largeur_fenetre, i*100), 1)
        for i in range(p+1):
            pygame.draw.line(fenetre, couleur_bord, (i*100, 0), (i*100, hauteur_fenetre), 1)

        # Dessin des voitures
        for voiture in Emplacements_voitures:
            a, b = voiture
            q1, r1 = divmod(a-1, p)
            q2, r2 = divmod(b-1, p)

            # Détermination du sens de la voiture
            if r1 == r2: # voiture verticale
                debut, fin = min(q1, q2), max(q1, q2)
                pygame.draw.rect(fenetre, couleur_voiture, (r1*100+1, debut*100+1, 98, 100))
                pygame.draw.rect(fenetre, couleur_voiture, (r1*100+1, (debut+1)*100+1, 98, 98))
            else: # voiture horizontale
                debut, fin = min(r1, r2), max(r1, r2)
                pygame.draw.rect(fenetre, couleur_voiture, (debut*100+1, q1*100+1, 100, 98))
                pygame.draw.rect(fenetre, couleur_voiture, ((debut+1)*100+1, q1*100+1, 98, 98))

            # Dessin du symbole sur la case représentant le devant de la voiture
            pygame.draw.circle(fenetre, couleur_symbole, ((r1*100)+50, (q1*100)+50), 10)

        # Actualisation de la fenêtre
        pygame.display.flip()
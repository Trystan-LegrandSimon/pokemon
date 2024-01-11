import pygame
import sys

# Initialisation de Pygame
pygame.init()

# Couleurs
BLANC = (255, 255, 255)
NOIR = (0, 0, 0)
GRIS = (169, 169, 169)

# Dimensions de la fenêtre
largeur, hauteur = 800, 600

# Création de la fenêtre
ecran = pygame.display.set_mode((largeur, hauteur))
pygame.display.set_caption("Fenêtre Stylée")

# Chargement de l'image de fond
fond = pygame.image.load('app/assets/assets_menu/backgmenu.png')  # Remplacez 'background_image.jpg' par le chemin de votre image
fond = pygame.transform.scale(fond, (largeur, hauteur))

# Positionnement des boutons
bouton_largeur, bouton_hauteur = 200, 50
espace_entre_boutons = 10

# Coordonnées du premier bouton (centré horizontalement)
x_bouton1 = (largeur - bouton_largeur) // 2
y_bouton1 = (hauteur - (3 * bouton_hauteur + 2 * espace_entre_boutons)) // 2

# Boucle principale
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Dessiner l'image de fond
    ecran.blit(fond, (0, 0))

    # Dessiner les boutons
    pygame.draw.rect(ecran, BLANC, (x_bouton1, y_bouton1, bouton_largeur, bouton_hauteur))
    pygame.draw.rect(ecran, BLANC, (x_bouton1, y_bouton1 + bouton_hauteur + espace_entre_boutons, bouton_largeur, bouton_hauteur))
    pygame.draw.rect(ecran, BLANC, (x_bouton1, y_bouton1 + 2 * (bouton_hauteur + espace_entre_boutons), bouton_largeur, bouton_hauteur))

    # Mise à jour de l'affichage
    pygame.display.flip()

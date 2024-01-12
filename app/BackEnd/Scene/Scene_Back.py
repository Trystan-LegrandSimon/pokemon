import pygame
import sys

# Initialisation de Pygame
pygame.init()

# Couleurs
BLANC = (255, 255, 255)
NOIR = (0, 0, 0)
GRIS = (169, 169, 169)

# Dimensions de la fenêtre
largeur, hauteur = 1520, 825

# Création de la fenêtre
ecran = pygame.display.set_mode((largeur, hauteur))
pygame.display.set_caption("Arène Pokémon")

# Chargement de l'image de fond
fond = pygame.image.load('app/assets/assets_scene/backcombat.png')
fond = pygame.transform.scale(fond, (largeur, hauteur))

# Classe Pokémon
class Pokemon(pygame.sprite.Sprite):
    def __init__(self, image, x, y, largeur, hauteur):
        super().__init__()
        self.image = pygame.image.load(image)
        self.image = pygame.transform.scale(self.image, (largeur, hauteur))
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)  # Utiliser center au lieu de x, y

    def afficher(self):
        ecran.blit(self.image, self.rect)

# Taille réduite du Pokémon
pokemon_largeur, pokemon_hauteur = 225, 225

# Position initiale du Pokémon
position_initiale = (largeur // 2 + 145, hauteur // 2 - 200)

# Initialiser le Pokémon à la position initiale
pokemon = Pokemon('app/assets/assets_pokemon/bulbizarre.png', *position_initiale, pokemon_largeur, pokemon_hauteur)

# Boucle principale
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Dessiner l'image de fond
    ecran.blit(fond, (0, 0))

    # Dessiner le Pokémon
    pokemon.afficher()

    # Mise à jour de l'affichage
    pygame.display.flip()
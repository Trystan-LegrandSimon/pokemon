import pygame
import sys
import os
import random

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

# Dossier des Pokémon
dossier_pokemon = 'app/assets/assets_pokemon'

# Liste de tous les fichiers dans le dossier des Pokémon
fichiers_pokemon = [f for f in os.listdir(dossier_pokemon) if os.path.isfile(os.path.join(dossier_pokemon, f.lower()))]

# Choisir un Pokémon au hasard parmi les fichiers
fichier_pokemon1 = random.choice(fichiers_pokemon)

# Position initiale du Pokémon 1
position_initiale_pokemon1 = (largeur // 2 + 145, hauteur // 2 - 200)

# Initialiser le Pokémon 1 avec l'image choisie
pokemon1 = Pokemon(os.path.join(dossier_pokemon, fichier_pokemon1.lower()), *position_initiale_pokemon1, pokemon_largeur, pokemon_hauteur)

# Position initiale du Pokémon 2
position_initiale_pokemon2 = (largeur // 2 - 250, hauteur // 2 + 100)

# Initialiser le Pokémon 2 avec une image fixe (par exemple, carapuce.png)
pokemon2 = Pokemon('app/assets/assets_pokemon_inverse/carapuce.png', *position_initiale_pokemon2, pokemon_largeur, pokemon_hauteur)

# Boucle principale
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Dessiner l'image de fond
    ecran.blit(fond, (0, 0))

    # Dessiner les Pokémon
    pokemon1.afficher()
    pokemon2.afficher()

    # Mise à jour de l'affichage
    pygame.display.flip()

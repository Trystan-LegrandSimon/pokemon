import pygame
import sys
import os
import random
import json

# Initialisation de Pygame
pygame.init()

# Couleurs
BLANC = (255, 255, 255)
NOIR = (0, 0, 0)
GRIS = (169, 169, 169)

# Dimensions de la fenêtre
largeur, hauteur = 1520, 825

# Classe Pokémon
class Pokemon(pygame.sprite.Sprite):
    def __init__(self, image, x, y, largeur, hauteur, nom, evolution, pv):
        super().__init__()
        self.image = pygame.image.load(image)
        self.image = pygame.transform.scale(self.image, (largeur, hauteur))
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.nom = nom
        self.evolution = evolution
        self.pv = pv

    def afficher(self, ecran):
        ecran.blit(self.image, self.rect)

# Classe pour traiter les données du JSON
class PokemonData:
    def __init__(self, json_file):
        with open(json_file, 'r') as file:
            data = json.load(file)
            self.pokemon_data = data["pokemon"]

    def get_random_pokemon(self):
        pokemon_info = random.choice(self.pokemon_data)
        return pokemon_info

# Dossier des Pokémon
dossier_pokemon = 'app/assets/assets_pokemon'

# Obtention des informations d'un Pokémon au hasard
pokemon_info = PokemonData('app/data/pokemon.json').get_random_pokemon()

# Position initiale du Pokémon
position_initiale_pokemon = (largeur // 2 + 145, hauteur // 2 - 200)

# Initialiser le Pokémon avec les informations du JSON
pokemon = Pokemon(
    os.path.join(dossier_pokemon, pokemon_info["asset"]),
    *position_initiale_pokemon,
    225,
    225,
    pokemon_info["nom"],
    pokemon_info["evolution"],
    pokemon_info["pv"]
)

# Création de la fenêtre principale du combat
ecran = pygame.display.set_mode((largeur, hauteur))
pygame.display.set_caption("Arène Pokémon")

# Chargement de l'image de fond
fond = pygame.image.load('app/assets/assets_scene/backcombat.png')
fond = pygame.transform.scale(fond, (largeur, hauteur))

# Police pour les informations
police_info = pygame.font.Font(None, 24)

# Classe Bouton
class Bouton:
    def __init__(self, x, y, largeur, hauteur, couleur, texte, action):
        self.rect = pygame.Rect(x, y, largeur, hauteur)
        self.couleur = couleur
        self.texte_surface = None  # Initialiser à None pour l'instant
        self.action = action

        # Convertir le texte en surface dès la création du bouton
        self.maj_texte(texte)

    def maj_texte(self, texte):
        self.texte_surface = police_info.render(texte, True, BLANC)

    def afficher(self, ecran):
        pygame.draw.rect(ecran, self.couleur, self.rect)

        # Vérifier si la surface de texte existe
        if self.texte_surface:
            self.afficher_texte(ecran, self.texte_surface, self.rect.centerx, self.rect.centery, BLANC)

    def afficher_texte(self, ecran, texte_surface, x, y, couleur):
        ecran.blit(texte_surface, (x - texte_surface.get_width() / 2, y - texte_surface.get_height() / 2))

# Création des boutons
bouton1 = Bouton(200, hauteur - 100, 150, 40, (255, 0, 0), "Attaque", None)
bouton2 = Bouton(400, hauteur - 100, 150, 40, (0, 255, 0), "Défense", None)

# Boucle principale
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            if bouton1.rect.collidepoint(x, y):
                print("Clic sur Bouton 1")
                # Ajoutez ici l'action que vous voulez exécuter pour le Bouton 1
            elif bouton2.rect.collidepoint(x, y):
                print("Clic sur Bouton 2")
                # Ajoutez ici l'action que vous voulez exécuter pour le Bouton 2

    # Dessiner l'image de fond
    ecran.blit(fond, (0, 0))

    # Dessiner le Pokémon
    pokemon.afficher(ecran)

    # Dessiner les boutons
    bouton1.afficher(ecran)
    bouton2.afficher(ecran)

    # Afficher les informations du Pokémon
    nom_texte_surface = police_info.render(f"Nom: {pokemon.nom}", True, BLANC)
    evolution_texte_surface = police_info.render(f"Évolution: {pokemon.evolution}" if pokemon.evolution else "Évolution: Aucune", True, BLANC)
    pv_texte_surface = police_info.render(f"PV: {pokemon.pv}", True, BLANC)

    ecran.blit(nom_texte_surface, (300, 20))
    ecran.blit(evolution_texte_surface, (300, 40))
    ecran.blit(pv_texte_surface, (300, 60))

    # Mise à jour de l'affichage
    pygame.display.flip()

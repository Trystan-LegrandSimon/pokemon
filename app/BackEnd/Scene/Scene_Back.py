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

    def get_pokemon_by_name(self, name):
        for pokemon_info in self.pokemon_data:
            if pokemon_info["nom"] == name:
                return pokemon_info
        return None

# Dossier des Pokémon
dossier_pokemon = 'app/assets/assets_pokemon'

# Chargement des images miniatures et création des rectangles associés
images_miniatures = []
rects_miniatures = []
for pokemon_info in PokemonData('app/data/pokemon.json').pokemon_data:
    image_miniature = pygame.image.load(os.path.join(dossier_pokemon, pokemon_info["asset"]))
    image_miniature = pygame.transform.scale(image_miniature, (50, 50))
    images_miniatures.append(image_miniature)
    rects_miniatures.append(image_miniature.get_rect())

# Sélection du Pokémon
def selection_pokemon():
    ecran_selection = pygame.display.set_mode((largeur, hauteur))
    pygame.display.set_caption("Sélection du Pokémon")

    # Afficher les miniatures des Pokémon
    choix_pokemon = None
    while not choix_pokemon:
        ecran_selection.fill(GRIS)

        for i, (image_miniature, rect_miniature) in enumerate(zip(images_miniatures, rects_miniatures)):
            rect_miniature.center = (largeur // 2, 50 * (i + 1))
            ecran_selection.blit(image_miniature, rect_miniature)

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                for rect_miniature, pokemon_info in zip(rects_miniatures, PokemonData('app/data/pokemon.json').pokemon_data):
                    if rect_miniature.collidepoint(x, y):
                        choix_pokemon = pokemon_info
                        break

    return choix_pokemon

# Obtention des informations d'un Pokémon au hasard
pokemon_data = PokemonData('app/data/pokemon.json')

# Sélection du premier Pokémon
pokemon_info_1 = selection_pokemon()

# Position initiale du premier Pokémon
position_initiale_pokemon_1 = (largeur // 2 - 250, hauteur // 2 + 75)

# Initialiser le premier Pokémon avec les informations du JSON
pokemon_1 = Pokemon(
    os.path.join(dossier_pokemon, pokemon_info_1["asset"]),
    *position_initiale_pokemon_1,
    225,
    225,
    pokemon_info_1["nom"],
    pokemon_info_1["evolution"],
    pokemon_info_1["pv"]
)

# Création de la fenêtre principale du combat
ecran_combat = pygame.display.set_mode((largeur, hauteur))
pygame.display.set_caption("Arène Pokémon")

# Chargement de l'image de fond
fond_combat = pygame.image.load('app/assets/assets_scene/backcombat.png')
fond_combat = pygame.transform.scale(fond_combat, (largeur, hauteur))

# Position initiale du deuxième Pokémon
position_initiale_pokemon_2 = (largeur // 2 + 200, hauteur // 2 - 200)

# Obtention des informations du deuxième Pokémon au hasard
pokemon_info_2 = pokemon_data.get_random_pokemon()

# Initialiser le deuxième Pokémon avec les informations du JSON
pokemon_2 = Pokemon(
    os.path.join(dossier_pokemon, pokemon_info_2["asset"]),
    *position_initiale_pokemon_2,
    225,
    225,
    pokemon_info_2["nom"],
    pokemon_info_2["evolution"],
    pokemon_info_2["pv"]
)

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
bouton_attaque = Bouton(200, hauteur - 100, 150, 40, (255, 0, 0), "Attaque", None)
bouton_defense = Bouton(400, hauteur - 100, 150, 40, (0, 255, 0), "Défense", None)

# Boucle principale du combat
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Dessiner l'image de fond
    ecran_combat.blit(fond_combat, (0, 0))

    # Dessiner les Pokémon
    pokemon_1.afficher(ecran_combat)
    pokemon_2.afficher(ecran_combat)

    # Dessiner les boutons
    bouton_attaque.afficher(ecran_combat)
    bouton_defense.afficher(ecran_combat)

    # Afficher les informations des Pokémon
    nom_texte_surface = police_info.render(f"Nom: {pokemon_1.nom}", True, BLANC)
    evolution_texte_surface = police_info.render(f"Évolution: {pokemon_1.evolution}" if pokemon_1.evolution else "Évolution: Aucune", True, BLANC)
    pv_texte_surface = police_info.render(f"PV: {pokemon_1.pv}", True, BLANC)

    ecran_combat.blit(nom_texte_surface, (950, 550))
    ecran_combat.blit(evolution_texte_surface, (950, 570))
    ecran_combat.blit(pv_texte_surface, (950, 590))

    nom_texte_surface_2 = police_info.render(f"Nom: {pokemon_2.nom}", True, BLANC)
    evolution_texte_surface_2 = police_info.render(f"Évolution: {pokemon_2.evolution}" if pokemon_2.evolution else "Évolution: Aucune", True, BLANC)
    pv_texte_surface_2 = police_info.render(f"PV: {pokemon_2.pv}", True, BLANC)

    ecran_combat.blit(nom_texte_surface_2, (300, 20))
    ecran_combat.blit(evolution_texte_surface_2, (300, 40))
    ecran_combat.blit(pv_texte_surface_2, (300, 60))

    # Mise à jour de l'affichage
    pygame.display.flip()
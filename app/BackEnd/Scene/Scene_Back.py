# main.py

import pygame
import sys
import os
import time
import random
from Pokemon import Pokemon
from PokemonData import PokemonData
from Combat_Back import Combat

# Initialisation de Pygame
pygame.init()

# Couleurs
BLANC = (255, 255, 255)
NOIR = (0, 0, 0)
GRIS = (169, 169, 169)

# Dimensions de la fenêtre
largeur, hauteur = 1520, 825

class Bouton:
    def __init__(self, x, y, largeur, hauteur, couleur, texte, action, combat_instance):
        self.rect = pygame.Rect(x, y, largeur, hauteur)
        self.couleur = couleur
        self.texte_surface = None
        self.action = action
        self.combat_instance = combat_instance
        self.maj_texte(texte)

    def maj_texte(self, texte):
        self.texte_surface = police_info.render(texte, True, BLANC)

    def afficher(self, ecran):
        pygame.draw.rect(ecran, self.couleur, self.rect)
        if self.texte_surface:
            self.afficher_texte(ecran, self.texte_surface, self.rect.centerx, self.rect.centery, BLANC)

    def afficher_texte(self, ecran, texte_surface, x, y, couleur):
        ecran.blit(texte_surface, (x - texte_surface.get_width() / 2, y - texte_surface.get_height() / 2))


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

    police_titre = pygame.font.Font(None, 36)
    titre_surface = police_titre.render("Choisis ton Pokémon", True, BLANC)
    titre_rect = titre_surface.get_rect(center=(largeur // 2, 30))

    choix_pokemon = None
    while not choix_pokemon:
        ecran_selection.fill(GRIS)
        ecran_selection.blit(titre_surface, titre_rect)

        nombre_colonnes = 4
        nombre_lignes = len(images_miniatures) // nombre_colonnes

        for i, (image_miniature, rect_miniature) in enumerate(zip(images_miniatures, rects_miniatures)):
            colonne = i % nombre_colonnes
            ligne = i // nombre_colonnes

            x = (largeur // (nombre_colonnes + 1)) * (colonne + 1)
            y = (hauteur // (nombre_lignes + 1)) * (ligne + 1)

            rect_miniature.center = (x, y)
            bordure_rectangle = pygame.Rect(x - 25, y - 25, 50, 50)
            pygame.draw.rect(ecran_selection, BLANC, bordure_rectangle, 2)

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
position_initiale_pokemon_1 = (largeur // 2 - 250, hauteur // 2 + 75)
pokemon_1 = Pokemon(
    os.path.join(dossier_pokemon, pokemon_info_1["asset"]),
    *position_initiale_pokemon_1,
    225,
    225,
    pokemon_info_1["nom"],
    pokemon_info_1["evolution"],
    pokemon_info_1["pv"],
    pokemon_info_1["puissance_attaque"],
    pokemon_info_1["defense"]
)

# Création de la fenêtre principale du combat
ecran_combat = pygame.display.set_mode((largeur, hauteur))
pygame.display.set_caption("Arène Pokémon")
fond_combat = pygame.image.load('app/assets/assets_scene/backcombat.png')
fond_combat = pygame.transform.scale(fond_combat, (largeur, hauteur))
position_initiale_pokemon_2 = (largeur // 2 + 200, hauteur // 2 - 200)
pokemon_info_2 = pokemon_data.get_random_pokemon()
pokemon_2 = Pokemon(
    os.path.join(dossier_pokemon, pokemon_info_2["asset"]),
    *position_initiale_pokemon_2,
    225,
    225,
    pokemon_info_2["nom"],
    pokemon_info_2["evolution"],
    pokemon_info_2["pv"],
    pokemon_info_2["puissance_attaque"],
    pokemon_info_2["defense"]
)

police_info = pygame.font.Font(None, 24)
combat = Combat(pokemon_1, pokemon_2)

bouton_attaque = Bouton(200, hauteur - 100, 150, 40, (255, 0, 0), "Attaque", combat.attaque, combat)
bouton_defense = Bouton(400, hauteur - 100, 150, 40, (0, 255, 0), "Défense", combat.defense, combat)



# Création de l'instance de Combat
combat = Combat(pokemon_1, pokemon_2)

# Boucle principale du combat
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            if bouton_attaque.rect.collidepoint(x, y):
                bouton_attaque.action()
            elif bouton_defense.rect.collidepoint(x, y):
                bouton_defense.action()

    ecran_combat.blit(fond_combat, (0, 0))
    pokemon_1.afficher(ecran_combat)
    pokemon_2.afficher(ecran_combat)
    bouton_attaque.afficher(ecran_combat)
    bouton_defense.afficher(ecran_combat)

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

    pygame.display.flip()
    pygame.time.Clock().tick(30)
    combat.tour_suivant()

    # Vérifie si le combat est terminé
    if int(pokemon_1.pv) <= 0 or int(pokemon_2.pv) <= 0:
        # Affiche le gagnant pendant 5 secondes
        gagnant_texte_surface = police_info.render(f"Le gagnant est {pokemon_1.nom}" if int(pokemon_1.pv) > 0 else f"Le gagnant est {pokemon_2.nom}", True, BLANC)
        ecran_combat.blit(gagnant_texte_surface, (largeur // 2 - gagnant_texte_surface.get_width() // 2, hauteur // 2 - gagnant_texte_surface.get_height() // 2))
        pygame.display.flip()

        pygame.time.delay(5000)

        # Retourner au menu
        os.execv(sys.executable, [sys.executable] + ["app/FrontEnd/Window/WindowBase.py"])


import pygame
import sys
import os
import time
import random
from Pokemon import Pokemon
from PokemonData import PokemonData
from Combat_Back import Combat
sys.path.append("app/FrontEnd/Window/")
from WindowBase import Window
pygame.init()

BLANC = (255, 255, 255)
NOIR = (0, 0, 0)
GRIS = (169, 169, 169)
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


dossier_pokemon = 'app/assets/assets_pokemon'

images_miniatures = []
rects_miniatures = []
for pokemon_info in PokemonData('app/data/pokemon.json').pokemon_data:
    image_miniature = pygame.image.load(os.path.join(dossier_pokemon, pokemon_info["asset"]))
    image_miniature = pygame.transform.scale(image_miniature, (50, 50))
    images_miniatures.append(image_miniature)
    rects_miniatures.append(image_miniature.get_rect())

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

        nombre_colonnes = 5
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

pokemon_data = PokemonData('app/data/pokemon.json')

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

combat_en_cours = True
fin_du_combat = False
temps_fin_combat = 0

while combat_en_cours:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pass
        elif event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            if bouton_attaque.rect.collidepoint(x, y):
                bouton_attaque.action()
            elif bouton_defense.rect.collidepoint(x, y):
                bouton_defense.action()
            elif 600 <= x <= 800 and hauteur - 100 <= y <= hauteur - 60:
                menu = Window()
                menu.executer()

    ecran_combat.blit(fond_combat, (0, 0))
    pokemon_1.afficher(ecran_combat)
    pokemon_2.afficher(ecran_combat)
    bouton_attaque.afficher(ecran_combat)
    bouton_defense.afficher(ecran_combat)

    pygame.draw.rect(ecran_combat, (0, 0, 255), (600, hauteur - 100, 200, 40))
    bouton_retour_menu_texte = police_info.render("Retour au Menu", True, BLANC)
    ecran_combat.blit(bouton_retour_menu_texte, (700 - bouton_retour_menu_texte.get_width() // 2, hauteur - 90))

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

    if int(pokemon_1.pv) <= 0 or int(pokemon_2.pv) <= 0:
        fin_du_combat = True

    if fin_du_combat:
        temps_fin_combat += 1
        if temps_fin_combat <= 150:
            gagnant_texte_surface = police_info.render(f"Le gagnant est {pokemon_1.nom}" if int(pokemon_1.pv) > 0 else f"Le gagnant est {pokemon_2.nom}", True, BLANC)
            ecran_combat.blit(gagnant_texte_surface, (largeur // 2 - gagnant_texte_surface.get_width() // 2, hauteur // 2 - gagnant_texte_surface.get_height() // 2))
        else:
            combat_en_cours = False

    pygame.time.Clock().tick(30)
    combat.tour_suivant()


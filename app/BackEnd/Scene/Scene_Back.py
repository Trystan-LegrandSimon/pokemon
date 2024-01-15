import pygame
import sys
import os
import random
import json
from Pokemon import Pokemon
from Bouton import Bouton

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

# Fonction pour choisir un Pokémon
def choisir_pokemon():
    print("Choisissez votre Pokémon:")
    with open('app/data/pokemon.json', 'r') as file:
        data = json.load(file)
        for i, pokemon in enumerate(data["pokemon"], start=1):
            print(f"{i}. {pokemon['nom']}")
    
    while True:
        try:
            choix = int(input("Entrez le numéro du Pokémon que vous voulez choisir: "))
            if 1 <= choix <= len(data["pokemon"]):
                return data["pokemon"][choix - 1]
            else:
                print("Choix invalide. Veuillez choisir à nouveau.")
        except ValueError:
            print("Veuillez entrer un nombre.")

# Obtenir les informations du Pokémon choisi
pokemon_info = choisir_pokemon()

# Taille réduite du Pokémon
pokemon_largeur, pokemon_hauteur = 225, 225

# Dossier des Pokémon
dossier_pokemon = 'app/assets/assets_pokemon'

# Position initiale du Pokémon
position_initiale_pokemon = (largeur // 2 + 145, hauteur // 2 - 200)

# Initialiser le Pokémon avec les informations du JSON
pokemon = Pokemon(
    os.path.join(dossier_pokemon, pokemon_info["asset"]),
    *position_initiale_pokemon,
    pokemon_largeur,
    pokemon_hauteur,
    pokemon_info["nom"],
    pokemon_info["evolution"],
    pokemon_info["pv"]
)

# Classe Bouton
class Bouton:
    def __init__(self, x, y, largeur, hauteur, couleur, texte, action):
        self.rect = pygame.Rect(x, y, largeur, hauteur)
        self.couleur = couleur
        self.texte = texte
        self.action = action

    def afficher(self):
        pygame.draw.rect(ecran, self.couleur, self.rect)
        self.afficher_texte(self.texte, self.rect.centerx, self.rect.centery, BLANC)

    def afficher_texte(self, texte, x, y, couleur):
        police = pygame.font.Font(None, 24)
        texte_surface = police.render(texte, True, couleur)
        texte_rect = texte_surface.get_rect(topleft=(x - 650, y - 40))
        ecran.blit(texte_surface, texte_rect)

# Création des boutons RGB
bouton1 = Bouton(200, hauteur - 50, 100, 40, (255, 0, 0), "Bouton 1", None)
bouton2 = Bouton(400, hauteur - 50, 100, 40, (0, 255, 0), "Bouton 2", None)

# Afficher le texte avec l'invite pour appuyer sur Entrée
invite_texte = "Appuyez sur Entrée pour continuer..."
invite_font = pygame.font.Font(None, 36)
invite_surface = invite_font.render(invite_texte, True, BLANC)
invite_rect = invite_surface.get_rect(center=(largeur // 2, hauteur - 100))

# Boucle principale
en_attente_entree = True
while en_attente_entree:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
            en_attente_entree = False

    # Dessiner l'image de fond
    ecran.blit(fond, (0, 0))

    # Afficher le Pokémon
    pokemon.afficher()

    # Afficher les boutons
    bouton1.afficher()
    bouton2.afficher()

    # Afficher les informations du Pokémon
    nom_texte = f"Nom: {pokemon.nom}"
    evolution_texte = f"Évolution: {pokemon.evolution}" if pokemon.evolution else "Évolution: Aucune"
    pv_texte = f"PV: {pokemon.pv}"

    pokemon_info_texts = [nom_texte, evolution_texte, pv_texte]

    for i, texte in enumerate(pokemon_info_texts):
        bouton1.afficher_texte(texte, 1000, 50 + i * 30, BLANC)

    # Afficher l'invite pour appuyer sur Entrée
    ecran.blit(invite_surface, invite_rect)

    # Mettre à jour l'affichage
    pygame.display.flip()

# Boucle principale (après avoir appuyé sur Entrée)
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Dessiner l'image de fond
    ecran.blit(fond, (0, 0))

    # Afficher le Pokémon
    pokemon.afficher()

    # Afficher les boutons
    bouton1.afficher()
    bouton2.afficher()

    # Afficher les informations du Pokémon
    nom_texte = f"Nom: {pokemon.nom}"
    evolution_texte = f"Évolution: {pokemon.evolution}" if pokemon.evolution else "Évolution: Aucune"
    pv_texte = f"PV: {pokemon.pv}"

    pokemon_info_texts = [nom_texte, evolution_texte, pv_texte]

    for i, texte in enumerate(pokemon_info_texts):
        bouton1.afficher_texte(texte, 1000, 50 + i * 30, BLANC)

    # Mettre à jour l'affichage
    pygame.display.flip()

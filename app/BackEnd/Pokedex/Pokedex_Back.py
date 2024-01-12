#!/usr/local/bin/python3
# -*- coding: utf-8 -*-
import pygame
import sys
import os

class Pokedex:
    def __init__(self):
        pygame.init()
        self.largeur = 800
        self.hauteur = 600
        self.fenetre = pygame.display.set_mode((self.largeur, self.hauteur))
        pygame.display.set_caption("Pokédex")
        self.police_taille = 24
        self.police = pygame.font.Font(None, self.police_taille)
        # Chemin d'accès à l'image du Pokédex
        dossier_assets = "app/assets/assets_pokedex"
        assets_file = "pokedex.png"
        chemin_image = os.path.join(dossier_assets, assets_file)
        # Gestion d'erreur
        if not os.path.exists(chemin_image):
            print(f"Erreur : Le fichier image '{assets_file}' n'existe pas dans le dossier '{dossier_assets}'.")
            sys.exit()

        self.image_pokedex = pygame.image.load(chemin_image).convert()

        # Initialisation des données Pokémon
        self.donnees_pokemon = []

    def infos(self):
        print(f"Liste des Pokémon : {str(self.donnees_pokemon)}")

    def ajouter_pokemon(self, donnees_pokemon):
        if not self.donnees_pokemon:
            self.donnees_pokemon = [donnees_pokemon]
        else:
            self.donnees_pokemon.append(donnees_pokemon)

    def executer(self):
        clock = pygame.time.Clock()
        while True:
            for evenement in pygame.event.get():
                if evenement.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            self.fenetre.fill((255, 255, 255))
            self.fenetre.blit(self.image_pokedex, (0, 0))
            pygame.display.flip()
            clock.tick(60)

if __name__ == "__main__":
    pokedex = Pokedex()
    pokedex.executer()

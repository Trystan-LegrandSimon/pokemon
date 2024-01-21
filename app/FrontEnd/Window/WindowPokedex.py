#!/usr/local/bin/python3
# -*- coding: utf-8 -*-
import pygame
import sys
import os
import json

class WindowPokedex:
    def __init__(self):
        pygame.init()
        self.largeur = 800
        self.hauteur = 600
        self.fenetre = pygame.display.set_mode((self.largeur, self.hauteur))
        pygame.display.set_caption("Pokédex")
        self.police_taille = 24
        self.police = pygame.font.Font(None, self.police_taille)

        # Liste des boutons des Pokémon à droite
        self.boutons_pokemon = []
        self.bouton_selectionne = None

        # Initialisation des données Pokémon
        self.donnees_pokemon = []

        # Chargement des données Pokémon depuis le fichier JSON
        self.charger_donnees_pokemon()

        # Chemin d'accès à l'image du Pokédex
        dossier_assets = "app/assets/assets_pokemon"
        self.chemin_images = {pokemon["nom"]: os.path.join(dossier_assets, pokemon["asset"]) for pokemon in self.donnees_pokemon}

        # Gestion d'erreur
        for chemin_image in self.chemin_images.values():
            if not os.path.exists(chemin_image):
                print(f"Erreur : Le fichier image '{chemin_image}' n'existe pas.")
                sys.exit()

        # Charger l'image de fond
        dossier_assets = "app/assets/assets_pokedex"
        assets_file = "pokedex.png"
        chemin_image = os.path.join(dossier_assets, assets_file)
        self.image_fond = pygame.image.load(chemin_image).convert()

    def charger_donnees_pokemon(self):
        # Charger les données Pokémon depuis le fichier JSON
        chemin_json = 'app/data/pokemon.json'
        if os.path.exists(chemin_json):
            with open(chemin_json, "r") as fichier:
                self.donnees_pokemon = json.load(fichier)["pokemon"]
        else:
            print(f"Erreur : Le fichier JSON '{chemin_json}' n'existe pas.")
            sys.exit()

    def afficher_infos_pokemon(self, index_pokemon):
        # Afficher les informations du Pokémon sélectionné
        if index_pokemon is not None and 0 <= index_pokemon < len(self.donnees_pokemon):
            pokemon_selectionne = self.donnees_pokemon[index_pokemon]

            # Position où les informations seront affichées
            x_info = 550
            y_info = 250
            # Afficher les informations du Pokémon
            infos_surface = self.police.render(f"Nom: {pokemon_selectionne['nom']}", True, (0, 0, 0))
            self.fenetre.blit(infos_surface, (x_info, y_info))
            y_info += 30

            infos_surface = self.police.render(f"Évolution: {pokemon_selectionne['evolution']}", True, (0, 0, 0))
            self.fenetre.blit(infos_surface, (x_info, y_info))
            y_info += 30

            infos_surface = self.police.render(f"Attaque: {pokemon_selectionne['puissance_attaque']}", True, (0, 0, 0))
            self.fenetre.blit(infos_surface, (x_info, y_info))
            y_info += 30

            infos_surface = self.police.render(f"Défense: {pokemon_selectionne['defense']}", True, (0, 0, 0))
            self.fenetre.blit(infos_surface, (x_info, y_info))
            y_info += 30

            infos_surface = self.police.render(f"PV: {pokemon_selectionne['pv']}", True, (0, 0, 0))
            self.fenetre.blit(infos_surface, (x_info, y_info))
            y_info += 30

    def gerer_clic(self, x, y):
        # Vérifier si l'un des boutons des Pokémon a été cliqué
        for i, bouton in enumerate(self.boutons_pokemon):
            if bouton.collidepoint(x, y):
                self.bouton_selectionne = i
                self.afficher_infos_pokemon(self.bouton_selectionne)

    def executer(self):
        clock = pygame.time.Clock()

        # Création des boutons des Pokémon à droite
        for i, pokemon in enumerate(self.donnees_pokemon):
            bouton = pygame.Rect(50, 20 * i + 50, 200, 30)
            self.boutons_pokemon.append(bouton)

        while True:
            for evenement in pygame.event.get():
                if evenement.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif evenement.type == pygame.MOUSEBUTTONDOWN:
                    x, y = pygame.mouse.get_pos()
                    self.gerer_clic(x, y)

            self.fenetre.fill((255, 255, 255))

            # Afficher l'image de fond
            self.fenetre.blit(self.image_fond, (0, 0))

            # Afficher les noms des Pokémon à droite
            for i, pokemon in enumerate(self.donnees_pokemon):
                couleur = (255, 0, 0) if i == self.bouton_selectionne else (0, 0, 0)
                nom_surface = self.police.render(pokemon["nom"], True, couleur)
                self.fenetre.blit(nom_surface, (100, 20 * i + 100))

            # Afficher l'image du Pokémon sélectionné (redimensionnée)
            if self.bouton_selectionne is not None:
                pokemon_nom = self.donnees_pokemon[self.bouton_selectionne]["nom"]
                chemin_image = self.chemin_images[pokemon_nom]
                image_pokemon = pygame.image.load(chemin_image).convert()
                image_pokemon = pygame.transform.scale(image_pokemon, (100, 100))  # Redimensionner l'image
                self.fenetre.blit(image_pokemon, (550, 100))  # Ajuster les coordonnées x

                # Afficher les informations du Pokémon en dessous de son image
                self.afficher_infos_pokemon(self.bouton_selectionne)

            pygame.display.flip()
            clock.tick(60)

if __name__ == "__main__":
    pokedex = WindowPokedex()
    pokedex.executer()

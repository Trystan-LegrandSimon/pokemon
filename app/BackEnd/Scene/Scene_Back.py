#!/usr/local/bin/python3
# -*- coding: utf-8 -*-
import pygame
import sys
import os
class Scene:
    
    def __init__(self):
        pygame.init()
        self.largeur = 1520
        self.hauteur = 825
        self.fenetre = pygame.display.set_mode((self.largeur, self.hauteur))
        pygame.display.set_caption("pokégame !")
        dossier_assets = "app/assets/assets_scene"
        assets_back = "backcombat.png"
        chemin_back = os.path.join(dossier_assets, assets_back)
        self.fond = pygame.image.load(chemin_back).convert()
        
    def combat(self, description, combat=None, ajout_pokedex=None):
        self.description = description
        self.combat = combat
        self.ajout_pokedex = ajout_pokedex
          
    def afficher_description(self):
        print(self.description)
        
    def lancer_combat(self):
        if self.combat:
            print("Combat en cours...")
            # Logique de combat ici
            
            # Supposons qu'un Pokémon nommé "Pikachu" a été vaincu
            pokemon_vaincu = "Pikachu"
            
            # Ajouter le Pokémon vaincu au Pokedex
            if self.ajout_pokedex:
                self.ajout_pokedex.ajouter_pokemon(pokemon_vaincu)
        else:
            print("Pas de combat dans cette scène.")
            
    def effectuer_ajout_pokedex(self):
        if self.ajout_pokedex:
            print("Ajout au Pokedex en cours...")
            self.ajout_pokedex.sauvegarder_vers_json()
        else:
            print("Pas d'ajout au Pokedex dans cette scène.")

if __name__ == "__main__":
    scene = Scene()
    running = True
    while running:
        for evenement in pygame.event.get():
            if evenement.type == pygame.QUIT:
                running = False

        scene.fenetre.fill((255, 255, 255))
        scene.fenetre.blit(scene.fond, (0, 0))
        pygame.display.flip()

    pygame.quit()
    sys.exit()
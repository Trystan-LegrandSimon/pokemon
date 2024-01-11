#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

class Scene:
    
    def __init__(self, description, combat=None, ajout_pokedex=None):
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
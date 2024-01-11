#!/usr/local/bin/python3
# -*- coding: utf-8 -*-


class Pokedex:
    
    def __init__(self, donnees_pokemon):
        self.donnees_pokemon = donnees_pokemon
        
    def infos(self):
        print(f"Liste des Pokémon : {str(self.donnees_pokemon)}")
        
    def ajouter_pokemon(self, donnees_pokemon):
        if self.donnees_pokemon == "" or self.donnees_pokemon == None:
            self.donnees_pokemon = []
        else:
            self.pokemon.append(donnees_pokemon)
        
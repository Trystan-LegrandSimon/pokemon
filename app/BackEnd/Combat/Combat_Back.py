#!/usr/local/bin/python3.12
# -*- coding: utf-8 -*-

class Combat:
    
    def __init__(self, pokemon1, pokemon2):
        self.pokemon1 = pokemon1
        self.pokemon2 = pokemon2
        
    def attack(self, pokemon1, pokemon2):
        print(f"{pokemon1.nom} attaque {pokemon2.nom} !")
        print()
        
        # Calculer les dégâts
        degats = pokemon1.puissance_attaque - pokemon2.defense
        
        # Appliquer les dégâts
        pokemon2.pv -= degats
        
        # Afficher les dégâts
        print(f"{pokemon2.nom} a perdu {str(degats)} PV !")
        print(f"{pokemon2.nom} a maintenant {str(pokemon2.pv)} PV.")
        print()
        
        # Vérifier si le Pokémon est KO
        if pokemon2.pv <= 0:
            print(f"{pokemon2.nom} est KO !")
            print()
            

import sys
sys.path.append("app/BackEnd/Pokemon/")

from Pokemon_Back import Pokemon
# Exemple de création d'une instance de Pokemon
pokeball = Pokemon(nom = "Herbizarre")

# Affichage des informations du Pokemon
pokeball.infos()
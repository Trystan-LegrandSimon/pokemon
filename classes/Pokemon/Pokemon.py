#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

import json
import os

# Importer le fichier de données JSON
dossier_data = "classes/data/"
fichier_data = "pokemon_data.json"
chemin_data = os.path.join(dossier_data, fichier_data)

class Pokemon:
    
    def __init__(self, id, asset, nom, pv, niveau, puissance_attaque, defense, types, evolution):
        self.id = id
        self.asset = asset
        self.nom = nom
        self.pv = pv
        self.niveau = niveau
        self.puissance_attaque = puissance_attaque
        self.defense = defense
        self.types = types
        self.evolution = evolution
        
    def infos(self):
        print(f"id : {str(self.id)}")
        print(f"Asset : {str(self.asset)}")
        print(f"Nom : {str(self.nom)}")
        print(f"PV : {str(self.pv)}")
        print(f"Niveau : {str(self.niveau)}")
        print(f"Puissance d'Attaque : {str(self.puissance_attaque)}")
        print(f"Défense : {str(self.defense)}")
        print(f"Types : {str(self.types)}")
        print(f"Évolution : {str(self.evolution)}")
        print()
        
    def attaquer(self, pokemon):
        print(f"{self.nom} attaque {pokemon.nom} !")
        print()
        
        # Calculer les dégâts
        degats = self.puissance_attaque - pokemon.defense
        
        # Appliquer les dégâts
        pokemon.pv -= degats
        
        # Afficher les dégâts
        print(f"{pokemon.nom} a perdu {str(degats)} PV !")
        print(f"{pokemon.nom} a maintenant {str(pokemon.pv)} PV.")
        print()
        
        # Vérifier si le Pokémon est KO
        if pokemon.pv <= 0:
            print(f"{pokemon.nom} est KO !")
            print()
        
    def defense(self, pokemon):
        print(f"{self.nom} se défend !")
        print()
        
        # Calculer les dégâts
        degats = pokemon.puissance_attaque - self.defense
        
        # Appliquer les dégâts
        self.pv -= degats
        
        # Afficher les dégâts
        print(f"{self.nom} a perdu {str(degats)} PV !")
        print(f"{self.nom} a maintenant {str(self.pv)} PV.")
        print()
        
        # Vérifier si le Pokémon est KO
        if self.pv <= 0:
            print(f"{self.nom} est KO !")
            print()

# Charger les données depuis le fichier JSON
with open(chemin_data, "r") as fichier_pokemon:
    donnees_pokemon = json.load(fichier_pokemon)

# Créer une instance de la classe Pokemon pour chaque entrée dans le fichier JSON
pokemons = [Pokemon(**pokemon) for pokemon in donnees_pokemon]

# Afficher les informations de tous les Pokémon instanciés
for pokemon in pokemons:
    pokemon.infos()
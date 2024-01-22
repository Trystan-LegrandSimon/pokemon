#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

import json
import os

# Importer le fichier de données JSON
dossier_data = "app/data/"
fichier_data = "pokemon_data.json"
chemin_data = os.path.join(dossier_data, fichier_data)

class Pokemon:
    
    def __init__(self, nom):
        self.nom = nom
        self.charger_infos()

    def charger_infos(self):
        # Charger les informations depuis le fichier JSON
        with open(chemin_data, 'r') as fichier:
            data = json.load(fichier)
            for pokemon_data in data["pokemon"]:
                if pokemon_data["nom"] == self.nom:
                    # Assigner les informations au Pokemon
                    self.id = pokemon_data["id"]
                    self.asset = pokemon_data["asset"]
                    self.pv = pokemon_data["pv"]
                    self.niveau = pokemon_data["niveau"]
                    self.puissance_attaque = pokemon_data["puissance_attaque"]
                    self.defense = pokemon_data["defense"]
                    self.types = pokemon_data["types"]
                    self.evolution = pokemon_data["evolution"]
                    break

    def infos(self):
        print(f"\nInformations Pokémon :\n")
        print(f"id : {str(self.id)}")
        print(f"Nom : {self.nom}")
        print(f"Asset : {str(self.asset)}")
        print(f"PV : {self.pv}")
        print(f"Niveau : {self.niveau}")
        print(f"Puissance d'Attaque : {self.puissance_attaque}")
        print(f"Défense : {self.defense}")
        print(f"Types : {self.types}")
        print(f"Évolution : {self.evolution}\n")

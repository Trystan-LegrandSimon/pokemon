#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

import json
import os

# Importer le fichier de données JSON
dossier_data = "classes/data/"
fichier_data = "pokemon_data.json"
chemin_data = os.path.join(dossier_data, fichier_data)

class Pokemon:
    
    def __init__(self, id, asset, nom, pv, niveau, puissance_attaque, defense, type, evolution):
        self.id = id
        self.asset = asset
        self.nom = nom
        self.pv = pv
        self.niveau = niveau
        self.puissance_attaque = puissance_attaque
        self.defense = defense
        self.type = type
        self.evolution = evolution
        
    def infos(self):
        print(f"id : {str(self.id)}")
        print(f"Asset : {str(self.asset)}")
        print(f"Nom : {str(self.nom)}")
        print(f"PV : {str(self.pv)}")
        print(f"Niveau : {str(self.niveau)}")
        print(f"Puissance d'Attaque : {str(self.puissance_attaque)}")
        print(f"Défense : {str(self.defense)}")
        print(f"Type : {str(self.type)}")
        print(f"Évolution : {str(self.evolution)}")

# Charger les données depuis le fichier JSON
with open(chemin_data, "r") as fichier_pokemon:
    donnees_pokemon = json.load(fichier_pokemon)

# Afficher les données chargées
print(donnees_pokemon)
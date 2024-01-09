import json
import os

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
        print("id: ", self.id)
        print("asset: ", self.asset)
        print("nom: ", self.nom)
        print("pv: ", self.pv)
        print("niveau: ", self.niveau)
        print("puissance_attaque: ", self.puissance_attaque)
        print("defense: ", self.defense)
        print("types: ", self.types)
        print("evolution: ", self.evolution)
        print("\n")

# Chemin vers le fichier JSON
data = "classes/data/pokemon_data.json"

# Ouvrir le fichier JSON
with open(data) as mon_fichier:
    datae = json.load(mon_fichier)

    # Parcourir la liste des Pokémon et afficher leurs informations
    for pokemon_data in datae:
        pokemon_instance = Pokemon(
            pokemon_data['id'],
            pokemon_data.get('asset', ''),
            pokemon_data['nom'],
            pokemon_data['pv'],
            pokemon_data['niveau'],
            pokemon_data['puissance_attaque'],
            pokemon_data['defense'],
            pokemon_data['types'],
            pokemon_data.get('evolution', '')
        )
        pokemon_instance.infos()

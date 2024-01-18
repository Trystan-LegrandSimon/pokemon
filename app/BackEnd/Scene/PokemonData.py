# PokemonData.py
import json
import os
import random

class PokemonData:
    def __init__(self, json_file):
        with open(json_file, 'r') as file:
            data = json.load(file)
            self.pokemon_data = data["pokemon"]

    def get_random_pokemon(self):
        pokemon_info = random.choice(self.pokemon_data)
        return pokemon_info

    def get_pokemon_by_name(self, name):
        for pokemon_info in self.pokemon_data:
            if pokemon_info["nom"] == name:
                return pokemon_info
        return None

import os
import sys

class Combat:
    def __init__(self, pokemon1, pokemon2):
        self.pokemon1 = pokemon1
        self.pokemon2 = pokemon2
        self.tour = 0

    def attaque(self, attaquant, defenseur):
        print(f"{attaquant.nom} attaque {defenseur.nom} !")
        print()

        # Calculer les dégâts
        degats = attaquant.puissance_attaque - defenseur.defense

        # Appliquer les dégâts
        defenseur.pv -= degats

        # Afficher les dégâts
        print(f"{defenseur.nom} a perdu {str(degats)} PV !")
        print(f"{defenseur.nom} a maintenant {str(defenseur.pv)} PV.")
        print()

        # Vérifier si le Pokémon est KO
        if defenseur.pv <= 0:
            print(f"{defenseur.nom} est KO !")
            print()

    def defense(self, pokemon):
        print(f"{pokemon.nom} se défend !")
        print()

        # Augmenter la défense du Pokémon temporairement
        pokemon.defense += 5
        print(f"{pokemon.nom} a maintenant {str(pokemon.defense)} points de défense.")
        print()

    def tour_suivant(self):
        self.tour += 1
        print(f"Fin du tour {self.tour}.\n")
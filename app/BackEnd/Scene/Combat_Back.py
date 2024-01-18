import os
import sys

class Combat:
    
    def __init__(self, pokemon1, pokemon2):
        self.pokemon1 = pokemon1
        self.pokemon2 = pokemon2
        self.tour = 0
        
    def attaque(self):
        if self.tour % 2 == 0:
            attaquant = self.pokemon1
            defenseur = self.pokemon2
        else:
            attaquant = self.pokemon2
            defenseur = self.pokemon1

        print(f"{attaquant.nom} attaque {defenseur.nom} !")
        degats = attaquant.puissance_attaque - defenseur.defense
        defenseur.pv -= degats

        print(f"{defenseur.nom} a perdu {str(degats)} PV !")
        print(f"{defenseur.nom} a maintenant {str(defenseur.pv)} PV.")

        if defenseur.pv <= 0:
            print(f"{defenseur.nom} est KO !")

    def defense(self):
        if self.tour % 2 == 0:
            pokemon = self.pokemon1
        else:
            pokemon = self.pokemon2

        print(f"{pokemon.nom} se défend !")
        pokemon.defense += 5
        print(f"{pokemon.nom} a maintenant {str(pokemon.defense)} points de défense.")

    def tour_suivant(self):
        self.tour += 1
        print(f"Fin du tour {self.tour}.\n")
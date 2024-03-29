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
        
        # Converti les attributs pv, puissance_attaque, et defense en entiers
        degats = max(int(attaquant.puissance_attaque) - int(defenseur.defense), 0)
        defenseur.pv = str(max(int(defenseur.pv) - degats, 0))  # Convertir pv en entier pour effectuer la soustraction

        print(f"{defenseur.nom} a perdu {str(degats)} PV !")
        print(f"{defenseur.nom} a maintenant {str(max(int(defenseur.pv), 0))} PV.")

        if int(defenseur.pv) <= 0:
            print(f"{defenseur.nom} est KO !")

        # Vérifi si un Pokémon est KO et terminez la partie si nécessaire
        if int(self.pokemon1.pv) <= 0 or int(self.pokemon2.pv) <= 0:
            print("Fin de la partie !")
            sys.exit()

        # Passe au tour suivant après l'attaque
        self.tour_suivant()


    def defense(self):
        if self.tour % 2 == 0:
            pokemon = self.pokemon1
        else:
            pokemon = self.pokemon2

        print(f"{pokemon.nom} se défend !")
        pokemon.defense += 5
        print(f"{pokemon.nom} a maintenant {str(pokemon.defense)} points de défense.")

        # Passe au tour suivant après la défense
        self.tour_suivant()

    def tour_suivant(self):
        self.tour += 1
        print(f"Fin du tour {self.tour}.\n")

#!/usr/local/bin/python3.12
# -*- coding: utf-8 -*-

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
        
# Exemple de création d'instances de Pokemon
pokeball1 = Pokemon(nom="Herbizarre", puissance_attaque=20, defense=10, pv=50)
pokeball2 = Pokemon(nom="Carapuce", puissance_attaque=18, defense=12, pv=50)

# Création de l'instance de Combat
combat = Combat(pokeball1, pokeball2)

# Déroulement du combat
for _ in range(3):  # 3 tours de combat
    print(f"Début du tour {combat.tour + 1}.\n")
    
    # Actions du joueur 1 (attaquer)
    combat.attaque(pokeball1, pokeball2)
    
    # Actions du joueur 2 (défendre)
    combat.defense(pokeball2)
    
    # Passage au tour suivant
    combat.tour_suivant()

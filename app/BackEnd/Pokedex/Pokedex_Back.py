import pygame
import sys
import os
import json

class Pokedex:
    def __init__(self):
        pygame.init()
        self.largeur = 800
        self.hauteur = 600
        self.fenetre = pygame.display.set_mode((self.largeur, self.hauteur))
        pygame.display.set_caption("Pokédex")
        self.police_taille = 34
        self.police = pygame.font.Font(None, self.police_taille)

        # Liste des boutons des Pokémon à droite
        self.boutons_pokemon = []
        self.bouton_selectionne = None

        # Initialisation des données Pokémon
        self.donnees_pokemon = []

        # Chargement des données Pokémon depuis le fichier JSON
        self.charger_donnees_pokemon()

        # Chemin d'accès à l'image du Pokédex
        dossier_assets = "app/assets/assets_pokedex"
        assets_file = "pokedex.png"
        chemin_image = os.path.join(dossier_assets, assets_file)

        # Gestion d'erreur
        if not os.path.exists(chemin_image):
            print(f"Erreur : Le fichier image '{assets_file}' n'existe pas dans le dossier '{dossier_assets}'.")
            sys.exit()

        self.image_pokedex = pygame.image.load(chemin_image).convert()

    def charger_donnees_pokemon(self):
        # Charger les données Pokémon depuis le fichier JSON
        chemin_json = 'app/data/pokemon.json' 
        if os.path.exists(chemin_json):
            with open(chemin_json, "r") as fichier:
                self.donnees_pokemon = json.load(fichier)["pokemon"]
        else:
            print(f"Erreur : Le fichier JSON '{chemin_json}' n'existe pas.")
            sys.exit()

    def afficher_infos_pokemon(self, index_pokemon):
        # Afficher les informations du Pokémon sélectionné
        if index_pokemon is not None and 0 <= index_pokemon < len(self.donnees_pokemon):
            pokemon_selectionne = self.donnees_pokemon[index_pokemon]

            infos_surface = self.police.render(f"Nom: {pokemon_selectionne['nom']}", True, (0, 0, 0))
            self.fenetre.blit(infos_surface, (self.largeur // 2, 150))

            infos_surface = self.police.render(f"Évolution: {pokemon_selectionne['evolution']}", True, (0, 0, 0))
            self.fenetre.blit(infos_surface, (self.largeur // 2, 180))

            # Ajoutez d'autres informations en fonction de votre structure JSON
            # ...

    def gerer_clic(self, x, y):
        # Vérifier si l'un des boutons des Pokémon a été cliqué
        for i, bouton in enumerate(self.boutons_pokemon):
            if bouton.collidepoint(x, y):
                self.bouton_selectionne = i
                self.afficher_infos_pokemon(self.bouton_selectionne)

                # Déclencher votre action ici en fonction du Pokémon sélectionné
                self.action_pour_pokemon(self.donnees_pokemon[i])

    def action_pour_pokemon(self, pokemon):
        # Mettez ici votre logique spécifique pour l'action associée au Pokémon
        print(f"Action déclenchée pour le Pokémon : {pokemon['nom']}")

    def executer(self):
        clock = pygame.time.Clock()

        # Création des boutons des Pokémon à droite
        for i, pokemon in enumerate(self.donnees_pokemon):
            bouton = pygame.Rect(self.largeur - 700, 20 * i + 120, 200, 50)
            self.boutons_pokemon.append(bouton)

        while True:
            for evenement in pygame.event.get():
                if evenement.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif evenement.type == pygame.MOUSEBUTTONDOWN:
                    x, y = pygame.mouse.get_pos()
                    self.gerer_clic(x, y)

            self.fenetre.fill((255, 255, 255))
            self.fenetre.blit(self.image_pokedex, (0, 0))

            # Afficher les noms des Pokémon à droite
            for i, pokemon in enumerate(self.donnees_pokemon):
                couleur = (255, 0, 0) if i == self.bouton_selectionne else (0, 0, 0)
                nom_surface = self.police.render(pokemon["nom"], True, couleur)
                self.fenetre.blit(nom_surface, (self.largeur - 700, 20 * i + 120))

            pygame.display.flip()
            clock.tick(60)

if __name__ == "__main__":
    pokedex = Pokedex()
    pokedex.executer()

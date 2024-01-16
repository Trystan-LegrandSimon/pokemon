import pygame
import sys
import json

# Initialisation de Pygame
pygame.init()

# Couleurs
BLANC = (255, 255, 255)

# Dimensions de la fenêtre
largeur, hauteur = 800, 600

class PokemonSelection:
    def __init__(self, json_file):
        self.pokemon_data = self.charger_pokemon(json_file)
        self.selection = None

        # Création de la fenêtre de sélection
        self.ecran = pygame.display.set_mode((largeur, hauteur))
        pygame.display.set_caption("Sélection du Pokémon")

        # Police pour le texte
        self.police = pygame.font.Font(None, 36)

    def charger_pokemon(self, json_file):
        with open(json_file, 'r') as file:
            data = json.load(file)
            return data["pokemon"]

    def afficher_grille(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = pygame.mouse.get_pos()
                    pokemon_choisi = self.obtenir_pokemon_selectionne(x, y)
                    if pokemon_choisi:
                        self.selection = pokemon_choisi
                        return

            self.ecran.fill(BLANC)
            self.afficher_texte("Sélectionnez votre Pokémon", (largeur // 2, 50))

            # Afficher la grille de Pokémon
            self.afficher_grille_pokemon()

            pygame.display.flip()

    def afficher_texte(self, texte, position):
        texte_surface = self.police.render(texte, True, BLANC)
        texte_rect = texte_surface.get_rect(center=position)
        self.ecran.blit(texte_surface, texte_rect)

    def afficher_grille_pokemon(self):
        x, y = 100, 150
        espace_entre_pokemon = 100

        for pokemon in self.pokemon_data:
            pokemon_rect = pygame.Rect(x, y, 80, 80)
            pygame.draw.rect(self.ecran, (200, 200, 200), pokemon_rect)

            # Afficher le nom du Pokémon sur le rectangle
            nom_surface = self.police.render(pokemon["nom"], True, BLANC)
            nom_rect = nom_surface.get_rect(center=pokemon_rect.center)
            self.ecran.blit(nom_surface, nom_rect)

            x += espace_entre_pokemon

    def obtenir_pokemon_selectionne(self, x, y):
        for i, pokemon in enumerate(self.pokemon_data):
            rect = pygame.Rect(100 + i * 100, 150, 80, 80)
            if rect.collidepoint(x, y):
                return pokemon

# Exemple d'utilisation dans le même fichier
if __name__ == "__main__":
    pokemon_selection = PokemonSelection('app/data/pokemon.json')
    pokemon_selection.afficher_grille()
    pokemon_choisi = pokemon_selection.selection
    print(f"Pokémon choisi : {pokemon_choisi}")

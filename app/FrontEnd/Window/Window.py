import pygame
import sys
import os
import math

class Window:
    
    def __init__(self):
        pygame.init()
        self.largeur = 800
        self.hauteur = 600
        self.fenetre = pygame.display.set_mode((self.largeur, self.hauteur))
        pygame.display.set_caption("Menu")
        self.police = pygame.font.Font(None, 24)
        # chemin d'accès au fond du menu
        dossier_assets = "app/assets/assets_menu"
        assets_file = "backgmenu.png"
        assets_titre = "pokemontitre.png"
        chemin_image = os.path.join(dossier_assets, assets_file)
        chemin_titre = os.path.join(dossier_assets, assets_titre)
        
        # gestion d'erreur 
        if not os.path.exists(chemin_image):
            print(f"Erreur : Le fichier image '{assets_file}' n'existe pas dans le dossier '{dossier_assets}'.")
            sys.exit()

        self.fond = pygame.image.load(chemin_image).convert()
        self.titre = pygame.image.load(chemin_titre).convert_alpha()
        self.bordure_couleur_phase = 0

    def afficher_texte(self, texte, x, y, couleur):
        texte_surface = self.police.render(texte, True, couleur)
        texte_rect = texte_surface.get_rect(center=(x, y))
        self.fenetre.blit(texte_surface, texte_rect)
        
    def afficher_boutons(self):
        bouton_largeur = 175
        bouton_hauteur = 30
        espacement = 20

        for i in range(3):
            bouton_rect = pygame.Rect((self.largeur - bouton_largeur) // 2 + (i - 1) * (bouton_largeur + espacement), 425, bouton_largeur, bouton_hauteur)
            pygame.draw.rect(self.fenetre, (255, 0, 0), bouton_rect)

            bordure_x = bouton_rect.x - 5
            bordure_y = bouton_rect.y - 5
            bordure_largeur = bouton_largeur + 10
            bordure_hauteur = bouton_hauteur + 10

            r = int(127 * math.sin(self.bordure_couleur_phase) + 128)
            g = int(127 * math.sin(self.bordure_couleur_phase + 2.0) + 128)
            b = int(127 * math.sin(self.bordure_couleur_phase + 4.0) + 128)

            pygame.draw.rect(self.fenetre, (r, g, b), (bordure_x, bordure_y, bordure_largeur, bordure_hauteur), 5)

            texte = ""
            if i == 0:
                texte = "Lancer une partie"
            elif i == 1:
                texte = "Ajouter un Pokémon"
            elif i == 2:
                texte = "Accéder au Pokédex"

            self.afficher_texte(texte, bouton_rect.centerx, bouton_rect.centery, (255, 255, 255))

        self.bordure_couleur_phase += 0.05

    def afficher_titre(self):
        titre_rect = self.titre.get_rect(center=(self.largeur // 2, 100))
        self.fenetre.blit(self.titre, titre_rect)

    def executer(self):
        clock = pygame.time.Clock()
        while True:
            for evenement in pygame.event.get():
                if evenement.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif evenement.type == pygame.MOUSEBUTTONDOWN:
                    x, y = pygame.mouse.get_pos()
                    self.verifier_clic(x, y)
            self.fenetre.fill((255, 255, 255))
            self.fenetre.blit(self.fond, (0, 0))
            self.afficher_boutons()
            self.afficher_titre()
            pygame.display.flip()
            clock.tick(60)

if __name__ == "__main__":
    menu = Window()
    menu.executer()
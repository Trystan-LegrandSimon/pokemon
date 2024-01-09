import pygame
import sys
import os

class MenuPokemon:
    def __init__(self):
        pygame.init()
        self.largeur = 800
        self.hauteur = 600
        self.fenetre = pygame.display.set_mode((self.largeur, self.hauteur))
        pygame.display.set_caption("Menu Pokémon")
        self.police = pygame.font.Font(None, 24)
        
        # Définissez le chemin du dossier des assets
        dossier_assets = "assets/assets_menu"

        # Définissez le nom du fichier image
        assets_file = "backgmenu.png"

        # Construisez le chemin complet du fichier image
        chemin_image = os.path.join(dossier_assets, assets_file)

        # Vérifiez si le fichier image existe
        if not os.path.exists(chemin_image):
            print(f"Erreur : Le fichier image '{assets_file}' n'existe pas dans le dossier '{dossier_assets}'.")
            sys.exit()

        # Chargez l'image du fond d'écran
        self.fond = pygame.image.load(chemin_image).convert()

    def afficher_texte(self, texte, x, y, couleur):
        texte_surface = self.police.render(texte, True, couleur)
        texte_rect = texte_surface.get_rect(center=(x, y))
        self.fenetre.blit(texte_surface, texte_rect)

    def afficher_boutons(self):
        bouton_largeur = 175
        bouton_hauteur = 30
        espacement = 20

        bouton1_rect = pygame.Rect((self.largeur - bouton_largeur) // 2 - bouton_largeur - espacement, 400, bouton_largeur, bouton_hauteur)
        bouton2_rect = pygame.Rect((self.largeur - bouton_largeur) // 2, 400, bouton_largeur, bouton_hauteur)
        bouton3_rect = pygame.Rect((self.largeur - bouton_largeur) // 2 + bouton_largeur + espacement, 400, bouton_largeur, bouton_hauteur)

        pygame.draw.rect(self.fenetre, (255, 0, 0), bouton1_rect)
        pygame.draw.rect(self.fenetre, (255, 0, 0), bouton2_rect)
        pygame.draw.rect(self.fenetre, (255, 0, 0), bouton3_rect)

        self.afficher_texte("Lancer une partie", bouton1_rect.centerx, bouton1_rect.centery, (255, 255, 255))
        self.afficher_texte("Ajouter un Pokémon", bouton2_rect.centerx, bouton2_rect.centery, (255, 255, 255))
        self.afficher_texte("Accéder au Pokédex", bouton3_rect.centerx, bouton3_rect.centery, (255, 255, 255))

    def executer(self):
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
            pygame.display.flip()
            pygame.time.Clock().tick(60)

    def verifier_clic(self, x, y):
        bouton1_rect = pygame.Rect((self.largeur - 150) // 2 - 150 - 20, 400, 150, 30)
        bouton2_rect = pygame.Rect((self.largeur - 150) // 2 - 20, 400, 150, 30)
        bouton3_rect = pygame.Rect((self.largeur - 150) // 2 + 150 + 20 - 150, 400, 150, 30)

        if bouton1_rect.collidepoint(x, y):
            print("Lancer une partie")
        elif bouton2_rect.collidepoint(x, y):
            print("Ajouter un Pokémon")
        elif bouton3_rect.collidepoint(x, y):
            print("Accéder au Pokédex")

if __name__ == "__main__":
    menu = MenuPokemon()
    menu.executer()

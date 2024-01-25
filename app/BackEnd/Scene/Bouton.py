# Bouton.py
import pygame

class Bouton:
    def __init__(self, x, y, largeur, hauteur, couleur, texte, action):
        self.rect = pygame.Rect(x, y, largeur, hauteur)
        self.couleur = couleur
        self.texte_surface = None
        self.action = action

        self.maj_texte(texte)

    def maj_texte(self, texte):
        self.texte_surface = pygame.font.Font(None, 24).render(texte, True, (255, 255, 255))

    def afficher(self, ecran):
        pygame.draw.rect(ecran, self.couleur, self.rect)

        # Vérifier si la surface de texte existe
        if self.texte_surface:
            self.afficher_texte(ecran, self.texte_surface, self.rect.centerx, self.rect.centery, (255, 255, 255))

    def afficher_texte(self, ecran, texte_surface, x, y, couleur):
        ecran.blit(texte_surface, (x - texte_surface.get_width() / 2, y - texte_surface.get_height() / 2))

import pygame

class Bouton:
    def __init__(self, x, y, largeur, hauteur, couleur, texte, action):
        self.rect = pygame.Rect(x, y, largeur, hauteur)
        self.couleur = couleur
        self.texte = texte
        self.action = action

    def afficher(self, ecran):
        pygame.draw.rect(ecran, self.couleur, self.rect)
        self.afficher_texte(ecran, self.texte, self.rect.centerx, self.rect.centery, (255, 255, 255))

    def afficher_texte(self, ecran, texte, x, y, couleur):
        police = pygame.font.Font(None, 24)
        texte_surface = police.render(texte, True, couleur)
        texte_rect = texte_surface.get_rect(topleft=(x - 650, y - 40))
        ecran.blit(texte_surface, texte_rect)

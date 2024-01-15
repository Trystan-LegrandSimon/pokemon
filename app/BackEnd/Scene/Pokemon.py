import pygame
import os

class Pokemon(pygame.sprite.Sprite):
    def __init__(self, image, x, y, largeur, hauteur, nom, evolution, pv):
        super().__init__()
        self.image = pygame.image.load(image)
        self.image = pygame.transform.scale(self.image, (largeur, hauteur))
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.nom = nom
        self.evolution = evolution
        self.pv = pv

    def afficher(self, ecran):
        ecran.blit(self.image, self.rect)

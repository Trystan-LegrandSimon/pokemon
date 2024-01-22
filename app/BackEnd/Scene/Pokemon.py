# pokemon.py
import pygame
import os
import sys


class Pokemon(pygame.sprite.Sprite):
    def __init__(self, image, x, y, largeur, hauteur, nom, evolution, pv, puissance_attaque, defense):
        super().__init__()
        self.image = pygame.image.load(image)
        self.image = pygame.transform.scale(self.image, (largeur, hauteur))
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.nom = nom
        self.evolution = evolution
        self.pv = pv
        self.puissance_attaque = puissance_attaque
        self.defense = defense

    def afficher(self, ecran):
        ecran.blit(self.image, self.rect)


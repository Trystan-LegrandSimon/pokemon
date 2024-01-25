#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

import pygame
import sys
sys.path.append("app/BackEnd/Scene/")
from Scene_Back import Scene

class WindowGame:
    
    def __init__(self):
        self.scene = Scene()
        self.running = True
        self.clock = pygame.time.Clock()

    def run(self):
        while self.running:
            for evenement in pygame.event.get():
                if evenement.type == pygame.QUIT:
                    self.running = False

            self.scene.fenetre.fill((255, 255, 255))
            self.scene.fenetre.blit(self.scene.fond, (0, 0))
            pygame.display.flip()

            self.clock.tick(60)

if __name__ == "__main__":
    game = WindowGame()
    game.run()
import pygame
import sys
import os

class Scene:
    def __init__(self):
        pygame.init()
        self.largeur = 1520
        self.hauteur = 825
        self.fenetre = pygame.display.set_mode((self.largeur, self.hauteur))
        pygame.display.set_caption("pokégame !")
        dossier_assets = "assets/assets_scene"
        assets_back = "backcombat.png"
        chemin_back = os.path.join(dossier_assets, assets_back)
        self.fond = pygame.image.load(chemin_back).convert()

if __name__ == "__main__":
    scene = Scene()
    running = True
    while running:
        for evenement in pygame.event.get():
            if evenement.type == pygame.QUIT:
                running = False

        scene.fenetre.fill((255, 255, 255))
        scene.fenetre.blit(scene.fond, (0, 0))
        pygame.display.flip()

    pygame.quit()
    sys.exit()

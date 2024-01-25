import pygame
import sys
import os
import json
import tkinter as tk
from tkinter import filedialog
sys.path.append("app/FrontEnd/Window/")
from WindowBase import Window

WINDOW_SIZE = (400, 400)
BUTTON_RECT = pygame.Rect(150, 350, 100, 40)
ADD_BUTTON_RECT = pygame.Rect(150, 310, 100, 30)
RETURN_MENU_BUTTON_RECT = pygame.Rect(150, 270, 100, 30)

class WindowsAjout:
    def __init__(self, chemin_du_pokedex):
        pygame.init()
        self.window_size = WINDOW_SIZE
        self.screen = pygame.display.set_mode(self.window_size)
        pygame.display.set_caption("WindowsAjout")

        self.text_font = pygame.font.Font(None, 24)
        self.input_font = pygame.font.Font(None, 18)

        self.informations_pokemon = {
            "nom": "",
            "evolution": "",
            "puissance_attaque": "",  
            "defense": "",
            "pv": "",
            "asset": ""  
        }

        self.chemin_du_pokedex = chemin_du_pokedex
        self.image_button_rect = pygame.Rect(150, 310, 150, 30)
        self.saisir_informations()

    def run(self):
        clock = pygame.time.Clock()
        running = True

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if BUTTON_RECT.collidepoint(pygame.mouse.get_pos()):
                        self.ajouter_pokemon()
                    elif ADD_BUTTON_RECT.collidepoint(pygame.mouse.get_pos()):
                        self.ajouter_pokemon()
                    elif self.image_button_rect.collidepoint(pygame.mouse.get_pos()):
                        self.ouvrir_dialogue_image()
                    elif RETURN_MENU_BUTTON_RECT.collidepoint(pygame.mouse.get_pos()):
                        running = False  # Terminer la boucle et le programme

                elif event.type == pygame.KEYDOWN:
                    self.gerer_saisie(event)

            self.screen.fill((255, 255, 255))
            self.afficher_formulaire()
            pygame.display.flip()
            clock.tick(60)

    def gerer_saisie(self, event):
        champ_actif = self.champ_actif()

        if champ_actif is not None:
            if event.key == pygame.K_RETURN:
                champ_suivant = self.champ_suivant(champ_actif)
                self.activer_saisie(champ_suivant)
            elif event.key == pygame.K_BACKSPACE:
                self.informations_pokemon[champ_actif] = self.informations_pokemon[champ_actif][:-1]
            elif event.unicode.isalnum() or event.unicode.isspace():
                self.informations_pokemon[champ_actif] += event.unicode

    def saisir_informations(self):
        self.active_input = "nom"
        self.champs_rects = {
            "nom": pygame.Rect(150, 50, 200, 30),
            "evolution": pygame.Rect(150, 90, 200, 30),
            "puissance_attaque": pygame.Rect(150, 130, 200, 30),
            "defense": pygame.Rect(150, 170, 200, 30),
            "pv": pygame.Rect(150, 210, 200, 30)
        }

        self.run()

    def afficher_formulaire(self):
        for champ, rect in self.champs_rects.items():
            pygame.draw.rect(self.screen, (0, 0, 0), rect, 2)

            label_surface = self.text_font.render(f"{champ.capitalize()}: ", True, (0, 0, 0))
            self.screen.blit(label_surface, (70, rect.y + 5))

            saisie_surface = self.input_font.render(self.informations_pokemon[champ], True, (0, 0, 0))
            self.screen.blit(saisie_surface, (rect.x + 5, rect.y + 5))

        # Afficher le bouton pour ajouter une image
        pygame.draw.rect(self.screen, (0, 0, 0), self.image_button_rect, 2)
        image_button_surface = self.text_font.render("Ajouter une Image", True, (0, 0, 0))
        self.screen.blit(image_button_surface, (self.image_button_rect.x + 5, self.image_button_rect.y + 5))

        # Afficher le bouton d'ajout
        pygame.draw.rect(self.screen, (0, 0, 0), BUTTON_RECT, 2)
        bouton_surface = self.text_font.render("Ajouter", True, (0, 0, 0))
        self.screen.blit(bouton_surface, (BUTTON_RECT.x + 5, BUTTON_RECT.y + 5))

        # Afficher le bouton "Ajouter"
        pygame.draw.rect(self.screen, (0, 0, 0), ADD_BUTTON_RECT, 2)
        add_button_surface = self.text_font.render("Ajouter", True, (0, 0, 0))
        self.screen.blit(add_button_surface, (ADD_BUTTON_RECT.x + 5, ADD_BUTTON_RECT.y + 5))

        # Afficher le bouton "Retour au menu"
        pygame.draw.rect(self.screen, (0, 0, 0), RETURN_MENU_BUTTON_RECT, 2)
        return_menu_button_surface = self.text_font.render("Retour au menu", True, (0, 0, 0))
        self.screen.blit(return_menu_button_surface, (RETURN_MENU_BUTTON_RECT.x + 5, RETURN_MENU_BUTTON_RECT.y + 5))

    def ouvrir_dialogue_image(self):
        root = tk.Tk()
        root.withdraw()
        file_directory = filedialog.askopenfilename(filetypes=[("PNG Images", "*.png")])
        if file_directory:
            self.informations_pokemon["asset"] = file_directory

    def champ_suivant(self, champ_actuel):
        champs = list(self.champs_rects.keys())
        index_actuel = champs.index(champ_actuel)
        index_suivant = (index_actuel + 1) % len(champs)
        return champs[index_suivant]

    def champ_actif(self):
        for champ, rect in self.champs_rects.items():
            if rect.collidepoint(pygame.mouse.get_pos()):
                return champ
        return None

    def activer_saisie(self, champ):
        self.active_input = champ
        
    def retour_au_menu(self):
        menu = Window()
        menu.executer()

    def ajouter_pokemon(self):
        if all(self.informations_pokemon.values()):
            if os.path.exists(self.chemin_du_pokedex):
                with open(self.chemin_du_pokedex, "r") as fichier:
                    donnees_pokemon = json.load(fichier).get("pokemon", [])
            else:
                donnees_pokemon = []

            nouveau_pokemon = {
                "nom": self.informations_pokemon["nom"],
                "evolution": self.informations_pokemon["evolution"],
                "puissance_attaque": self.informations_pokemon["puissance_attaque"],
                "defense": self.informations_pokemon["defense"],
                "pv": self.informations_pokemon["pv"],
                "asset": self.informations_pokemon["asset"]
            }

            donnees_pokemon.append(nouveau_pokemon)

            with open(self.chemin_du_pokedex, "w") as fichier:
                json.dump({"pokemon": donnees_pokemon}, fichier)

            pygame.quit()
            sys.exit()



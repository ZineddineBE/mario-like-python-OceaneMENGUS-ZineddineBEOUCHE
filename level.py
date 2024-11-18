import random
import pygame

class Level:
    def __init__(self, screen_width, screen_height):
        self.screen_width = screen_width
        self.screen_height = screen_height

        # Liste des images de fond
        self.background_images = [
            pygame.image.load('assets/BG/mountain.png').convert(),
            pygame.image.load('assets/BG/rock.png').convert(),
            pygame.image.load('assets/BG/snow.png').convert()
        ]
        # On garde un index pour l'image actuelle
        self.current_background_index = random.randint(0, len(self.background_images) - 1)
        self.current_background = self.background_images[self.current_background_index]

    def update_background(self, player):
        # Si le joueur dépasse la bordure droite de l'écran, on change l'arrière-plan
        if player.x > self.screen_width:
            # Changer l'arrière-plan aléatoirement
            self.current_background_index = random.randint(0, len(self.background_images) - 1)
            self.current_background = self.background_images[self.current_background_index]
            
            # Réinitialiser la position du joueur à gauche de l'écran
            player.x = -player.width  # Le joueur réapparaît à gauche

    def draw(self, screen):
        # Afficher l'image de fond
        screen.blit(self.current_background, (0, 0))

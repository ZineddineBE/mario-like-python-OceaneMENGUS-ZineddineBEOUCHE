import pygame

class Floor():

    def __init__(self, screen_width, screen_height):
        super().__init__()
        self.width = screen_width + 100   # Largeur du sol (par exemple, toute la largeur de l'écran)
        self.height = 100   # Hauteur du sol, ajustez selon votre design
        self.y = screen_height - self.height       # Position Y du sol (peut être ajusté selon le design)
        self.rect = pygame.Rect(0, self.y, self.width, self.height)

    def display_floor(self, surface):
        pygame.draw.rect(surface, (255, 245, 220), self.rect)
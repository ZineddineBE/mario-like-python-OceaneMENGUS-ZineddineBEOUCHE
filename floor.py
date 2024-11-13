import pygame

class Floor(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.rect = pygame.Rect(0, 650, 1000, 100)

    def display_floor(self, surface):
        pygame.draw.rect(surface, (255, 245, 220), self.rect)
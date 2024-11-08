from typing import Any
import pygame
import animation

#Création du joueur
class Player(pygame.sprite.Sprite):

    def __init__(self):
      super().__init__()
      self.velocity = 4 #Vitesse de déplacement en px
      self.width = 120
      self.height = 68

      self.is_animating = False
    
      self.sprites = []
      for i in range(1, 10):
        self.sprites.append(pygame.image.load(f'Mario/assets/player/Walk/Walk{i}.png'))

      self.current_sprite = 0
      self.image = self.sprites[self.current_sprite]
      self.rect = self.image.get_rect()
      self.rect.x = 400
      self.rect.y = 500   

    def move_right(self):
      self.rect.x += self.velocity

    def move_left(self):
      self.rect.x -= self.velocity

    def animate(self):
      self.is_animating = True

    def update(self, speed):
      if self.is_animating == True:
        self.current_sprite += speed

        if self.current_sprite >= len(self.sprites):
          self.current_sprite = 0
          self.is_animating = False

        self.image = self.sprites[int(self.current_sprite)]
      
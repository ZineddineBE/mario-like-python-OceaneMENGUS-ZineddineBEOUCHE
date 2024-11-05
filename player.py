import pygame
import animation

#Création du joueur
class Player(animation.AnimateSprite):

    def __init__(self):
      super().__init__("idle (1)")
      self.velocity = 5 #Vitesse de déplacement en px
      self.width = 120
      self.height = 68
      self.rect = self.image.get_rect()
      self.rect.x = 400
      self.rect.y = 500

    def move_right(self):
      self.rect.x += self.velocity

    def move_left(self):
      self.rect.x -= self.velocity
      
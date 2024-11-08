import pygame
import sys
from game import Game

#Charger les composants
pygame.init()

#Charger notre jeu
game = Game()

# Paramètres de la fenêtre
pygame.display.set_caption("Mario Like - Océane Mengus x Zineddine Beouche")

screen = pygame.display.set_mode((1000,750))

background = pygame.image.load('Mario/assets/background/png/BG/BG.png')

#Maintenir la fenêtre
running = True

moving_sprites = pygame.sprite.Group()
moving_sprites.add(game.player)

#boucle tant que le jeu est actif
while running:

   #Arrière plan
   screen.blit(background, (0, 0)) #largeur / hauteur


   player_scaled = pygame.transform.scale(game.player.image, (game.player.width, game.player.height))
   
   

   if game.pressed.get(pygame.K_RIGHT):
      game.player.move_right()
      game.player.animate()
      if game.player.rect.x >= 930:
         game.player.rect.x = 0
   elif game.pressed.get(pygame.K_LEFT) and game.player.rect.x > 0:
      game.player.animate()
      game.player.move_left()
   
    #Si le joueur ferme cette fenêtre
   for event in pygame.event.get():
      #Que l'evenement est fermeture de fenêtre
      if event.type == pygame.QUIT:
         running = False
         pygame.quit()
      #Détecter si un joueur lâche une touche
      elif event.type == pygame.KEYDOWN:
        game.pressed[event.key] = True
      elif event.type == pygame.KEYUP:
        game.player.is_animating = False
        game.pressed[event.key] = False
        game.player.image = pygame.image.load('Mario/assets/player/Idle/Idle1.png')
   
   moving_sprites.update(0.2)
   #Mettre à jour l'écran
   pygame.display.flip()
   

      

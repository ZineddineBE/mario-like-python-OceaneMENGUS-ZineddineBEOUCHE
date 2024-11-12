import pygame
from player import Player

pygame.init()

# Définition de la taille de la fenêtre
screen_width = 1000
screen_height = 750

# Création de la fenêtre d'affichage
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Mario Like")

# Charger l'arrière-plan
background = pygame.image.load('assets/BG/BG.png')

# Créer un joueur
player = Player(300, 600, 3)

# Gestion du framerate
clock = pygame.time.Clock()
FPS = 60

# Boucle principale du jeu
run = True
while run:
    # Dessine l'arrière-plan
    screen.blit(background, (0, 0))

    keys = pygame.key.get_pressed() # Récupère l'état des touches du clavier
    player.update(keys) # Met à jour l'état du joueur
    player.draw(screen) # Affiche l'image du joueur

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.flip() # Met à jour l'affichage
    clock.tick(FPS) # Limite le jeu à 60 FPS

pygame.quit()

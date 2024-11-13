import pygame
from player import Player
from floor import Floor

pygame.init()

# Définition de la taille de la fenêtre
screen_width = 1000
screen_height = 750

# Création de la fenêtre d'affichage
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Mario Like - Océane Mengus x Zineddine Beouche")

# Charger l'arrière-plan
background = pygame.image.load('assets/BG/BG.png')

# Créer un joueur
player = Player(300, 0, 3)

#Création du sol
floor = Floor()

#Création de la gravité
gravity = (0, 10)
resistence = (0, 0)

#
floor_collision = False

# Gestion du framerate
clock = pygame.time.Clock()
FPS = 60

def game_gravity():
    player.y += gravity[1] + resistence[1]
    player.rect.topleft = (player.x, player.y)

# Boucle principale du jeu
run = True
while run:
    # Dessine l'arrière-plan
    screen.blit(background, (0, 0))

    keys = pygame.key.get_pressed() # Récupère l'état des touches du clavier
    player.update(keys) # Met à jour l'état du joueur
    player.draw(screen) # Affiche l'image du joueur
    
    
    # Affiche l'image Idle du joueur quand le personnage ne bouge pas
    if not (keys[pygame.K_LEFT] or keys[pygame.K_RIGHT]):
        idle = pygame.image.load(f'assets/player/Idle (1).png').convert_alpha()
        if player.facing_left:
            player.image = pygame.transform.flip(idle, True, False)
            player.image = pygame.transform.scale(player.image, (player.width, player.height))
        else:
            player.image = idle
            player.image = pygame.transform.scale(player.image, (player.width, player.height))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False    
    if floor.rect.colliderect(player.rect):
        resistence = (0, -10)
        floor_collision = True
        player.number_of_jump = 0
    else:
        resistence = (0, 0)

    if player.is_jumped and floor_collision:
        if player.number_of_jump < 2:
            player.player_jump()

    game_gravity()
    floor.display_floor(screen) #affiche le sol
    pygame.display.flip() # Met à jour l'affichage
    clock.tick(FPS) # Limite le jeu à 60 FPS
pygame.quit()





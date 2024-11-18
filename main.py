import pygame
from player import Player
from floor import Floor
from level import Level

pygame.init()
pygame.mixer.init()

# Définition de la taille de la fenêtre
screen_width = 1280
screen_height = 720

# Création de la fenêtre d'affichage
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Mario Like - Océane Mengus x Zineddine Beouche")

# Créer un joueur
player = Player(300, 550, 10, screen_width)

#Création du sol
floor = Floor(screen_width, screen_height)

#Création du niveau
level = Level(screen_width, screen_height)

#Création de la gravité
gravity = (0, 10)
resistence = (0, 0)

#Déclaration du booléen qui gère si le personnage est en collision avec le sol
floor_collision = False

# Gestion du framerate
clock = pygame.time.Clock()
FPS = 60

# Chargement de la musique
pygame.mixer.music.load('assets/sounds/TheForest.wav')
pygame.mixer.music.set_volume(0.15)
pygame.mixer.music.play()

def game_gravity():
    if not floor.rect.colliderect(player.rect):
        player.y += gravity[1] + resistence[1]
    player.rect.topleft = (player.x, player.y)

# Boucle principale du jeu
run = True
while run:

    keys = pygame.key.get_pressed() # Récupère l'état des touches du clavier

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


    # Met à jour l'arrière-plan si nécessaire
    level.update_background(player)  # Changer l'arrière-plan si le joueur dépasse la bordure droite

    # Dessiner l'arrière-plan mis à jour
    level.draw(screen)

    player.update(keys)  # Met à jour l'état du joueur
    player.draw(screen)  # Affiche le joueur
    
    game_gravity()  # Applique la gravité
    floor.display_floor(screen)  # Affiche le sol
    pygame.display.flip()  # Met à jour l'affichage
    clock.tick(FPS)  # Limite à 60 FPS
pygame.quit()





import pygame
import time

class Player:
    def __init__(self, x, y, speed, screen_width):
        self.x = x
        self.y = y
        self.width = 65
        self.height = 80
        self.speed = speed
        self.frame_index = 0
        self.animation_speed = 0.2

        # Frames de marche et de saut
        self.walk_frames = self.load_walk_frames()  
        self.jump_frames = self.load_jump_frames()  

        # Image Idle préchargée
        self.idle_image = pygame.image.load('assets/player/Idle/Idle.png').convert_alpha()
        self.idle_image = pygame.transform.scale(self.idle_image, (self.width, self.height))
        
        # Initialiser l'image et le rectangle
        self.image = self.idle_image
        self.rect = self.image.get_rect(topleft=(self.x, self.y))

        # Variables de direction, saut, gravité et cooldown de saut
        self.facing_left = False
        self.is_jumped = False
        self.velocity_y = 0  
        self.gravity = 1     
        self.jump_strength = 15  
        self.number_of_jump = 0  

        # Variables de suivi du saut
        self.jump_up = 0
        self.jump_down = 0
        
        # Cooldown pour le saut
        self.jump_cooldown = 0.25  # 0.25 seconde de délai
        self.last_jump_time = 0

        # Screen width pour la gestion de la position
        self.screen_width = screen_width

        # Son du jump
        self.jump_sound = pygame.mixer.Sound('assets/sounds/jump.wav')
        self.jump_sound.set_volume(0.5)

        

    def load_walk_frames(self):
        frames = []
        for i in range(1, 10):
            frame = pygame.image.load(f'assets/player/Walk/Walk ({i}).png').convert_alpha()
            frame = pygame.transform.scale(frame, (self.width, self.height))
            frames.append(frame)
        return frames
    
    def load_jump_frames(self):
        frames = []
        for i in range(1, 12):
            frame = pygame.image.load(f'assets/player/Jump/Jump ({i}).png').convert_alpha()
            frame = pygame.transform.scale(frame, (self.width, self.height))
            frames.append(frame)
        return frames

    def update(self, keys):
        self.moving = False   

        # Gestion des touches pour le mouvement horizontal
        if keys[pygame.K_q] or keys[pygame.K_LEFT]:
            self.x -= self.speed
            self.facing_left = True
            self.moving = True

        if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            self.x += self.speed
            self.facing_left = False
            self.moving = True

        # Si le joueur dépasse le bord droit de l'écran, réapparaît à gauche
        if self.x > self.screen_width:
            self.x = -self.width  # Réapparaît à gauche de l'écran

        # Limite la position horizontale aux bords de l'écran
        # Prendre en compte la largeur du joueur pour la position droite
        self.x = max(0, min(self.x, self.screen_width + self.width))

        # Gestion du saut avec cooldown
        current_time = time.time()
        if (self.number_of_jump == 0 and 
            (keys[pygame.K_z] or keys[pygame.K_SPACE] or keys[pygame.K_UP]) and
            current_time - self.last_jump_time >= self.jump_cooldown):
            self.jump_sound.play()
            
            self.is_jumped = True
            self.velocity_y = -self.jump_strength
            self.number_of_jump += 1
            self.last_jump_time = current_time


        # Appliquer la gravité si le joueur est en l'air
        if self.is_jumped:
            self.velocity_y += self.gravity
            self.y += self.velocity_y

            # Animation de jump
            self.frame_index += self.animation_speed
            if self.frame_index >= len(self.jump_frames):
                self.frame_index = 0
            self.image = self.jump_frames[int(self.frame_index)]

            # Appliquer le flip si le personnage saute vers la gauche
            if self.facing_left:
                self.image = pygame.transform.flip(self.image, True, False)

            # Arrêter le saut lorsque le joueur atteint le sol
            if self.y >= 650:
                self.y = 650
                self.is_jumped = False
                self.velocity_y = 0
                self.number_of_jump = 0

        # Gestion de l'animation de marche
        elif self.moving:
            self.frame_index += self.animation_speed
            if self.frame_index >= len(self.walk_frames):
                self.frame_index = 0
            self.image = self.walk_frames[int(self.frame_index)]

            # Appliquer le flip horizontal si le joueur se déplace vers la gauche
            if self.facing_left:
                self.image = pygame.transform.flip(self.image, True, False)
        else:
            # Image Idle lorsque le joueur est au repos, en respectant l'orientation
            if self.facing_left:
                self.image = pygame.transform.flip(self.idle_image, True, False)
            else:
                self.image = self.idle_image

        # Mise à jour de la position du rectangle du joueur
        self.rect.topleft = (self.x, self.y)

    # Gestion du saut du joueur
    def player_jump(self):
        # Contrôle du saut vertical
        if self.is_jumped:
            if self.jump_up >= 10:
                self.jump_down -= 1
                self.jump = self.jump_down
            else:
                self.jump_up += 1
                self.jump = self.jump_up
            
            if self.jump_down < 0:
                self.jump_up = 0
                self.jump_down = 5
                self.is_jumped = False
    
        # Calcul de la position verticale (saut)
        self.y -= (5 * self.jump / 2)
    
        # Courbe plus longue horizontalement : ajustement en fonction de la direction
        horizontal_curve_factor = 2  # Augmentez pour rendre la courbe plus longue
        if self.is_jumped:
            if self.facing_left:
                self.x -= horizontal_curve_factor  # Mouvement à gauche pendant le saut
            else:
                self.x += horizontal_curve_factor  # Mouvement à droite pendant le saut
    
    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))



                


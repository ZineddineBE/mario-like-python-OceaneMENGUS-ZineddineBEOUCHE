import pygame

class Player:
    def __init__(self, x, y, speed):
        self.x = x
        self.y = y
        self.width = 120
        self.height = 68
        self.speed = speed
        self.frame_index = 0
        self.animation_speed = 0.2
        self.walk_frames = self.load_walk_frames()  # Frames de marche
        self.image = self.walk_frames[self.frame_index]
        self.rect = self.image.get_rect(topleft=(self.x, self.y))
        
        # Variables de saut et gravité
        self.facing_left = False
        self.is_jumped = False
        self.velocity_y = 0  # Vitesse verticale
        self.gravity = 1     # Gravité pour rendre le saut plus naturel
        self.jump_strength = 15  # Force du saut
        self.number_of_jump = 0  # Compte le nombre de sauts
        self.jump_up = 0  
        self.jump_down = 0  

    def load_walk_frames(self):
        frames = []
        for i in range(1, 10):
            frame = pygame.image.load(f'assets/player/Walk/Walk ({i}).png').convert_alpha()
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

        # Limite la position horizontale aux bords de l'écran
        self.x = max(0, min(self.x, 930))

        # Gestion du saut : permet un saut seulement si `number_of_jump` est 0
        if self.number_of_jump == 0 and (keys[pygame.K_z] or keys[pygame.K_SPACE] or keys[pygame.K_UP]):
            self.is_jumped = True
            self.velocity_y = -self.jump_strength
            self.number_of_jump += 1  # Incrémente pour limiter à un saut

        # Applique la gravité si le joueur est en l'air
        if self.is_jumped:
            self.velocity_y += self.gravity
            self.y += self.velocity_y
            # Arrête le saut lorsque le joueur atteint le sol (ajuster la valeur selon le sol)
            if self.y >= 650:  # Ajuster "650" à la position du sol
                self.y = 650
                self.is_jumped = False
                self.velocity_y = 0
                self.number_of_jump = 0  # Réinitialise le nombre de sauts quand le joueur touche le sol

        # Choisir l'image du joueur en fonction de son état
        if self.moving:
            # Animation de marche
            self.frame_index += self.animation_speed
            if self.frame_index >= len(self.walk_frames):
                self.frame_index = 0
            self.image = self.walk_frames[int(self.frame_index)]
        else:
            # Image Idle lorsque le joueur est au repos
            idle = pygame.image.load(f'assets/player/Idle (1).png').convert_alpha()
            self.image = pygame.transform.scale(idle, (self.width, self.height))

        # Appliquer la direction gauche/droite en fonction de `facing_left`
        if self.facing_left:
            self.image = pygame.transform.flip(self.image, True, False)

        # Mise à jour de la position du rectangle du joueur
        self.rect.topleft = (self.x, self.y)

    # Gestion du saut du joueur
    def player_jump(self):
        if self.is_jumped:
            if self.jump_up >= 10:
                self.jump_down -= 1
                self.jump = self.jump_down
            else:
                self.jump_up += 1
                self.jump = self.jump_up
            
            if self.jump_down < 0 :
                self.jump_up = 0
                self.jump_down = 5
                self.is_jumped = False

        self.y = self.y - (5 * self.jump /2)

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))



                


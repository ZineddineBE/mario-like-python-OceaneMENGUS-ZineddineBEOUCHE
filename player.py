import pygame

class Player:
    def __init__(self, x, y, speed):
        self.x = x
        self.y = y
        self.width = 120
        self.height = 68
        self.speed = speed #Vitesse du joueur
        self.frame_index = 0 #Index de la frame actuelle pour l'animation
        self.animation_speed = 4 #Vitesse de changement des frames pour l'animation.
        self.frames = self.load_frames()
        self.image = self.frames[self.frame_index] #Image actuelle du joueur
        self.rect = self.image.get_rect(topleft=(self.x, self.y))
        self.facing_left = False
        self.moving = False
        self.jump = 0
        self.jump_up = 0
        self.jump_down = 5
        self.number_of_jump = 0
        self.is_jumped = False

    def load_frames(self):
        frames = []
        for i in range(1, 10):
            frame = pygame.image.load(f'assets/player/Walk/Walk ({i}).png').convert_alpha()
            frame = pygame.transform.scale(frame, (self.width, self.height))
            frames.append(frame)
        return frames

    def update(self, keys):
        self.moving = False
        # Déplacement du Player
        if keys[pygame.K_q] or keys[pygame.K_LEFT]:
            if not self.facing_left:  # Si le personnage ne fait pas déjà face à la gauche
                self.facing_left = True
                self.image = pygame.transform.flip(self.image, True, False)  # Retourne l'image vers la gauche
            self.x -= self.speed
            self.moving = True
            if self.x < 0:
                self.x = 0

        if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            if self.facing_left:  # Si le personnage ne fait pas déjà face à la droite
                self.facing_left = False
                self.image = pygame.transform.flip(self.image, True, False)  # Retourne l'image vers la droite
            self.x += self.speed
            self.moving = True
            if self.x >= 930:
                self.x = 0
        
        if keys[pygame.K_z] or keys[pygame.K_SPACE] or keys[pygame.K_UP]:
            self.is_jumped = True
            self.number_of_jump += 1

        # Créer l'animation du Player
        if self.moving == True:
            self.frame_index += 0.2
            if self.frame_index >= len(self.frames):
                self.moving = False
                self.frame_index = 0
                
            self.image = self.frames[int(self.frame_index)]
            if self.facing_left:
                self.image = pygame.transform.flip(self.image, True, False)

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))
    
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

                


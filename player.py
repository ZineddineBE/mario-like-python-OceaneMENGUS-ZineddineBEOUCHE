import pygame

class Player:
    def __init__(self, x, y, speed):
        self.x = x
        self.y = y
        self.speed = speed #Vitesse du joueur
        self.frame_index = 0 #Index de la frame actuelle pour l'animation
        self.animation_speed = 3 #Vitesse de changement des frames pour l'animation.
        self.frames = self.load_frames()
        self.image = self.frames[self.frame_index] #Image actuelle du joueur
        self.moving = False

    def load_frames(self):
        frames = []
        for i in range(1, 11):
            frame = pygame.image.load(f'assets/player/Walk ({i}).png').convert_alpha()
            frame = pygame.transform.scale(frame, (120, 68))
            frames.append(frame)
        return frames

    def update(self, keys):
        self.moving = False
        # Déplacement du Player
        if keys[pygame.K_q] or keys[pygame.K_LEFT]:
            self.x -= self.speed
            self.moving = True
            if self.x < 0:
                self.x = 0

        elif keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            self.x += self.speed
            self.moving = True
            if self.x >= 930:
                self.x = 0

        # Créer l'animation du Player
        if self.moving:
            if pygame.time.get_ticks() % self.animation_speed == 0:
                self.frame_index = (self.frame_index + 1) % len(self.frames)
        else:
            self.frame_index = 0

        self.image = self.frames[self.frame_index]

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))

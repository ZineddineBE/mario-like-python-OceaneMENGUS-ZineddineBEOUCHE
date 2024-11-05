import pygame

class AnimateSprite(pygame.sprite.Sprite):

    def __init__(self, sprite_name):
        super().__init__()
        self.image = pygame.image.load(f'Mario/assets/player/{sprite_name}.png')

def load_animation_images(sprite_name):
    images = []
    path = f"Mario/assets/player/{sprite_name}"
    for i in range(10):
        image_path = path + i + '.png'
        images.append(pygame.image.load(image_path)) #14:50min vidéo 8/10
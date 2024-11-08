# import pygame

# class AnimateSprite(pygame.sprite.Sprite):

#     def __init__(self, sprite_name):
#         super().__init__()
#         self.image = pygame.image.load(f'Mario/assets/player/{sprite_name}.png')
#         self.current_image = 0
#         self.images = animations.get(sprite_name)

#     def animate(self):
#         self.current_image += 1

#         if self.current_image >= 10:
#             self.current_image = 0

#         self.image = self.images[self.current_image]


# def load_animation_images(sprite_name):
#     images = []
#     path = f"Mario/assets/player/{sprite_name}"
#     for i in range(1, 10):
#         image_path = path + str(i) + '.png'
#         images.append(pygame.image.load(image_path)) #14:50min vidéo 8/10
#     return images

# animations = {
#     'Walk' : load_animation_images('Walk/Walk')
# }
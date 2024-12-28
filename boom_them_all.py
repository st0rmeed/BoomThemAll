import pygame
import os
import random

pygame.init()

screen = pygame.display.set_mode((500, 500))


class Bomb(pygame.sprite.Sprite):
    def __init__(self, image_path):
        super().__init__()
        self.image = pygame.image.load(image_path)
        self.rect = self.image.get_rect()

    def change_image(self, new_image_path):
        self.image = pygame.image.load(new_image_path)
        self.rect = self.image.get_rect(x=self.rect.x, y=self.rect.y)


all_sprites = pygame.sprite.Group()

bomb_image_path = os.path.join('data', 'bomb.png')
for _ in range(20):
    bomb = Bomb(bomb_image_path)
    bomb.rect.x = random.randint(0, 450)
    bomb.rect.y = random.randint(0, 449)
    all_sprites.add(bomb)

clock = pygame.time.Clock()

running = True
while running:
    clock.tick(30)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = event.pos
            for bomb in all_sprites:
                if bomb.rect.collidepoint(mouse_pos):
                    bomb.change_image(os.path.join('data', 'boom.png'))

    screen.fill('black')
    all_sprites.draw(screen)
    pygame.display.flip()

pygame.quit()

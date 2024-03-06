#flappy bird

#Cod För att kunna se spelet
import pygame
from pygame.locals import *
pygame.init()

screen_width = 500
screen_heighet = 500

#Variabler för skärmen
screen = pygame.display.set_mode((screen_width, screen_heighet))
pygame.display.set_caption("flappy_bird Alican")

bg = pygame.image.load("16364.png")

#Laddaner bilder

class Bird(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.image.load
        self.image=pygame.image.load(f'fågel1.png')
        self.rect=self.image.get_rect()
        self.rect.center = (x, y)


bird_group =




    screen.blit(bg, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    pygame.display.update()
pygame.quit()


run = True
while run:





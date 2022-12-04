import pygame
import time
import math
from utils import scale_image

GRASS = scale_image(pygame.image.load("images/grass.jpg"), 2.5)
TRACK = scale_image(pygame.image.load("images/track.png"), 0.9)

TRACK_BORDER = pygame.image.load("images/track-border.png")
FINISH = pygame.image.load("images/finish.png")

RED_CAR = scale_image(pygame.image.load("images/red-car.png"), 0.55)
GREEN_CAR = scale_image(pygame.image.load("images/green-car.png"), 0.55)

#Setting Up My Game Window
WIDTH, HEIGHT = TRACK.get_width(), TRACK.get_height()
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Racing Game!")

FPS = 60

def draw(win, images):
    for img, pos in images:
        win.blit(img, pos)

run = True
clock = pygame.time.Clock()
images = [(GRASS, (0, 0)), (TRACK, (0, 0))]

while run:
    clock.tick(FPS) #Game limited to 60 Frames Per Second

    draw(WIN, images)
    pygame.display.update()
        

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            break

pygame.quit()
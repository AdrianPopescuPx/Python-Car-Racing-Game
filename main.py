import pygame
import time
import math

GRASS = pygame.image.load("images/grass.jpg")
TRACK = pygame.image.load("images/track.png")

TRACK_BORDER = pygame.image.load("images/track-border.png")
FINISH = pygame.image.load("images/finish.png")

RED_CAR = pygame.image.load("images/red-car.png")
GREEN_CAR = pygame.image.load("images/green-car.png")

#Setting Up My Game Window
WIDTH, HEIGHT = TRACK.get_width(), TRACK.get_height()
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Racing Game!")
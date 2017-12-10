import sys, pygame, time, os, io
from pygame.locals import *
pygame.init()

mouse = pygame.mouse

size = width, height = 960, 720

screen = pygame.display.set_mode(size)

canvas = screen.copy()

BLACK = pygame.Color(0,0,0)
WHITE = pygame.Color(255,255,255)

fill_color = 255, 127, 64

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    screen.fill(WHITE)
    pygame.display.update()

# ball = pygame.image.load("/Users/ben/Desktop/ball.gif")
# ballrect = ball.get_rect()
#
#     pygame.display.flip()
import sys, pygame, time, os, io
from pygame.locals import *
pygame.init()

pygame.display.set_caption('Traceorama')
mouse = pygame.mouse

size = width, height = 960, 720

screen = pygame.display.set_mode(size)

canvas = screen.copy()

BLACK = pygame.Color(0,0,0)
WHITE = pygame.Color(255,255,255)

canvas.fill(WHITE)

quit_pressed = False

while not quit_pressed:
    left_pressed, middle_pressed, right_pressed = mouse.get_pressed()
    for event in pygame.event.get():
        if event.type == QUIT:
            quit_pressed = True
            break
        elif left_pressed:
            pygame.draw.circle(canvas, BLACK, (pygame.mouse.get_pos()), 5)
    if not quit_pressed:
        screen.fill(WHITE)
        screen.blit(canvas, (0,0))
        pygame.draw.circle(screen, BLACK, (pygame.mouse.get_pos()), 5)
        pygame.display.update()
    else:
        break
pygame.image.save(canvas,'/Users/ben/Desktop/traceorama_picture.jpeg')
pygame.quit()
sys.exit()




# ball = pygame.image.load("/Users/ben/Desktop/ball.gif")
# ballrect = ball.get_rect()
#
#     pygame.display.flip()
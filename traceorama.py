import sys, pygame, time
pygame.init()


size = width, height = 320, 240

fill_color = 255, 127, 64

screen = pygame.display.set_mode(size)

ball = pygame.image.load("/Users/ben/Desktop/ball.gif")
ballrect = ball.get_rect()


while 1:
    speed = [0,0]
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT and ballrect.left > 0:
                speed = [-5,0]
            if event.key == pygame.K_RIGHT and ballrect.right < width:
                speed = [5,0]
            if event.key == pygame.K_UP and ballrect.top > 0:
                speed = [0,-5]
            if event.key == pygame.K_DOWN and ballrect.bottom < height:
                speed = [0,5]

    ballrect = ballrect.move(speed)


    screen.fill(fill_color)
    screen.blit(ball, ballrect)
    pygame.display.flip()
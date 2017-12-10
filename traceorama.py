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
            if event.key == pygame.K_LEFT:
                speed = [-1,0]
            if event.key == pygame.K_RIGHT:
                speed = [1,0]
            if event.key == pygame.K_UP:
                speed = [0,-1]
            if event.key == pygame.K_DOWN:
                speed = [0,1]

    if ballrect.left < 0 or ballrect.right > width:
        speed[0] = 0
    if ballrect.top < 0 or ballrect.bottom > height:
        speed[1] = 0

    ballrect = ballrect.move(speed)


    screen.fill(fill_color)
    screen.blit(ball, ballrect)
    pygame.display.flip()
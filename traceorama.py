import sys, pygame, time, os, io
from pygame.locals import *
from google.cloud import vision
from google.cloud.vision import types

pygame.init()


def load_image(file_name):
    with io.open(file_name, 'rb') as image_file:
        content = image_file.read()
    return types.Image(content=content)

def construct_fullpath(folder_name, file_name):
    return os.path.join(os.path.dirname(folder_name), file_name)

def get_labels(client, image):
    response = client.label_detection(image=image)  ##The magic happens
    return response.label_annotations

def get_descriptions(labels):
    return[label.description for label in labels]

def print_descriptions(descriptions):
    print('label descriptions:')
    for description in descriptions:
        print(description)

def flash_image(image_file_name, width, height, screen):
    image = pygame.image.load(image_file_name)
    image = pygame.transform.scale(image, (width,height))
    screen.blit(image,(0,0))
    pygame.display.update()
    time.sleep(3)
    screen.fill(WHITE)
    pygame.display.update()

traceorama_picture_file_name = "traceorama_pictures.jpg"
client = vision.ImageAnnotatorClient()
file_name = construct_fullpath('/Users/ben/Downloads/', traceorama_picture_file_name)

pygame.display.set_caption('Traceorama')
mouse = pygame.mouse

size = width, height = 960, 720

screen = pygame.display.set_mode(size)

canvas = screen.copy()

BLACK = pygame.Color(0,0,0)
WHITE = pygame.Color(255,255,255)

canvas.fill(WHITE)

flash_image('/Users/ben/Desktop/Christmas_Tree_Picture.png', width, height, screen)
# christmas_tree_image = pygame.image.load('/Users/ben/Desktop/Christmas_Tree_Picture.png')
#     christmas_tree_image = pygame.transform.scale(christmas_tree_image, (width,height))
#     screen.blit(christmas_tree_image,(0,0))
#     pygame.display.update()
#     time.sleep(3)
#     canvas.fill(WHITE)

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

pygame.image.save(canvas, file_name)

image = load_image(file_name)

labels = get_labels(client, image)

descriptions = get_descriptions(labels)

print_descriptions(descriptions)

pygame.quit()
sys.exit()




# ball = pygame.image.load("/Users/ben/Desktop/ball.gif")
# ballrect = ball.get_rect()
#
#     pygame.display.flip()
import json
import pygame, sys
from setings import *
from Map import Map

#Pygame setup
pygame.init()
screen_width = 800
screen_height = 800

screen = pygame.display.set_mode((screen_width,screen_height))
clock = pygame. time.Clock()
Map = Map(worldMap,screen)

#user settings setup
user_json = json.load(open("/home/akako/pixelByPixel/user.json"))

fps = user_json["max_fps"]

#loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.set_caption(str(int(clock. get_fps())),"fps")

    screen.fill('black')

    Map.run()

    pygame.display.update()
    clock.tick(fps)
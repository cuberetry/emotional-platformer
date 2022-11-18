import cv2
import pygame
import keras

pygame.init()

win = pygame.display.set_mode((500, 500)) # create window w/ 500 width, 500 height

pygame.display.set_caption("First Game")

x = 50
y = 50
width = 40
height = 60
vel = 5

run = True

while run:
    pygame.time.delay(100) # delay 0.1 second
    for event in pygame.event.get(): # loop through a list of keyboard or mouse
        if event.type == pygame.QUIT:
            run = False

pygame.quit()



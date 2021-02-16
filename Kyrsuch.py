import pygame
import random
import sys
import time
import turtle


pygame.init()

blue = (135, 206, 250)
balck = (0, 0, 0)
white = (255, 255, 255)

gravity = 10  # speed
FPS = 60  # Frames Per second
width = 1200
height = 980
snowSize = 8
snowNum = 300

varHeight = height
snowColor = white
bgColor = blue

game0ver = False

display = pygame.display.set_mode((width, height))
pygame.display.set_caption('Snow')

snowFlake = []

for q in range(snowNum):
    x = random.randrange(0, width)
    y = random.randrange(0, varHeight)
    snowFlake.append([x, y])
clock = pygame.time.Clock()
while not game0ver:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game0ver = True

    display.fill(bgColor)

    for i in snowFlake:
        i[1] += gravity

        pygame.draw.circle(display, snowColor, i, snowSize)

        if i[1] > varHeight:
            i[1] = random.randrange(-50, -5)
            i[0] = random.randrange(width)

    pygame.display.flip()
    clock.tick(FPS)

import pygame
import pandas as pd
import numpy as np
import random
import time
import sys

#Constants
#DIMENSIONS
WIDTH = 800
HEIGHT = 800
LINE_WIDTH = 15
BOARD_ROWS = 3
BOARD_COLS = 3

SPACE = 55

#RGB: RED, GREEN, BLUE
RED = (255, 0, 0)
BG_COLOR = (28, 170, 156)
LINE_COLOR = (23, 145, 135)
screen = pg.display.set_mode( (WIDTH, HEIGHT) )
pg.display.set_caption( 'DrugLord' )
screen.fill( BG_COLOR )
CIRCLE_COLOR = (239, 231, 200)
CROSS_COLOR = (66, 66, 66)




#Main Loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.constants.MOUSEBUTTONDOWN:

            MouseX = event.pos[0] # x
            MouseY = event.pos[1] # y

    pg.display.update()
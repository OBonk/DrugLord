import pygame
import pandas as pd
import numpy as np
import random
import time
import sys

#Constants
#DIMENSIONS
WIDTH = 600
HEIGHT = 800
LINE_WIDTH = 15
BOARD_ROWS = 3
BOARD_COLS = 3

SPACE = 55

#RGB: RED, GREEN, BLUE
RED = (255, 0, 0)
BG_COLOR = (172, 172, 172)
screen = pygame.display.set_mode( (WIDTH, HEIGHT) )
pygame.display.set_caption( 'DrugLord' )
screen.fill( BG_COLOR )


def event_screen():
    # Initialing Color
    color = (255, 255, 255)
    # Drawing Rectangle
    pygame.draw.rect(screen, color, pygame.Rect(20, 20, 560, 200))
    #why flip??????
    pygame.display.flip()

#do not know where to put this
event_screen()

def market_screen():
    color = (255, 255, 255)
    # Drawing Rectangle
    pygame.draw.rect(screen, color, pygame.Rect(20, 240, 140, 540))
    pygame.display.flip()

#do not know where to put this
market_screen()

def button_screen():
    color = (255, 255, 255)
    # Drawing Rectangle
    pygame.draw.rect(screen, color, pygame.Rect(180, 240, 140, 540))
    pygame.display.flip()

button_screen()

def pockets_screen():
    color = (255, 255, 255)
    # Drawing Rectangle
    pygame.draw.rect(screen, color, pygame.Rect(340, 240, 240, 260))
    pygame.display.flip()

pockets_screen()

def status_screen():
    color = (255, 255, 255)
    # Drawing Rectangle
    pygame.draw.rect(screen, color, pygame.Rect(340, 520, 240, 260))
    pygame.display.flip()

status_screen()


def buy_button():
    color = (175, 175, 175)
    # Drawing Rectangle                        right down width height
    pygame.draw.rect(screen, color, pygame.Rect(190, 250, 120, 40))
    pygame.display.flip()

buy_button()

def sell_button():
    color = (175, 175, 175)
    # Drawing Rectangle                        right down width height
    pygame.draw.rect(screen, color, pygame.Rect(190, 300, 120, 40))
    pygame.display.flip()

sell_button()

#Main Loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.constants.MOUSEBUTTONDOWN:

            MouseX = event.pos[0] # x
            MouseY = event.pos[1] # y

    pygame.display.update()
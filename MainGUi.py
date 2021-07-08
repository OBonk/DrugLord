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
    pygame.draw.rect(screen, color, pygame.Rect(190, 250, 120, 30))
    pygame.display.flip()

buy_button()

def sell_button():
    color = (175, 175, 175)
    # Drawing Rectangle                        right down width height
    pygame.draw.rect(screen, color, pygame.Rect(190, 290, 120, 30))
    pygame.display.flip()

sell_button()

def dump_button():
    color = (175, 175, 175)
    # Drawing Rectangle                        right down width height
    pygame.draw.rect(screen, color, pygame.Rect(190, 330, 120, 30))
    pygame.display.flip()

dump_button()

def places_button():
    color = (175, 175, 175)
    # Drawing Rectangle                        right down width height
    pygame.draw.rect(screen, color, pygame.Rect(190, 370, 120, 30))
    pygame.display.flip()

places_button()

def info_button():
    color = (175, 175, 175)
    # Drawing Rectangle                        right down width height
    pygame.draw.rect(screen, color, pygame.Rect(190, 410, 120, 30))
    pygame.display.flip()

info_button()


def stay_button():
    color = (175, 175, 175)
    # Drawing Rectangle                        right down width height
    pygame.draw.rect(screen, color, pygame.Rect(190, 470, 120, 30))
    pygame.display.flip()

stay_button()

def fly_button():
    color = (175, 175, 175)
    # Drawing Rectangle                        right down width height
    pygame.draw.rect(screen, color, pygame.Rect(190, 510, 120, 30))
    pygame.display.flip()

fly_button()

def sound_button():
    color = (175, 175, 175)
    # Drawing Rectangle                        right down width height
    pygame.draw.rect(screen, color, pygame.Rect(200, 590, 20, 20))
    pygame.display.flip()

sound_button()

def about_button():
    color = (175, 175, 175)
    # Drawing Rectangle                        right down width height
    pygame.draw.rect(screen, color, pygame.Rect(190, 620, 120, 30))
    pygame.display.flip()

about_button()

def docs_button():
    color = (175, 175, 175)
    # Drawing Rectangle                        right down width height
    pygame.draw.rect(screen, color, pygame.Rect(190, 660, 120, 30))
    pygame.display.flip()

docs_button()

def High_Score_button():
    color = (175, 175, 175)
    # Drawing Rectangle                        right down width height
    pygame.draw.rect(screen, color, pygame.Rect(190, 700, 120, 30))
    pygame.display.flip()

High_Score_button()

def Quit_button():
    color = (175, 175, 175)
    # Drawing Rectangle                        right down width height
    pygame.draw.rect(screen, color, pygame.Rect(190, 740, 120, 30))
    pygame.display.flip()

Quit_button()


#Main Loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.constants.MOUSEBUTTONDOWN:

            MouseX = event.pos[0] # x
            MouseY = event.pos[1] # y

    pygame.display.update())
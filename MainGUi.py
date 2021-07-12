import pygame
import pandas as pd
import numpy as np
import random
import time
import sys
from collections import namedtuple

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

def main_Buttons(x1,y1):
    buttonStruct = namedtuple("buttonStruct", "x y width height name")


    b1 = buttonStruct(x=190, y=250, width= 120, height=30, name="Buy")
    b2 = buttonStruct(x=190, y=290, width=120, height=30, name="Sell")
    b3 = buttonStruct(x=190, y=330, width=120, height=30, name="Dump")
    b4 = buttonStruct(x=190, y=370, width=120, height=30, name="Places")
    b5 = buttonStruct(x=190, y=410, width=120, height=30, name="Info")
    b6 = buttonStruct(x=190, y=470, width=120, height=30, name="Stay")
    b7 = buttonStruct(x=190, y=510, width=120, height=30, name="Fly")
    b8 = buttonStruct(x=200, y=590, width=20, height=20, name="Sound")
    b9 = buttonStruct(x=190, y=620, width=120, height=30, name="About")
    b10 = buttonStruct(x=190, y=660, width=120, height=30, name="Docs")
    b11 =buttonStruct(x=190, y=700, width=120, height=30, name="High_Score")
    b12 = buttonStruct(x=190, y=740, width=120, height=30, name="Quit")

    buts = [b1, b2, b3, b4, b5, b6, b7, b8, b9, b10, b11, b12]
    x1 = int(input("input x of click: "))
    y1 = int(input("input y of click: "))
    for but in buts:
        print(but.x)
        if but.x <= x1 <= (but.x + but.width) and but.y <= y1 <= (but.y + but.height):
            return but.name
    return None

def player_struct():
    playerStruct = namedtuple("playerStruct","location inventory balance")
    p1 = playerStruct(location= "Bristol", inventory= {"Cocaine":0, "Crack":0, "LSD":0, "Ecstasy":0,"Weed": 0}, balance=0)
    arrofplayers = [p1]

    for names in arrofplayers:
        if names.location == "London":
            print(names.inventory)

def dictionary_places():
    BirminghamDF = pd.read_csv("Birmingham.csv")
    BristolDF = pd.read_csv("BristolDL.csv")
    LondonDF = pd.read_csv("LondonDL.csv")
    NottinghamDF = pd.read_csv("NottinghamDL.csv")

    Dict = {1: ' BirminghamDF', 2: 'BristolDF ', 3: 'LondonDF', 4:'NottinghamDF'}


#def hover_check():

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

def main_loop():
    color = (175, 175, 175)
    # Drawing Rectangle                        right down width height
    pygame.draw.rect(screen, color, pygame.Rect(190, 740, 120, 30))
    pygame.display.flip()
    #define playerStruct and player here
    color_white = (255, 255, 255)
    color_light = (180, 180, 180)
    color_dark = (110, 110, 110)
    width = screen.get_width()
    height = screen.get_height()
    pygame.font.init()
    smallfont = pygame.font.SysFont('Arial', 30)
    text = smallfont.render('Quit', True, color_white)
    quit_text = text.get_rect(center=(250,755))
    screen.blit(text, quit_text)
    #market_dict["london"] = load_pricing("London.csv")
    while True:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                sys.exit()
            if e.type == pygame.MOUSEBUTTONDOWN:

                mouse = pygame.mouse.get_pos()
                # prints position of mouse clicked
                print(f"Mouse clicked at {mouse[0]},{mouse[1]}")
                if 190 <= mouse[0] <= 190 + 120 and 740 <= mouse[1] <= 740 + 30:
                    sys.exit()

        mouse = pygame.mouse.get_pos()
        #hover_check(mouse[0],mouse[1])
        #market at 20,240 and is 140 wide and 540 long
        #button at is 180,240 and 140 wide and 540 long
        if 180 <= mouse[0] <= 320 and 240 <= mouse[1] <= 780:
            #in button area
            print("cool you are in button area")
            butClicked = main_Buttons(mouse[0],mouse[1])
            #calls function named after button
            eval(butClicked+"()")
        elif 20 <= mouse[0] <= 160 and 240 <= mouse[1] <= 780:
            #in market area
            print("cool you are in market area")
            #hover_checkM(mouse[0,mouse[1]])

        if 190 <= mouse[0] <= 190 + 120 and 740 <= mouse[1] <= 740 + 30:
            pygame.draw.rect(screen, color_light, [190, 740, 120, 30])
            screen.blit(text, quit_text)
        else:
            pygame.draw.rect(screen, color_dark, [190, 740, 120, 30])
            screen.blit(text, quit_text)


        #screen.blit(text, (width / 2 + 50, height / 2))
        pygame.display.update()

main_loop()

def mouse_clicking():
    pass

def load_pricing(filename):

    return #the dataframe


def Market():
    # Initialise data to Dicts of series.
    Standard_Pricing = {'Current Price': pd.Series([1600, 800, 400, 200, 100],
                                index=["Cocaine", "Crack", "LSD", "Ecstasy", "Weed"]),
                        'Min Price': pd.Series([1200, 600, 300, 150, 75],
                                index=["Cocaine", "Crack", "LSD", "Ecstasy", "Weed"]),
                        'Max Price': pd.Series([2000, 1200, 500, 250, 125],
                                index=["Cocaine", "Crack", "LSD", "Ecstasy", "Weed"]),
                        'Detection Per a Unit': pd.Series([1, 0.5, 0.25, 0.125, 0.005],
                                index=["Cocaine", "Crack", "LSD", "Ecstasy", "Weed"]),
                        'Special event increase %': pd.Series([200, 150, 300, 500, 600],
                                index=["Cocaine", "Crack", "LSD", "Ecstasy", "Weed"]),
                        'Special event decrease %': pd.Series([-90, -90, -90, -90, -90],
                                index=["Cocaine", "Crack", "LSD", "Ecstasy", "Weed"]),
                        'Quantity': pd.Series([5, 10, 20, 40, 80],
                                index=["Cocaine", "Crack", "LSD", "Ecstasy", "Weed"])
                        }

    df = pd.DataFrame(Standard_Pricing)

    '''# Create DataFrame
    df = pd.DataFrame(data)
    London_dict = {
        "Drug": "Cocaine","Crack","LSD","Ecstasy","Weed",
        "price": "1000","800","600","200","50",
        "Variaion": "+-40%","+-80%","+-60%","+-20%"
    }'''





#Main Loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.constants.MOUSEBUTTONDOWN:

            MouseX = event.pos[0] # x
            MouseY = event.pos[1] # y

    pygame.display.update()
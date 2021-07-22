from tkinter import *
import tkinter.font as font
from collections import namedtuple
import pandas as pd
from pandastable import Table, TableModel
#from tkinter.ttk import *
import sys
import random
#import Pillow not working do not know why
from PIL import ImageTk, Image
#import sqlite3

#splash_root = Tk()
#splash_root.geometry("800x600")

root = Tk()
root.title("Get guuuuuddddd")
#cannt get this to work
#root.iconbitmap("marioMushroom.png")
#myImage = ImageTK.PhotoImage(Image.open("Whatever Pic I Need"))
#my_label = Label(image =  myImage)
root.geometry("800x600")
root.configure(background='#D6EAF8')


bg1 = "#F1948A"
fg1 = "white"
hlbg = "#8E44AD"
button1 = "#FCF3CF"
button2 = "#85C1E9"
text1 = "#85C1E9"
#frame = LabelFrame(root, text = "Buy Inventory", padx = 50, pady = 50)
#frame.grid(padx = 10, pady = 10, row =1,column = 1)

#does not work
#window_main = root.Tk(className='Tkinter - TutorialKart', )
#window_main.geometry("600x800")

#creating a label widget
def Buy():

    my_label = Label(root, text = "Hello Yankerrrr MOOOOOOO! XXXX", padx = 50, pady = 50, font = buttonFont)
    my_label.grid(row= 0, column =3)

def Remove():
    pass

def Sell():
    pass

def Sail():
    pass

def StayHere(Market,BirminghamDF):
    g = BirminghamDF
    frame = Frame(BuyScreen)
    frame.pack(fill='both', expand=True)

    pt = Table(frame, dataframe=g )
    pt.show()

def Places():
    pass

def Options():
    pass

def HighScore():
    pass

def player_struct():
    playerStruct = namedtuple("playerStruct","location inventory balance")
    p1 = playerStruct(location= "Bristol", inventory= {"Cocaine":0, "Crack":0, "LSD":0, "Ecstasy":0,"Weed": 0, }, balance=0, Health = 100)
    arrofplayers = [p1]

def dictionary_places(StayHere):
    BirminghamDF = pd.read_csv("Birmingham.csv")
    BristolDF = pd.read_csv("BristolDL.csv")
    LondonDF = pd.read_csv("LondonDL.csv")
    NottinghamDF = pd.read_csv("NottinghamDL.csv")

    Dict = {1: ' BirminghamDF', 2: 'BristolDF ', 3: 'LondonDF', 4:'NottinghamDF'}

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

def Quit():
    root.destroy()




#Constants hahaa

#inside button, if you have state = DISABLED it stops the button from being clicked

#The Font very Important
buttonFont = font.Font(family='Helvetica', size=10, weight='bold')

#clicked = StringVar() #Do not know how to change text for dropdown box
#drop = OptionMenu(root,clicked, "New Game", "Save Game","Options","Help")
#drop.grid(row= 1, column =1) FFB374


DisplayFrame = LabelFrame(root, text = "Action Screen",width = 750, height = 125,highlightthickness=4,
                      highlightbackground= hlbg, padx = 10, pady = 10, bg = bg1,fg = fg1)
DisplayFrame.grid(row = 1 ,column = 1, columnspan = 3, rowspan = 1,padx = 5, pady = 5)
DisplayScreen = Canvas(DisplayFrame, width = 750, height = 125, bg = "white", highlightthickness=4)
DisplayScreen.pack()

# Holds All the Buttons

ButtonFrame = LabelFrame(root, text = "Buttons",highlightthickness=4, highlightbackground =hlbg
                      , bg = bg1,fg = fg1)
ButtonFrame.grid(row = 2 ,column = 2, columnspan = 1)

# Holds both the inventory and data screen frame, this frame should be invisable
RHS_Frame = LabelFrame(root)
RHS_Frame.grid(row = 2 ,column = 3, columnspan = 1, rowspan = 1)

InventoryFrame = LabelFrame(RHS_Frame, text = "Inventory",width = 160, height = 160,highlightthickness=4,
                      highlightbackground =hlbg,padx = 10, pady = 10, bg = bg1,fg = fg1)
InventoryFrame.grid(row = 1 ,column = 1, columnspan = 1, rowspan = 1)
InventoryScreen = Canvas(InventoryFrame, width = 180, height = 140,  highlightthickness=4)
InventoryScreen.pack()

DataScreenFrame = LabelFrame(RHS_Frame, text = "Data Screen",width = 160, height = 160,highlightthickness=4,
                      highlightbackground = hlbg,padx = 10, pady = 10, bg = bg1,fg = fg1)
DataScreenFrame.grid(row = 3 ,column = 1, columnspan = 1, rowspan = 1)
DataScreen = Canvas(DataScreenFrame, width = 180, height = 140,  highlightthickness=4)
DataScreen.pack()

# Buy Frame and person frame
LHS_Frame = LabelFrame(root)
LHS_Frame.grid(row = 2 ,column = 1, columnspan = 1, rowspan = 1)

BuyScreenFrame = LabelFrame(LHS_Frame, text = "Buy Screen", width = 160, height = 160,highlightthickness=4,
                      highlightbackground =hlbg,padx = 10, pady = 10, bg = bg1,fg = fg1)
BuyScreenFrame.grid(row = 1 ,column = 1, columnspan = 1, rowspan = 1)
BuyScreen = Canvas(BuyScreenFrame, width = 180, height = 140,  highlightthickness=4)
BuyScreen.pack()

PersonFrame = LabelFrame(LHS_Frame, text = "Your Stats",width = 160, height = 160,highlightthickness=4,
                      highlightbackground = hlbg,padx = 10, pady = 10, bg = bg1,fg = fg1)
PersonFrame.grid(row = 2 ,column = 1, columnspan = 1, rowspan = 1)
Person = Canvas(PersonFrame, width = 180, height = 140,  highlightthickness=4)
Person .pack()

# Buy_Sell_Button_Frame
#Buy_Sell_Button_Frame = LabelFrame(root,width = 50, height = 10)
#Buy_Sell_Button_Frame.grid(row= 2, column =2,rowspan = 1, padx = 10, pady = 10)
myButtonBuy = Button(ButtonFrame, text = "Buy", fg = button2, width= 8,
                     bg = button1, command = Buy, borderwidth=10, font = buttonFont)
myButtonBuy.grid(row = 1 ,column = 1, columnspan = 1, rowspan = 1,padx = 2, pady = 2)

myButtonDrop = Button(ButtonFrame, text = "Remove", fg = button2, width= 8,
                     bg = button1, command = Remove, borderwidth=10, font = buttonFont)
myButtonDrop.grid(row = 1 ,column = 2, columnspan = 1, rowspan = 1,padx = 2, pady = 2)

myButtonSell = Button(ButtonFrame, text = "Sell", fg = button2, width= 8,
                      bg = button1, command = Sell,borderwidth=10, font = buttonFont)
myButtonSell.grid(row = 1 ,column = 3, columnspan = 1, rowspan = 1,padx = 2, pady = 2)



# Move Frame
#MoveFrame = LabelFrame(root,width = 50, height = 10)
#MoveFrame.grid(row= 4, column =2)

myButtonStayHere = Button(ButtonFrame, text = "Stay Here", fg = button2, width= 8,
                      bg = button1, command = StayHere,borderwidth=10, font = buttonFont)
myButtonStayHere.grid(row = 2 ,column = 2, columnspan = 1, rowspan = 1,padx = 2, pady = 2)

myButtonPlaces = Button(ButtonFrame, text = "Places", fg = button2,width= 8,
                      bg = button1, command = Places,borderwidth=10, font = buttonFont)
myButtonPlaces.grid(row = 2 ,column = 1, columnspan = 1, rowspan = 1,padx = 2, pady = 2)

myButtonSail = Button(ButtonFrame, text = "Sail", fg = button2,width= 8,
                     bg = button1, command = Sail, borderwidth=10, font = buttonFont)
myButtonSail.grid(row = 2 ,column = 3, columnspan = 1, rowspan = 1,padx = 2, pady = 2)


# Options
myButtonOptions = Button(ButtonFrame, text = "Options", fg = button2,width= 8,
                     bg = button1, command = Options, borderwidth=10, font = buttonFont)
myButtonOptions.grid(row = 3 ,column = 2, columnspan = 1, rowspan = 1,padx = 2, pady = 2)



#High Score

myButtonHighScore = Button(ButtonFrame, text = "High Score", fg = button2,width= 8,
                      bg = button1, command = HighScore,borderwidth=10, font = buttonFont)
myButtonHighScore.grid(row = 4 ,column = 2, columnspan = 1, rowspan = 1,padx = 2, pady = 2)



r = IntVar()
Checkbutton(ButtonFrame, text = "Sound On/Off", variable = r).grid(row= 5, column =2)
#Radiobutton(root, text = "Sound Off", variable = r, value =1,command=lambda: Sound(r.get)).grid(row= 4, column =1)

#Quit Button
myButtonQuit = Button(ButtonFrame, text = "Quit", fg = button2,width= 8,
                      bg = button1, command = Quit,borderwidth=10, font = buttonFont)
myButtonQuit.grid(row = 6 ,column = 2, columnspan = 1, rowspan = 1,padx = 2, pady = 2)




#e = Entry(root, width = 50, borderwidth=10)
#e.grid(row= 0, column =2)

#textBox = root.Enter(text="Placeholder text").grid(row= 0, column =0)
#you can have .pack at the end orrrrrrr myButton.pack just underneath









root.mainloop()
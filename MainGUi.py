from tkinter import *
import tkinter.font as font
from collections import namedtuple
import pandas as pd
import numpy as np
from pandastable import Table, TableModel
from tkinter.ttk import Treeview,Style
import sys
import random
import time
#import Pillow not working do not know why
from PIL import ImageTk, Image
#import sqlite3

#splash_root = Tk()
#splash_root.geometry("800x600")

root = Tk()
root.title("Get guuuuuddddd")
style = Style(root)
style.configure('Treeview', rowheight=15)
#cannt get this to work
#root.iconbitmap("marioMushroom.png")
#myImage = ImageTK.PhotoImage(Image.open("Whatever Pic I Need"))
#my_label = Label(image =  myImage)
root.geometry("800x600")
root.configure(background='#D6EAF8')

#Loading_Screen = Canvas(root, width = 800, height = 600, bg = "white")
#Loading_Screen.pack()
#root.update()
#time.sleep(5)
#Loading_Screen.pack_forget()
#Creating dictionary of dataframes
#BirminghamDF = pd.read_csv("Birmingham.csv")
#BristolDF = pd.read_csv("BristolDL.csv")
#LondonDF = pd.read_csv("LondonDL.csv")
#NottinghamDF = pd.read_csv("NottinghamDL.csv")

#Dictofplaces = {'Birmingham': BirminghamDF, 'Bristol': BristolDF, 'London': LondonDF, 'Nottingham': NottinghamDF}

Days = 0

playerStruct = namedtuple("playerStruct","location inventory balance health")
p1 = playerStruct(location = "Bristol", inventory= {"Cocaine":0, "Crack":0, "LSD":0, "Ecstasy":0,"Weed": 0, }, balance=0, health = 100)
#how to change players values
#p1.location = "London"

#Current_Price = [1600, 800, 400, 200, 100]
#Quantity = [5, 10, 20, 40, 80]


Birmingham_price = [random.randrange(1200,2000), random.randrange(600,1000), random.randrange(200,500),
                    random.randrange(150,250), random.randrange(75,125)]
Birmingham_quantity = [random.randrange(1,5), random.randrange(1,10), 0, random.randrange(10,40), random.randrange(20,80)]

Bristol_price = [random.randrange(1000,2500), random.randrange(500,1250), random.randrange(250,750),
                    random.randrange(125,325), random.randrange(50,225)]
Bristol_quantity = [random.randrange(1,5), random.randrange(1,10), random.randrange(1,20),
                    random.randrange(10,40), random.randrange(20,80)]

London_price = [random.randrange(1200,2000), random.randrange(600,1000), random.randrange(250,750),
                    random.randrange(150,250), random.randrange(75,125)]
London_quantity = [random.randrange(1,5), random.randrange(1,10), 0,
                    random.randrange(10,40), random.randrange(20,80)]

Nottingham_price = [random.randrange(1200,2000), random.randrange(600,1000), random.randrange(300,500),
                    random.randrange(150,250), random.randrange(75,125)]
Nottingham_quantity = [0, random.randrange(1,10), random.randrange(1,20),
                    random.randrange(10,40), random.randrange(20,80)]
Birmingham_dict = {"Drug":["Cocaine", "Crack", "LSD", "Ecstasy", "Weed"],"Price":Birmingham_price,"Quantity":Birmingham_quantity}

Inventory_dict = {"Drug":["Cocaine", "Crack", "LSD", "Ecstasy", "Weed"],"Quantity":Birmingham_quantity}
BirminghamDF = pd.DataFrame(data=Birmingham_dict, index =["Cocaine", "Crack", "LSD", "Ecstasy", "Weed"])

#BirminghamDF = pd.DataFrame(Birmingham_price, Birmingham_quantity,["Cocaine", "Crack", "LSD", "Ecstasy", "Weed"],columns =['Price','Quantity'])
def random():


    '''if stayhere or palces or sail:

        Days =+ 1


        '''
    pass


#Colours
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
    tv = Treeview(BuyScreen)
    selected = tv.focus()
    temp = tv.item(selected, 'values')

    # if money is more or equal to cost
    Transfer = float(temp[2]) + float(temp[2]) * 0.05
    tv.item(selected, values=(temp[0], temp[1], Transfer))

def Remove():
    pass

def Sell():
    pass


def loading_inventory():
    tv = Treeview(InventoryScreen)
    tv.place(relheight=1, relwidth=1)
    tv['columns'] = list(Inventory_dict.columns)
    tv['show'] = "headings"
    for column in tv['columns']:
        tv.heading(column, text=column)
        tv.column(column, minwidth=0, width=65)
    df_rows = BirminghamDF.to_numpy().tolist()
    for row in df_rows:
        tv.insert("", "end", values=row)
    tv.pack()
    return None

def load_market(df):
    tv = Treeview(BuyScreen)
    tv.place(relheight=1, relwidth=1)  #
    # Used for scrolling
    # treescrolly = tk.Scrollbar(buyscreen, orient= "vertical", command=tv.yveiw)
    # treescrollx = tk.Scrollbar(buyscreen, orient= "horizontal", command=tv.yveix)
    # tv.configure(xscrollcommand=treescrollx.set,yscrollcommand=treescrolly.set)
    # treescrollx.pack(side=bottom,fill="x")
    # treescrolly.pack(side=bottom,fill="y")
    tv['columns'] = list(df.columns)
    tv['show'] = "headings"
    for column in tv['columns']:
        tv.heading(column, text=column)
        tv.column(column, minwidth=0, width=65)
    df_rows = df.to_numpy().tolist()
    for row in df_rows:
        tv.insert("", "end", values=row)
    tv.pack()
    return None

    # placeDf = Dictofplaces[p1.location]
    # frame = Frame(BuyScreen)
    # frame.pack(fill='both', expand=True)

    # pt = Table(frame, dataframe=placeDf )
    # pt.show()


def Sail():
    pass



def StayHere():
    pass


def Places():
    pass



def Options():
    pass


def HighScore():
    pass

def end_game():
    if Days == 30:
        print("HighScore and congrats")

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

#Loading_Screen.pack


#e = Entry(root, width = 50, borderwidth=10)
#e.grid(row= 0, column =2)

#textBox = root.Enter(text="Placeholder text").grid(row= 0, column =0)
#you can have .pack at the end orrrrrrr myButton.pack just underneath






loading_inventory()

load_market(BirminghamDF)

root.mainloop()
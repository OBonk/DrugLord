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

#sound


#player and enemies
Days = 0

playerStruct = namedtuple("playerStruct","location inventory balance health")
p1 = {"balance":1000,"health":100,"fists":2,"Debt":10000,"Katana":0, "Gun":0,"Ammo":0 }
cop = {"balance":10,"health":5,"Gun":1,"Ammo":10,"Baton":1 }

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
Bristol_dict = {"Drug":["Cocaine", "Crack", "LSD", "Ecstasy", "Weed"],"Price":Bristol_price,"Quantity":Bristol_quantity}
London_dict = {"Drug":["Cocaine", "Crack", "LSD", "Ecstasy", "Weed"],"Price":London_price,"Quantity":London_quantity}
Nottingham_dict = {"Drug":["Cocaine", "Crack", "LSD", "Ecstasy", "Weed"],"Price":Nottingham_price,"Quantity":Nottingham_quantity}
Inventory_dict = {"Drug":["Cocaine", "Crack", "LSD", "Ecstasy", "Weed"],"Quantity":[0,0,0,0,0]}


BirminghamDF = pd.DataFrame(data=Birmingham_dict, index =["Cocaine", "Crack", "LSD", "Ecstasy", "Weed"])
BristolDF = pd.DataFrame(data=Bristol_dict, index =["Cocaine", "Crack", "LSD", "Ecstasy", "Weed"])
LondonDF = pd.DataFrame(data=London_dict, index =["Cocaine", "Crack", "LSD", "Ecstasy", "Weed"])
NottinghamDF = pd.DataFrame(data=Nottingham_dict, index =["Cocaine", "Crack", "LSD", "Ecstasy", "Weed"])


#creating random encounter
#Extracted quantities list from inventory Dict and then used in sum
quantities = Inventory_dict["Quantity"]
chance_of_dectection = sum([quantities[0]*5,quantities[1]*3,quantities[2]*2,
                        quantities[3], quantities[4]])
#BirminghamDF = pd.DataFrame(Birmingham_price, Birmingham_quantity,["Cocaine", "Crack", "LSD", "Ecstasy", "Weed"],columns =['Price','Quantity'])

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



def random_encounter():
    # I do not understand weights and why do I need numbers


    numberList = ["nothing_happens","dectected", "freak_happiness"]
    R_E = random.choices(numberList, weights=[100, chance_of_dectection, 10],k=1)
    if R_E == "nothing_happens":
        'nothing happens'
    elif R_E == "detected":
        combat()
    elif R_E == "freak_happiness":
        p1["balance"] += 500


def shop(): #Canvas does not work
    Katana = p1["balance"]-500
    Gun = p1["balance"]-1000
    ammo = p1["balance"]-10
    #Solutions: Create new tk window for shop
    #2: Create a function to hide all widgets on screen
    unpack_list()
    place_map = Canvas(root, width=800, height=600, bg="white")
    # Misc.lift(place_map)
    place_map.place(height=600, width=800)

    Katana_Button = Button(place_map, text="Katana - $500", fg=button2, width=8,
                               bg=button1, command= Katana,borderwidth=10, font=buttonFont)
    Katana_Button.pack()

    gun_Button =Button(place_map, text="Gun - $1000", fg=button2, width=8,
                               bg=button1, command=Gun,borderwidth=10, font=buttonFont)
    gun_Button.pack()
    ammo_Button = Button(place_map, text="ammo$10", fg=button2, width=8,
                        bg=button1, command=ammo,borderwidth=10, font=buttonFont)
    ammo_Button.pack()

    Leave_Button = Button(place_map, text="Leave Shop", fg=button2, width=8,
                          bg=button1, command=lambda: [place_forget(place_map), pack_list()],
                          borderwidth=10, font=buttonFont)
    Leave_Button.pack()
def Buy():
    #this allows you to select the grid
    selected = market_tv.focus()

    temp = market_tv.item(selected, 'values')
    temp2 = inv_tv.item(selected, 'values')
    # if money is more or equal to cost
    if p1["balance"] >= int(temp[1]) and int(temp[2]) > 0:
        Transfer = int(temp[2]) - 1
        p1["balance"] -= int(temp[1])
        Balancetext.set(p1["balance"])
        market_tv.item(selected, values=(temp[0], temp[1], Transfer))
        inv_tv.item(selected, values=(temp2[0], int(temp2[1]) + 1))
    else:
        'note to self add message to action screen'
def Remove():
    pass

def Sell():#######Not working
    ################ Havent figured this out
    selected = inv_tv.focus()

    temp = market_tv.item(selected, 'values')
    temp2 = inv_tv.item(selected, 'values')
    #if the selected from is greater than
    if int(temp2[1])> 0:
        #this removes the drug
        Transfer = int(temp2[1]) - 1
        # this puts money into the balance
        p1["balance"] += int(temp[1])
        Balancetext.set(p1["balance"])
        # now we edit the values in the actual treeviews on the screen
        market_tv.item(selected, values=(temp[0], temp[1],int(temp[2])+1 ))
        inv_tv.item(selected, values=(temp2[0], Transfer))
    else:
        'note to self add message to action screen'


def loading_inventory():
    tv = Treeview(InventoryScreen)
    tv.place(relheight=1, relwidth=1)
    df = pd.DataFrame(data=Inventory_dict)
    tv['columns'] = list(df.columns)
    tv['show'] = "headings"
    for column in tv['columns']:
        tv.heading(column, text=column)
        tv.column(column, minwidth=0, width=100)
    df_rows = df.to_numpy().tolist()
    for row in df_rows:
        tv.insert("", "end", values=row)
    tv.pack()
    return tv

def load_market(df,preloaded=True):
    if preloaded:
        print("this should work")
        market_tv.pack_forget()
    tv = Treeview(BuyScreen)
    tv.place(relheight=1, relwidth=1)  #

    tv['columns'] = list(df.columns)
    tv['show'] = "headings"
    for column in tv['columns']:
        tv.heading(column, text=column)
        tv.column(column, minwidth=0, width=65)
    df_rows = df.to_numpy().tolist()
    for row in df_rows:
        tv.insert("", "end", values=row)
    tv.pack()
    return tv

    # placeDf = Dictofplaces[p1.location]
    # frame = Frame(BuyScreen)
    # frame.pack(fill='both', expand=True)

    # pt = Table(frame, dataframe=placeDf )
    # pt.show()


def Sail():
    pass



def StayHere(load_market,Days):
    load_market()
    Days += 1# why do I have to put Days as any argument
    pass


def Places():### how do I
    unpack_list()
    place_map = Canvas(root, width = 800, height = 600, bg = "white")
    #Misc.lift(place_map)
    place_map.place(height=600,width=800)


    Birmingham_Button = Button(place_map, text="Birmingham", fg=button2, width=8,
                         bg=button1, command=lambda:[place_forget(place_map),pack_list(),load_market(BirminghamDF),random_encounter()],  borderwidth=10, font=buttonFont)
    Birmingham_Button.pack()

    Bristol_Button = Button(place_map, text="Bristol", fg=button2, width=8,
                          bg=button1, command=lambda:[place_forget(place_map),pack_list(),load_market(BristolDF),random_encounter()], borderwidth=10, font=buttonFont)
    Bristol_Button.pack()

    London_Button = Button(place_map, text="London", fg=button2, width=8,
                          bg=button1, command=lambda:[place_forget(place_map),pack_list(),load_market(LondonDF),random_encounter()], borderwidth=10, font=buttonFont)
    London_Button.pack()

    Nottingham_button = Button(place_map, text="Nottingham", fg=button2, width=8,
                           bg=button1, command=lambda:[place_forget(place_map),pack_list(),load_market(NottinghamDF),random_encounter()], borderwidth=10, font=buttonFont)
    Nottingham_button.pack()

    Leave_Button = Button(place_map, text="Leave Shop", fg=button2, width=8,
                          bg=button1, command=lambda: [place_forget(place_map),pack_list()],
                          borderwidth=10, font=buttonFont)
    Leave_Button.pack()


def place_forget(place_map):

    place_map.place_forget()


def Options():
    pass


def HighScore():
    pass

def end_game():
    if Days == 30:
        print("HighScore and congrats")
    elif Days == 7 and p1["Debt"] > 0:
        print("HighScore and congrats")

def Quit():
    root.destroy()

def pack_list():
    List_Of_Grids_pack = [DisplayFrame.grid(row = 1 ,column = 1, columnspan = 3, rowspan = 1,padx = 5, pady = 5),
                          ButtonFrame.grid(row = 2 ,column = 2, columnspan = 1),
                          RHS_Frame.grid(row = 2 ,column = 3, columnspan = 1, rowspan = 1),
                          InventoryFrame.grid(row = 1 ,column = 1, columnspan = 1, rowspan = 1),
                          DataScreenFrame.grid(row = 3 ,column = 1, columnspan = 1, rowspan = 1),
                          LHS_Frame.grid(row = 2 ,column = 1, columnspan = 1, rowspan = 1),
                          BuyScreenFrame.grid(row = 1 ,column = 1, columnspan = 1, rowspan = 1),
                          PersonFrame.grid(row = 2 ,column = 1, columnspan = 1, rowspan = 1)]
    for x in List_Of_Grids_pack:
        return x


def unpack_list(): #why does the unpack list interact ith the root????
    List_Of_Grids_Unpack = [DisplayFrame.grid_forget(), ButtonFrame.grid_forget(), RHS_Frame.grid_forget(),
                            InventoryFrame.grid_forget(), DataScreenFrame.grid_forget(),
                            LHS_Frame.grid_forget(), BuyScreenFrame.grid_forget(), PersonFrame.grid_forget()]
    for x in List_Of_Grids_Unpack:
        return x

def Bank_Borrow():
    if Days > 7:
      print("The Bank cannot lend any more money")
    else:
        if p1["Debt"] == 20000:
            print("You have no more collateral")
        else:
            p1["Debt"] += 2000
            p1["balance"] += 1000


def Bank_RemoveBorrow():
    if Days > 7:
      print("The Bank cannot lend any more money")
    else:
        if p1["Debt"] < 10000:
            print("Nice try")
        else:
            p1["Debt"] -= 2000
            p1["balance"] -= 1000

def Bank_pay_back():

    if p1["Debt"] == 0 or p1["Debt"] < 0:
        print("Your all paid up")

    else:
        p1["Debt"] -= 1000

        p1["balance"] -= 1000


def Bank():

    myButtonBorrow = Button(ButtonFrame, text="Borrow", fg=button2, width=8,
                         bg=button1, command=Bank_Borrow, borderwidth=10, font=buttonFont)
    myButtonBorrow.grid(row=1, column=1, columnspan=1, rowspan=1, padx=2, pady=2)

    myButtonPay = Button(ButtonFrame, text="Payback", fg=button2, width=8,
                          bg=button1, command=Bank_pay_back, borderwidth=10, font=buttonFont)
    myButtonPay.grid(row=1, column=2, columnspan=1, rowspan=1, padx=2, pady=2)

    myButtonRemoveBorrow = Button(ButtonFrame, text="RemoveBorrow", fg=button2, width=8,
                          bg=button1, command=Bank_RemoveBorrow, borderwidth=10, font=buttonFont)
    myButtonRemoveBorrow.grid(row=1, column=3, columnspan=1, rowspan=1, padx=2, pady=2)

    myButtonBank = Button(ButtonFrame, text="Baaaank", fg=button2, width=8,
                          bg=button1, command=UnBank, borderwidth=10, font=buttonFont)
    myButtonBank.grid(row=8, column=2, columnspan=1, rowspan=1, padx=2, pady=2)

def UnBank():
    myButtonBuy = Button(ButtonFrame, text="Buy", fg=button2, width=8,
                         bg=button1, command=Buy, borderwidth=10, font=buttonFont)
    myButtonBuy.grid(row=1, column=1, columnspan=1, rowspan=1, padx=2, pady=2)

    myButtonDrop = Button(ButtonFrame, text="Remove", fg=button2, width=8,
                          bg=button1, command=Remove, borderwidth=10, font=buttonFont)
    myButtonDrop.grid(row=1, column=2, columnspan=1, rowspan=1, padx=2, pady=2)

    myButtonSell = Button(ButtonFrame, text="Sell", fg=button2, width=8,
                          bg=button1, command=Sell, borderwidth=10, font=buttonFont)
    myButtonSell.grid(row=1, column=3, columnspan=1, rowspan=1, padx=2, pady=2)

    myButtonBank = Button(ButtonFrame, text="Baaaank", fg=button2, width=8,
                          bg=button1, command=Bank, borderwidth=10, font=buttonFont)
    myButtonBank.grid(row=8, column=2, columnspan=1, rowspan=1, padx=2, pady=2)




def combat():

    myButtonAttack = Button(ButtonFrame, text="Borrow", fg=button2, width=8,
                         bg=button1, command=Bank_Borrow, borderwidth=10, font=buttonFont)
    myButtonAttack.grid(row=1, column=1, columnspan=1, rowspan=1, padx=2, pady=2)

    myButtonRun = Button(ButtonFrame, text="Payback", fg=button2, width=8,
                          bg=button1, command=lambda:[UnCombat()], borderwidth=10, font=buttonFont)
    myButtonRun.grid(row=1, column=2, columnspan=1, rowspan=1, padx=2, pady=2)

    myButtonBribe = Button(ButtonFrame, text="RemoveBorrow", fg=button2, width=8,
                          bg=button1, command=Bank_RemoveBorrow, borderwidth=10, font=buttonFont)
    myButtonBribe.grid(row=1, column=3, columnspan=1, rowspan=1, padx=2, pady=2)

    # this allows you to select the grid
    selected = market_tv.focus()

    temp = market_tv.item(selected, 'values')
    temp2 = inv_tv.item(selected, 'values')
    # if money is more or equal to cost
    if p1["balance"] >= int(temp[1]) and int(temp[2]) > 0:
        Transfer = int(temp[2]) - 1
        p1["balance"] -= int(temp[1])
        market_tv.item(selected, values=(temp[0], temp[1], Transfer))
        inv_tv.item(selected, values=(temp2[0], int(temp2[1]) + 1))
    else:
        'note to self add message to action screen'


def UnCombat():
    myButtonBuy = Button(ButtonFrame, text="Buy", fg=button2, width=8,
                         bg=button1, command=Buy, borderwidth=10, font=buttonFont)
    myButtonBuy.grid(row=1, column=1, columnspan=1, rowspan=1, padx=2, pady=2)

    myButtonDrop = Button(ButtonFrame, text="Remove", fg=button2, width=8,
                          bg=button1, command=Remove, borderwidth=10, font=buttonFont)
    myButtonDrop.grid(row=1, column=2, columnspan=1, rowspan=1, padx=2, pady=2)

    myButtonSell = Button(ButtonFrame, text="Sell", fg=button2, width=8,
                          bg=button1, command=Sell, borderwidth=10, font=buttonFont)
    myButtonSell.grid(row=1, column=3, columnspan=1, rowspan=1, padx=2, pady=2)

    myButtonBank = Button(ButtonFrame, text="Baaaank", fg=button2, width=8,
                          bg=button1, command=Bank, borderwidth=10, font=buttonFont)
    myButtonBank.grid(row=8, column=2, columnspan=1, rowspan=1, padx=2, pady=2)
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
Person.pack()

Healthtext = StringVar()
Healthtext.set(p1["health"])
Balancetext = StringVar()
Balancetext.set(p1["balance"])

Health = Label(Person,textvariable=Healthtext,font =buttonFont,fg="black")
Health.pack()
Balance = Label(Person,textvariable=Balancetext,font =buttonFont,fg="black")
Balance.pack()
Debt = Label(Person,text = "Debt" + str(p1["Debt"]),font =buttonFont,fg="black")
Debt.pack()


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

myButtonBank = Button(ButtonFrame, text = "Baaaank", fg = button2,width= 8,
                      bg = button1, command = Bank,borderwidth=10, font = buttonFont)
myButtonBank.grid(row = 8 ,column = 2, columnspan = 1, rowspan = 1,padx = 2, pady = 2)


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

myButtonShop = Button(ButtonFrame, text = "shop", fg = button2,width= 8,
                      bg = button1, command = shop,borderwidth=10, font = buttonFont)
myButtonShop.grid(row = 7 ,column = 2, columnspan = 1, rowspan = 1,padx = 2, pady = 2)

myButtonBank = Button(ButtonFrame, text = "Baaaank", fg = button2,width= 8,
                      bg = button1, command = Bank,borderwidth=10, font = buttonFont)
myButtonBank.grid(row = 8 ,column = 2, columnspan = 1, rowspan = 1,padx = 2, pady = 2)

#Loading_Screen.pack


#e = Entry(root, width = 50, borderwidth=10)
#e.grid(row= 0, column =2)

#textBox = root.Enter(text="Placeholder text").grid(row= 0, column =0)
#you can have .pack at the end orrrrrrr myButton.pack just underneath
# Used for scrolling
# treescrolly = tk.Scrollbar(buyscreen, orient= "vertical", command=tv.yveiw)
# treescrollx = tk.Scrollbar(buyscreen, orient= "horizontal", command=tv.yveix)
# tv.configure(xscrollcommand=treescrollx.set,yscrollcommand=treescrolly.set)
# treescrollx.pack(side=bottom,fill="x")
# treescrolly.pack(side=bottom,fill="y")








inv_tv = loading_inventory()

market_tv = load_market(BirminghamDF,False)

root.mainloop()
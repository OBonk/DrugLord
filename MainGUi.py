from tkinter import *
import tkinter.font as font
#import Pillow not working do not know why
from PIL import ImageTk, Image
#import sqlite3

#splash_root = Tk()
#splash_root.geometry("800x600")




root = Tk()
root.title("Get guuuuuddddd")
#cannt get this to work
root.iconbitmap("marioMushroom.png")
#myImage = ImageTK.PhotoImage(Image.open("Whatever Pic I Need"))
#my_label = Label(image =  myImage)
root.geometry("800x600")

#frame = LabelFrame(root, text = "Buy Inventory", padx = 50, pady = 50)
#frame.grid(padx = 10, pady = 10, row =1,column = 1)





#does not work
#window_main = root.Tk(className='Tkinter - TutorialKart', )
#window_main.geometry("600x800")

#creating a label widget
def Buy():

    my_label = Label(root, text = "Hello Yankerrrr MOOOOOOO! XXXX", padx = 50, pady = 50, font = buttonFont)
    my_label.grid(row= 0, column =3)

def Sell():
    pass

def Dump():
    pass

def Places():
    pass

def Options():
    pass

def StayHere():
    pass

def Sail():
    pass

def HighScore():
    pass

'''def Sound(value):
    #not working
    sound = Label(root, text=value)
    sound.grid(row= 4, column =3)'''

def Quit():
    root.destroy()




#Constants hahaa

#inside button, if you have state = DISABLED it stops the button from being clicked
buttonFont = font.Font(family='Helvetica', size=10, weight='bold')

#clicked = StringVar() #Do not know how to change text for dropdown box
#drop = OptionMenu(root,clicked, "New Game", "Save Game","Options","Help")
#drop.grid(row= 1, column =1)

DisplayScreen = Canvas(root, width = 750, height = 125, bg = "white", highlightthickness=4)
DisplayScreen.grid(row = 2 ,column = 1, columnspan = 3, rowspan = 1)

InventoryScreen = Canvas(root, width = 200, height = 200, bg = "white", highlightthickness=4)
InventoryScreen.grid(row = 3 ,column = 3, columnspan = 1, rowspan = 5)

ImportantScreen = Canvas(root, width = 200, height = 200, bg = "white", highlightthickness=4)
ImportantScreen.grid(row = 8 ,column = 3, columnspan = 1, rowspan = 5)

BuyScreen = Canvas(root, width = 200, height = 400, bg = "white", highlightthickness=4)
BuyScreen.grid(row = 3 ,column = 1, columnspan = 1, rowspan = 11)

#frame = LabelFrame(root, text = "Buy Inventory", padx = 50, pady = 50)
#frame.grid(padx = 200, pady = 600, row =0,column = 1)
myButtonBuy = Button(root, text = "Buy",padx = 40, pady = 0.5, fg = "white",bg = "lightblue", command = Buy, borderwidth=10, font = buttonFont)
myButtonBuy.grid(row= 3, column =2)

myButtonSell = Button(root, text = "Sell",padx = 40, pady = 0.5, fg = "white",bg = "lightblue", command = Sell,borderwidth=10, font = buttonFont)
myButtonSell.grid(row= 4, column =2)

myButtonBuy = Button(root, text = "Dump",padx = 40, pady = 0.5, fg = "white",bg = "lightblue", command = Dump, borderwidth=10, font = buttonFont)
myButtonBuy.grid(row= 5, column =2)

myButtonSell = Button(root, text = "Places",padx = 40, pady = 0.5, fg = "white",bg = "lightblue", command = Places,borderwidth=10, font = buttonFont)
myButtonSell.grid(row= 6, column =2)

myButtonBuy = Button(root, text = "Options",padx = 40, pady = 0.5, fg = "white",bg = "lightblue", command = Options, borderwidth=10, font = buttonFont)
myButtonBuy.grid(row= 7, column =2)

myButtonSell = Button(root, text = "Stay Here",padx = 40, pady = 0.5, fg = "white",bg = "lightblue", command = StayHere,borderwidth=10, font = buttonFont)
myButtonSell.grid(row= 8, column =2)

myButtonBuy = Button(root, text = "Sail",padx = 40, pady = 0.5, fg = "white",bg = "lightblue", command = Sail, borderwidth=10, font = buttonFont)
myButtonBuy.grid(row= 9, column =2)


myButtonSell = Button(root, text = "High Score",padx = 40, pady = 0.5, fg = "white",bg = "lightblue", command = HighScore,borderwidth=10, font = buttonFont)
myButtonSell.grid(row= 10, column =2)



r = IntVar()
Checkbutton(root, text = "Sound On/Off", variable = r).grid(row= 11, column =2)
#Radiobutton(root, text = "Sound Off", variable = r, value =1,command=lambda: Sound(r.get)).grid(row= 4, column =1)

myButtonQuit = Button(root, text = "Quit",padx = 40, pady = 0.5, fg = "white",bg = "lightblue", command = Quit,borderwidth=10, font = buttonFont)
myButtonQuit.grid(row= 12, column =2)




#e = Entry(root, width = 50, borderwidth=10)
#e.grid(row= 0, column =2)

#textBox = root.Enter(text="Placeholder text").grid(row= 0, column =0)
#you can have .pack at the end orrrrrrr myButton.pack just underneath








root.mainloop()
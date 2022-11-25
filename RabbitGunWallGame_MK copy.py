# Original Program by Mandar Kelkar
# Copyright
#  ---Rabbit---
#  ---Gun---
#  ---Wall---

# Basically its same game as Rock paper and scissors....
# ---  RULES ---
# When Gun vs Rabbit = Gun wins!
# When Rabbit vs wall = Rabbit wins!
# When Wall vs Gun = Wall wins!

# --- Functions
import random
from tkinter import messagebox
from tkinter import *
operator = ""

'''# Disable all the Buttons after first Match
def button_disable():
    rabbit_btn.config(state="disabled")
    gun_btn.config(state="disabled")
    wall_btn.config(state="disabled")'''

# Define function for Rabbit


def israbbit():
    value = player_one[str(random.randint(0, 2))]
    if value == "rabbit":
        match_result = "Match Draw"
    elif value == "wall":
        match_result = "Wohoo! You Won"
    else:
        match_result = "Computer Win"
    player_one_lbl.config(text=match_result)


# Function for Gun
def isgun():
    value = player_one[str(random.randint(0, 2))]
    if value == "gun":
        match_result = "Match Draw"
    elif value == "wall":
        match_result = "Computer Win"
    else:
        match_result = "Amazing..You won"
    player_one_lbl.config(text=match_result)


# Function for Wall
def iswall():
    value = player_one[str(random.randint(0, 2))]
    if value == "rabbit":
        match_result = "Computer Win"
    elif value == "wall":
        match_result = "Match Draw"
    else:
        match_result = "You Win... :D"
    player_one_lbl.config(text=match_result)


'''def clickbut(Choice):  # lambda:clickbut(1)
    global operator
    operator = operator + str(Choice)
    player_two.set(operator)'''

def info():
    messagebox.showinfo("Info", "Rabbit Gun Wall is similiar to \nrock paper scissors. This game can be played by \ntwo to multile users\nHere you are playing againt the computer\nThe choice is selected randomly.")

def htop():
    messagebox.showinfo("How to play","INSTRUCTIONS TO PLAY GAME :\nPress on images \n1 Rabbit vs Gun = Gun wins!\n2 Gun vs Wall = Wall wins! \n3 Rabbit vs Wall = Rabbit wins!")
    
def cprt():
    messagebox.showinfo("© Copyright", "This application is developed and owned by Mandar Kelkar")
# ------------------------------------------------------------------------------------------------------------------------

root = Tk()
root.title("Rabbit Gun Wall Game")
root.geometry("800x550")
root.minsize(800, 400)
root.config(borderwidth=0, bg="royalblue4")  # bg="DarkSlateGray"
#root.iconphoto()

# Players
player_one = {"0": "rabbit", "1": "gun", "2": "wall"}
player_two = StringVar()

#  Images used in buttons
gun_image = PhotoImage(file="gun.png")
rabbit_image = PhotoImage(file="rabbit.png")
wall_image = PhotoImage(file="brick-wall.png")

# ____________________________________________________________________________________________________________________________________

# Game name Label

rabbit_lbl = Label(text="RABBIT", borderwidth=0, font="Helvetica 17 bold",
                   bg="royalblue4", fg="plum1")  # Rabbit heading label
rabbit_lbl.place(x=250, y=20)
gun_lbl = Label(text="GUN", borderwidth=0, font="Helvetica 17 bold",
                bg="royalblue4", fg="lightsteelblue1")  # Gun heading label
#
gun_lbl.place(x=360, y=20)
wall_lbl = Label(text="WALL", borderwidth=0, font="Helvetica 17 bold",
                 bg="royalblue4", fg="lightpink4")  # Wall heading label
#
wall_lbl.place(x=430, y=20)

# A frame which will contain three buttons
frame1 = Frame(root, bg="white", width=750, height=280)
frame1.place(x=20, y=80)


rabbit_btn = Button(frame1, text="Rabbit", font="Arial 12 bold", image=rabbit_image, compound='top', bg="white",
                    borderwidth=0, height=155, width=155, activebackground="plum1", command=lambda: israbbit())
rabbit_btn.place(x=60, y=60)
gun_btn = Button(frame1, text="Gun", font="Arial 12 bold", image=gun_image, compound='top', bg="white",
                 borderwidth=0, height=155, width=155, activebackground="lightsteelblue1", command=lambda: isgun())
gun_btn.place(x=290, y=60)
wall_btn = Button(frame1, text="Wall", font="Arial 12 bold", image=wall_image, compound='top', bg="white",
                  borderwidth=0, height=155, width=155, activebackground="lightpink4", command=lambda: iswall())
wall_btn.place(x=510, y=60)

player_one_lbl = Label(root, text="Your result",
                       borderwidth=0, bg="royalblue4", font="Arial 15 bold", fg="white")
player_one_lbl.place(x=330, y=450)

# -------------------------------------------------------------------------------------------------------------------------------------------

# Creating a menu for the rules of game :


# create a menubar
menubar = Menu(root, bg="royalblue1")
root.config(menu=menubar)

# create the file_menu
file_menu = Menu(menubar,tearoff=0, bg="royalblue1", font="Arial 10 bold")

# add menu items to the File menu
file_menu.add_command(label='Info',command=lambda:info())
file_menu.add_command(label='How to play',command=lambda:htop())
file_menu.add_command(label='Copyright',command=lambda:cprt())
file_menu.add_separator()

# add Exit menu item
file_menu.add_command(label='Exit',command=root.destroy)

# add the File menu to the menubar
menubar.add_cascade(label="Guide", menu=file_menu, font="Arial 10 bold")


# This is test area

'''test1 = Entry(root, textvariable=player_two, borderwidth=1)
test1.place(x=200, y=450)'''


root.mainloop()

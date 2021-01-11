# A simple dice roller GUI, made with Tkinter.

from random import randint
from tkinter import *

import os, sys

dice_types = [
    "d20",
    "d12",
    "d10",
    "d8",
    "d6",
    "d4",
    "d100"
]


# Roll any number of any type of dice
def roll_dice(num_sides=20, num_rolls=1):
    if num_rolls == 1:
        return randint(1, num_sides)
    elif num_rolls > 1:
        return [randint(1, num_sides) for roll in range(0, num_rolls)]
    else:
        pass


# Return a single roll
def format_roll(roll, mod):
    if mod == 0:
        return f"Roll: {roll}"
    else:
        return f"Roll: {roll} + {mod}\n\nSum: {roll + mod}"


# Return multiple rolls
def format_many_rolls(ind_rolls, sum_rolls, mod):
    return f"Rolls: {ind_rolls} + {mod}\n\nSum: {sum_rolls}"


# Calculate results based on input
def calc_results(num_sides, num_dice, mod):
    if num_dice == 1:
        results["text"] = format_roll(roll_dice(num_sides, num_dice), mod)
    elif num_dice > 1:
        rolls = roll_dice(num_sides, num_dice)
        results["text"] = format_many_rolls(rolls, sum(rolls) + mod, mod)


# Convert user input to an integer and set zero default for blank fields
def handle_input(i):
    if i == "":
        return 0
    else:
        return int(i)


# Button command
def execute():
    try:
        dice_choice = type_display.get()
        num_dice = handle_input(entry_dice_num.get())
        mod = handle_input(entry_dice_mod.get())

        if num_dice <= 0:
            results["text"] = "You must roll at least one dice!"
        else:
            calc_results(int(dice_choice.strip("d")), num_dice, mod)
            
    except ValueError:
        results["text"] = "Invalid input! Only integers allowed!"


# Used to retrieve bundled data files when running as an executable (such as when compiling with PyInstaller)
# SOURCE: https://stackoverflow.com/a/44352931
def resource_path(relative_path):
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)


# Define root and root attributes
root = Tk()
root.geometry("800x600")
root.iconphoto(False, PhotoImage(file="d20.png"))
root.title("Dice Roller")

# Background frames
border = Frame(root, bg="tan")
border.place(relwidth=1, relheight=1)

dice_bg = Frame(border, bg="lightgrey", relief="groove", bd=5)
dice_bg.place(relx=0.5, rely= 0.5, relwidth=0.9, relheight=0.9, anchor="c")

dice_opts = Frame(dice_bg, bg="tan", relief="raised", bd=10)
dice_opts.place(relx=0.55, rely=0.05, relwidth=0.5, relheight=0.5, anchor="ne")

# d20 image
# ---
# This is required for an executable:
# dice_image = PhotoImage(file=resource_path("d20.png"))
# ---
# This is required for running locally:
image = PhotoImage(file="d20.png")

dice_image = Label(dice_bg, image=image, relief="solid", bg="white")
dice_image.place(relx=0.6, rely=0.1, relwidth=0.35, relheight=0.4, anchor="nw")

# Default values
type_display = StringVar()
type_display.set(dice_types[0])

num_display = StringVar()
num_display.set("1")

mod_display = StringVar()
mod_display.set("0")

# Labels
bold_font = ("SysFixed", 12, "bold")

dice_type = Label(dice_opts, bg="tan", text="Dice type: ", font=bold_font, justify="right")
dice_type.place(relx=0.4, rely=0.1, relwidth=0.3, relheight=0.1, anchor="c")

dice_num = Label(dice_opts, bg="tan", text=" Number of dice: ", font=bold_font, justify="right")
dice_num.place(relx=0.33, rely=0.3, relwidth=0.4, relheight=0.1, anchor="c")

dice_mod = Label(dice_opts, bg="tan", text=" Modifier: ", font=bold_font, justify="right")

dice_mod.place(relx=0.41, rely=0.5, relwidth=0.3, relheight=0.1, anchor="c")

# Interactive fields
dice_type = OptionMenu(dice_opts, type_display, *dice_types)
dice_type.config(activebackground="orange", font="SysFixed")
dice_type["menu"].config(activebackground="orange", font="SysFixed")
dice_type.place(relx=0.65, rely=0.1, relwidth=0.25, relheight=0.12, anchor="c")

entry_dice_num = Entry(dice_opts, font="SysFixed", textvariable=num_display, justify="center")
entry_dice_num.place(relx=0.65, rely=0.3, relwidth=0.25, relheight=0.12, anchor="c")

entry_dice_mod = Entry(dice_opts, font="SysFixed", textvariable=mod_display, justify="center")
entry_dice_mod.place(relx=0.65, rely=0.5, relwidth=0.25, relheight=0.12, anchor="c")

# Button for rolling the dice
bttn_roll_dice = Button(dice_opts,
                        text="Roll the dice!",
                        font="Terminal",
                        bg="black",
                        fg="orange",
                        bd=5,
                        relief="ridge",
                        activebackground="orange",
                        activeforeground="black",
                        command=lambda:execute())
                        
bttn_roll_dice.place(relx=0.5, rely=0.7, relwidth=0.75, relheight=0.2, anchor="n")

# Result field
results = Label(dice_bg, font="Terminal", relief="sunken", bd=10, wraplength=600)
results.place(relx=0.5, rely=0.755, relwidth=0.8, relheight=0.25, anchor="c")

# Call main program loop
root.mainloop()

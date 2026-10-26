import pyautogui
import os
import subprocess
from random import randint
import numpy as np
from PIL import ImageColor
import tkinter as tk
from tkinter import ttk
from tkinter import colorchooser
from tkinter import *
from random import uniform
root = Tk()
frame = ttk.Frame(root, padding=10)
frame.grid()
#settings
Turn = "OFF"
width = 300
accuracy = 0.8
height = 200
color = "#000000"
color2 = (0,0,0)
check_ms = 200
root.title("Easy shutdown!")      
root.geometry(f"{width}x{height}")    # starting width and height......,.,
root.resizable(False, False)  
secret = ["Looks like you didn't insert a decimal or it was negitive. Please retry! ","Please enter a decimal. Please retry", "I said... a decimal. just a decimal.", "RETRY.","Can you not read? Just input a value from 0 to 1", "PLEASE. ENTER. A. DECIMAL.", "INSERT A DECIMAL OR I WILL CHOOSE FOR YOU"]
#something else



def random():
    global Turn
    if Turn == "OFF":
        Turn = "ON"
        status.config(text= f"Program has now turned {Turn}.")
        button1.config(text="Running")
    else:
        Turn = "OFF"
        status.config(text= f"Program is now turned {Turn}.")
        button1.config(text= Turn)
    button1.grid(padx= 165)
def get_image():
    current = pyautogui.screenshot()
    pixels = np.array(current.convert('RGB'))
    target = ImageColor.getrgb(color)
    # 2D boolean array: True where the pixel equals the target color
    return (pixels == target).all(axis=2)

status = ttk.Label(frame, text= f"Program is {Turn}")
status.grid(column=0, row=2, sticky= "w")

button1 = ttk.Button(frame, text="Press to start", command=random)
button1.grid(column=0, row=2, sticky = "w", padx= 90)

ttk.Label(frame, text="Hello this is adam's funny shutdown script!", anchor = "w",).grid(column=0, row=0, sticky = "w")
def edit():
    global accuracy
    try:
        accuracy = float(pyautogui.prompt("enter decimal. (0.8 default)"))
        counterin = 0
        while accuracy < 0 or accuracy > 1:
            accuracy = float(pyautogui.prompt(secret[counterin]))
            counterin += 1
            if counterin == 7:
                accuracy = uniform(0.0,1.0)
        accuracy_button.grid(column=0, row=5, sticky = "w", padx= 85 + len(str(accuracy * 100)) * 9)
    except:
        pyautogui.alert("Hey. I don't know what you did- but it caused a error.. Congradulations!")
    

    
    accuracy_label.config(text=f"Accuracy is {accuracy} ({int(accuracy * 100)}%)")
def choose_color():
    global color
    _, selected_color = colorchooser.askcolor(color=color)
    if selected_color is not None:
        color = selected_color
        color_label.config(text=f"Color to look for: {color}")
        accuracy_label.config(bg=color)


color_pick = ttk.Button(frame, text="Change", command=choose_color)
color_label = ttk.Label(frame, text= f"Color to look for: {color}%")
color_label.grid(column=0, row=4, sticky= "w")
color_pick.grid(column=0, row=4, sticky = "w", padx= 180)
color_preview = tk.Label(frame, bg=color, width=2, height=1, relief="solid", borderwidth=1,)
color_preview.place(x = 152, y = 47 )
accuracy_label = ttk.Label(frame, text= f"Accuracy: {accuracy}")
accuracy_label.grid(column=0, row=5, sticky= "w")
accuracy_button = ttk.Button(frame, text="Edit", command= edit)
accuracy_button.grid(column=0, row=5, sticky = "w", padx= 80)
count = 0

def check_loop():
    if Turn == "ON":
        larp = get_image()
        trues = np.count_nonzero(larp)
        if (trues / larp.size) >= accuracy:
            #subprocess.run(["shutdown", "/s", "/t", "0"], check=True)
            print("test death")
            
        
            

    # run again in check_ms ms, inside the tkinter event loop
    root.after(check_ms, check_loop)

check_loop()

root.mainloop()

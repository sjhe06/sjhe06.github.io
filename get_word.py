from tkinter import *

def click():
    print("You clicked the button")

window = Tk()

button = Button(window, text = "click me!", command = click)

button.pack()

window.mainloop()
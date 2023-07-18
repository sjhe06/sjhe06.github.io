from flask import Flask
from tkinter import *


app = Flask(__name__)

@app.route('/')
def click():
    print('You clicked the button')

window = Tk()

button = Button(window, text = "click me!", command = click)

button.pack()

window.mainloop()
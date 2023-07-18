from flask import Flask
from tkinter import *


app = Flask(__name__)

@app.route('/')
def click():
    return '<h2>You clicked the button<h2>'

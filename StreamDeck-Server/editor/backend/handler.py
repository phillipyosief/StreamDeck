from dearpygui.dearpygui import *
from tkinter import Tk, filedialog

import json
import requests
import keyboard
import socket

path = 'resources/buttons.json'  # C:\Program Files (x86)\StreamDeck-Server\buttons.json

localip = [(s.connect(('8.8.8.8', 53)), s.getsockname()[0], s.close()) for s in
           [socket.socket(socket.AF_INET, socket.SOCK_DGRAM)]][0][1] + ':52801'

with open(path, 'r') as b:
    btns = json.load(b)


def handle():
    pass

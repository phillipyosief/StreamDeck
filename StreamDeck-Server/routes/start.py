from flask import Flask, Blueprint, jsonify

import subprocess
import os
import ctypes
import sys

start = Blueprint('start', __name__, url_prefix='/start')


@start.route('/test')
def test():
    return 'working'


@start.route('/wt')
def wt():
    os.system('start wt')
    return 'opened wt'


@start.route('/ds4windows')
def ds4windows():
    os.system('start D:\Desktop\DS4Windows\DS4Windows.exe')
    return 'opened ds4windows'


@start.route('/bluetooth_settings')
def bluetooth_settings():
    os.system('start ms-settings:bluetooth')
    return 'opened bluetooth settings'


@start.route('/coding_folder')
def coding_folder():
    os.system('start D:\Coding')
    return 'opened coding folder'


@start.route('/design_folder')
def design_folder():
    os.system('start D:\Designs')
    return 'opened design folder'


@start.route('/virtualbox')
def virtualbox():
    os.system(r'"C:\Users\yosie\OneDrive\Dokumente\start_vb.bat"')
    return 'opened virtualbox'


@start.route('/signal')
def signal():
    os.system(r'"C:\Users\yosie\AppData\Local\Programs\signal-desktop\Signal.exe"')
    return 'opened signal'


@start.route('/whatsapp')
def whatsapp():
    os.system(r'"C:\Users\yosie\AppData\Local\WhatsApp\WhatsApp.exe"')
    return 'opened whatsapp'


@start.route('/leagueoflegends')
def leagueoflegends():
    os.system(r'"D:\Games\Riot Games\League of Legends\LeagueClient.exe"')
    return 'opened leagueoflegends'


@start.route('/kodi')
def kodi():
    os.system(r'"D:\Programme\Kodi\kodi.exe"')
    return 'opened kodi'


@start.route('/netflix')
def netflix():
    os.system('start https://netflix.com')
    return 'opened netflix'


@start.route('/reddit')
def reddit():
    os.system('start https://reddit.com')
    return 'opened reddit'


@start.route('/3utools')
def _3utools():
    os.system('start D:/Programme/3uTools/3uTools.exe')
    return 'opened 3uTools'


@start.route('/calculator')
def calculator():
    os.system('calc')
    return 'opened calculator'
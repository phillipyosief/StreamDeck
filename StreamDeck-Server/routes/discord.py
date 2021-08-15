from flask import Flask, Blueprint, jsonify

import pyautogui
import pypresence

discord = Blueprint('discord', __name__, url_prefix='/discord')


# Pillow (PIL) is required (pip install pillow)
@discord.route('/mute')
def mute():
    # mute = pyautogui.locateCenterOnScreen('img/discord_mute.png')  # If the file is not a png file it will not work
    # if mute == None:
    #     unmute = pyautogui.locateCenterOnScreen(
    #         'img/discord_unmute.png')  # If the file is not a png file it will not work
    #     print(unmute)
    #     pyautogui.moveTo(unmute)
    #     pyautogui.click()
    # else:
    #     pyautogui.moveTo(mute)
    #     pyautogui.click()

    return '...'


@discord.route('/connect')
def connect():
    c = pypresence.Client(876122754200522782)
    c.start()
    auth = c.authorize(876122754200522782, scopes=['rpc'])  # If you need other scopes, add them
    code_grant = auth.code

    c.set_voice_settings(mute=True)

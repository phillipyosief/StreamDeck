from flask import Flask, Blueprint, jsonify

import pyautogui

discord = Blueprint('discord', __name__, url_prefix='/discord')


@discord.route('/test')
def test():
    return 'working'


@discord.route('/mute_mic')
def mute_mic():
    pyautogui.hotkey('alt', 'm')
    return '...'


@discord.route('/mute_headset')
def mute_headset():
    pyautogui.hotkey('alt', 'j')
    return '...'


@discord.route('/show_overlay_chat')
def show_overlay_chat():
    pyautogui.hotkey('alt', 'e')
    return '...'


@discord.route('/screenshare')
def screenshare():
    pyautogui.hotkey('strg', 'alt', 'l')
    return '...'

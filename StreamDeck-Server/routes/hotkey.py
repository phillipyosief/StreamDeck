import time

from flask import Blueprint, request

import os
import pyautogui

hotkey = Blueprint('hotkey', __name__, url_prefix='/hotkey')


@hotkey.route('/run')
def run():
    keys = request.args.get('keys', None)
    keys = list(keys.split(','))

    for key in keys:
        pyautogui.keyDown(key)

    for key in keys:
        pyautogui.keyUp(key)

    return '...'
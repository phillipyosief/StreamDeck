from flask import Flask, Blueprint, jsonify

photoshop = Blueprint('photoshop', __name__, url_prefix='/photoshop')


@photoshop.route('/test')
def test():
    return 'working'


@photoshop.route('/ebene_rastern')
def ebene_rastern():
    pyautogui.hotkey('strg', 'shift', 'r')
    return '...'


@photoshop.route('/schnell_export')
def schnell_export():
    pyautogui.hotkey('alt', 'umschalt', 'strg', 's')
    return '...'


@photoshop.route('/exportieren_als')
def exportieren_als():
    pyautogui.hotkey('alt', 'shift', 'strg', 'w')
    return '...'


@photoshop.route('/fülloptionen')
def fülloptionen():
    pyautogui.hotkey('alt', 'shift', 'f')
    return '...'


@photoshop.route('/zuschneiden')
def zuschneiden():
    pyautogui.hotkey('alt', 'strg', 'shift', 'z')
    return '...'


@photoshop.route('/standard_arbeitsbereich')
def standard_arbeitsbereich():
    pyautogui.hotkey('shift', 'strg', 'g')
    return '...'
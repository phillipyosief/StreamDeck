from infi.systray import SysTrayIcon

from plyer import notification
from editor import editor
import socket
import platform
import webbrowser
import pyperclip
import requests
import threading
import os

localip = [(s.connect(('8.8.8.8', 53)), s.getsockname()[0], s.close()) for s in
           [socket.socket(socket.AF_INET, socket.SOCK_DGRAM)]][0][1] + ':52800'


def close(systray):
    requests.get('http://' + localip + '/shutdown')


def copy_localip(systray):
    pyperclip.copy(localip)


def github(systray):
    webbrowser.open(url='https://github.com/philliphqs/StreamDeck')


def bugreport(systray):
    body = f'%23%23%23%23%20Description%0A' \
           f'%23%23%23%23%23%23%20Describe%20your%20problem%20here%0A' \
           f'%23%23%23%23%20Environment%0A' \
           f'%20*%20StreamDeck-Server%0A' \
           f'%20*%20Platform:%20{platform.system()}%0A' \
           f'%20*%20Arch:%20{platform.architecture()[0]}%0A' \
           f'%20*%20OS%20Version:%20{platform.version()}%0A' \
           f'%20*%20Python%20Version:%20{platform.python_version()}%0A' \
           f'%20*%20Proccesor:%20{platform.processor()}%0A' \
           f'%20*%20App%20Version:%200.0.2-alpha'
    webbrowser.open(url=f'https://github.com/philliphqs/StreamDeck/issues/new?body={body}')


def edit_layout(systray):
    editor_thread = threading.Thread(target=editor.show)
    editor_thread.start()


def start_tray():
    menu_options = (('GitHub', None, github), ('Report a bug', None, bugreport),
                    ('Layout Editor', None, edit_layout), (localip, None, copy_localip))
    systray = SysTrayIcon('resources/ICON_NOBORDER.ico', f"StreamDeck-Server\n{localip}", menu_options, on_quit=close)
    systray.start()


if __name__ == '__main__':
    start_tray()

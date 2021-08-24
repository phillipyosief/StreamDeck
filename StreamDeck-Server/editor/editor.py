from dearpygui.dearpygui import *

from editor.ui import Window


# from ui import Window

def show():
    # Trying to fix startup issue
    if is_dearpygui_running() is True:
        cleanup_dearpygui()

    Window.show()


if __name__ == '__main__':
    show()

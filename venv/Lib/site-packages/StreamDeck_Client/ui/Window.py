from dearpygui.dearpygui import *

from ui import Buttons
from ui import NavBar


def show():
    with window(label="MainWindow", id=5) as main_window:
        NavBar.show()
        Buttons.show()

    viewport_init()
    start_dearpygui()


def viewport_init():
    vp = create_viewport()
    setup_dearpygui(viewport=vp)
    configure_viewport(0, height=480, width=800, x_pos=600, y_pos=200)

    set_viewport_title("StreamDeck - 0.0.1-alpha - by philliphqs")
    set_viewport_always_top(True)
    set_viewport_resizable(True)
    # set_viewport_small_icon('')
    # set_viewport_large_icon('')
    # set_viewport_height()
    # set_viewport_width()
    set_viewport_decorated(False)

    set_primary_window(5, True)
    show_viewport(vp)
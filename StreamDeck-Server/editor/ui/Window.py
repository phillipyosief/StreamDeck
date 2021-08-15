from dearpygui.dearpygui import *

from editor.ui import Buttons
from editor.ui import Tools
from editor.ui import NavBar

# from ui import Buttons


def show():
    with window(label="MainWindow", id=5) as main_window:
        NavBar.show()
        Tools.show()
        Buttons.show()



    viewport_init()
    # minimize_viewport()
    # maximize_viewport()
    start_dearpygui()


def viewport_init():
    vp = create_viewport()
    setup_dearpygui(viewport=vp)
    configure_viewport(0, height=700, width=1200)

    set_viewport_title("StreamDeck - 0.0.5-alpha - by philliphqs")
    set_viewport_always_top(False)
    set_viewport_resizable(True)
    set_viewport_small_icon('resources/ICON_NOBORDER.ico')
    set_viewport_large_icon('resources/ICON_NOBORDER.ico')
    # set_viewport_height()
    # set_viewport_width()
    set_viewport_decorated(True)

    set_primary_window(5, True)
    show_viewport(vp)

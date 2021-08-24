from dearpygui.dearpygui import *

# from backend import handler
from editor.backend import handler

from editor.ui import ButtonEditor

import json

screen_child = generate_uuid()
navbar_child = generate_uuid()
buttons_child = generate_uuid()
preview_child = generate_uuid()

preview_window = generate_uuid()


def show():
    button_init()


path = 'resources/buttons.json'  # C:\Program Files (x86)\StreamDeck-Server\buttons.json

with open(path, 'r') as b:
    btns = json.load(b)

buttons_height = int(btns['size']['image']['height'])
buttons_width = int(btns['size']['image']['width'])

screen_width = int(btns['size']['screen']['width'])
screen_height = int(btns['size']['screen']['height'])


def create_btns(sender, app_data, user_data, count):
    for key, value in dict.items(btns['buttons']):

        # Register Image and adding image button
        texture_reg_id = generate_uuid()

        width, height, channels, data = load_image(value['image'])
        with texture_registry(id=texture_reg_id):
            image = add_static_texture(width, height, data, parent=texture_reg_id)

        add_image_button(image, id=int(key), width=buttons_width, height=buttons_height,
                         callback=ButtonEditor.show,
                         user_data=int(key))

        # Counting for rows
        if count < int(btns["count"]):
            add_same_line()
            count += 1

        else:
            count = 0


def button_init():
    buttons_child_width = int(btns['size']['screen']['width'])
    navbar_child_width = buttons_child_width - 480
    with window(id=preview_window, label='Current StreamDeck configuration', no_move=True, no_resize=True,
                no_close=True,
                pos=[10, 30]):
        with child(id=preview_child, width=screen_width, height=screen_height):
            with child(id=buttons_child, width=buttons_child_width, no_scrollbar=True, border=False,
                       horizontal_scrollbar=False):
                count = 0

                create_btns(sender=None, app_data=None, user_data=None, count=count)

                add_same_line()

                # Navbar row 1
                with child(border=False, width=buttons_width, height=112):
                    add_button(label='_', callback=minimize_viewport, height=54, width=40)
                    add_button(label='X', callback=stop_dearpygui, height=54, width=40)

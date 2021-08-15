from dearpygui.dearpygui import *

navbar = generate_uuid()

width, height, channels, data = load_image('resources/ICON_NOBORDER.png')
with texture_registry():
    logo = add_static_texture(width, height, data)

logo_id = generate_uuid()


def show():
    def main_menu():
        with menu():
            add_menu_item(label='hello')

    with menu_bar(label='NavBar', id=navbar):
        add_image(id=logo_id, texture_id=logo, width=18, height=18)
        add_separator()

        with menu(label='Tools'):
            add_menu_item(label='Show buttons.json')

from dearpygui.dearpygui import *

from backend.client import *
import json


def show():
    button_init()


with open('StreamDeck/StreamDeck-Client/resources/buttons.json', 'r') as b:
    btns = json.load(b)
    img = btns['image_buttons']
    btn = btns['buttons']


class Images:
    width, height, channels, data = load_image("StreamDeck/StreamDeck-Client/resources/image.png")
    with texture_registry():
        texture_id = add_static_texture(width, height, data)

    width, height, channels, data = load_image(img['1']['image'])
    with texture_registry():
        image_1 = add_static_texture(width, height, data)

    width, height, channels, data = load_image(img['2']['image'])
    with texture_registry():
        image_2 = add_static_texture(width, height, data)

    width, height, channels, data = load_image(img['3']['image'])
    with texture_registry():
        image_3 = add_static_texture(width, height, data)

    width, height, channels, data = load_image(img['4']['image'])
    with texture_registry():
        image_4 = add_static_texture(width, height, data)

    width, height, channels, data = load_image(img['5']['image'])
    with texture_registry():
        image_5 = add_static_texture(width, height, data)

    width, height, channels, data = load_image(img['6']['image'])
    with texture_registry():
        image_6 = add_static_texture(width, height, data)
    #
    width, height, channels, data = load_image(img['7']['image'])
    with texture_registry():
        image_7 = add_static_texture(width, height, data)

    width, height, channels, data = load_image(img['8']['image'])
    with texture_registry():
        image_8 = add_static_texture(width, height, data)

    width, height, channels, data = load_image(img['9']['image'])
    with texture_registry():
        image_9 = add_static_texture(width, height, data)

    width, height, channels, data = load_image(img['10']['image'])
    with texture_registry():
        image_10 = add_static_texture(width, height, data)

    width, height, channels, data = load_image(img['11']['image'])
    with texture_registry():
        image_11 = add_static_texture(width, height, data)

    width, height, channels, data = load_image(img['12']['image'])
    with texture_registry():
        image_12 = add_static_texture(width, height, data)

    width, height, channels, data = load_image(img['13']['image'])
    with texture_registry():
        image_13 = add_static_texture(width, height, data)

    width, height, channels, data = load_image(img['14']['image'])
    with texture_registry():
        image_14 = add_static_texture(width, height, data)

    width, height, channels, data = load_image(img['15']['image'])
    with texture_registry():
        image_15 = add_static_texture(width, height, data)

    width, height, channels, data = load_image(img['16']['image'])
    with texture_registry():
        image_16 = add_static_texture(width, height, data)

    width, height, channels, data = load_image(img['17']['image'])
    with texture_registry():
        image_17 = add_static_texture(width, height, data)

    width, height, channels, data = load_image(img['18']['image'])
    with texture_registry():
        image_18 = add_static_texture(width, height, data)

def one():
    add_image_button(Images.image_1, width=106, height=106, callback=start.wt)
    add_same_line()
    add_spacing()

    add_same_line()

    add_image_button(Images.image_2, width=106, height=106, callback=start.ds4windows)
    add_same_line()
    add_spacing()

    add_same_line()

    add_image_button(Images.image_3, width=106, height=106, callback=start.bluetooth_settings)
    add_same_line()
    add_spacing()

    add_same_line()

    add_image_button(Images.image_4, width=106, height=106, callback=start.coding_folder)
    add_same_line()
    add_spacing()

    add_same_line()

    add_image_button(Images.image_5, width=106, height=106, callback=start.design_folder)
    add_same_line()
    add_spacing()

    add_same_line()

    add_image_button(Images.image_6, width=106, height=106, callback=start.virtualbox)
    add_same_line()
    add_spacing()


def two():
    add_image_button(Images.image_7, width=106, height=106, callback=discord.mute_mic)
    add_same_line()
    add_spacing()

    add_same_line()

    add_image_button(Images.image_8, width=106, height=106, callback=discord.mute_headset)
    add_same_line()
    add_spacing()

    add_same_line()

    add_image_button(Images.image_9, width=106, height=106, callback=discord.overlay)
    add_same_line()
    add_spacing()

    add_same_line()

    add_image_button(Images.image_10, width=106, height=106, callback=discord.screenshare)
    add_same_line()
    add_spacing()

    add_same_line()

    add_image_button(Images.image_11, width=106, height=106, callback=start.signal)
    add_same_line()
    add_spacing()

    add_same_line()

    add_image_button(Images.image_12, width=106, height=106, callback=start.whatsapp)
    add_same_line()
    add_spacing()


def three():
    add_image_button(Images.image_13, width=106, height=106, callback=start.leagueoflegends)
    add_same_line()
    add_spacing()

    add_same_line()

    add_image_button(Images.image_14, width=106, height=106, callback=start.kodi)
    add_same_line()
    add_spacing()

    add_same_line()

    add_image_button(Images.image_15, width=106, height=106, callback=start.netflix)
    add_same_line()
    add_spacing()

    add_same_line()

    add_image_button(Images.image_16, width=106, height=106, callback=start.reddit)
    add_same_line()
    add_spacing()

    add_same_line()

    add_image_button(Images.image_17, width=106, height=106, callback=start._3utools)
    add_same_line()
    add_spacing()

    add_same_line()

    add_image_button(Images.image_18, width=106, height=106, callback=start.calculator)
    add_same_line()
    add_spacing()


def button_init():
    with open('resources/buttons.json', 'r') as bjson:
        one()
        #
        add_spacing()
        #
        two()
        #
        add_spacing()
        #
        three()
        #
        add_spacing()

        add_button(label=btn['1']['title'], width=114, height=45)
        add_same_line()

        add_spacing(count=1)

        add_same_line()
        add_button(label=btn['2']['title'], width=114, height=45)
        add_same_line()

        add_spacing(count=1)

        add_same_line()
        add_button(label=btn['3']['title'], width=114, height=45)
        add_same_line()

        add_spacing(count=1)

        add_same_line()
        add_button(label=btn['4']['title'], width=114, height=45)
        add_same_line()

        add_spacing(count=1)

        add_same_line()
        add_button(label=btn['5']['title'], width=114, height=45)
        add_same_line()

        add_spacing(count=1)

        add_same_line()
        add_button(label=btn['6']['title'], width=114, height=45)
        add_same_line()

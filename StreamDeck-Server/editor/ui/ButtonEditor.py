from dearpygui.dearpygui import *
from tkinter import Tk, filedialog

import requests
import socket
import json

ButtonEditor_id = generate_uuid()

category_combo = generate_uuid()
system_combo = generate_uuid()
obs_combo = generate_uuid()

system_selectapp_button = generate_uuid()
system_websiteurl_input = generate_uuid()
system_hotkey_input = generate_uuid()
system_runcmd_input = generate_uuid()
system_selectfolder_button = generate_uuid()
system_selectfile_button = generate_uuid()
system_selectfolder_text = generate_uuid()
system_selectfile_text = generate_uuid()

obs_switchscene_combo = generate_uuid()
obs_togglemute_combo = generate_uuid()

system = ['Run a app', 'Open website', 'Hotkey', 'Run command', 'Open Folder', 'Open File']
obs = ['Switch scene', 'Toggle mute', 'Stop recording', 'Start recording', 'Pause recording', 'Resume recording',
       'Start streaming', 'Stop streaming']

category = ['System', 'OBS']

localip = [(s.connect(('8.8.8.8', 53)), s.getsockname()[0], s.close()) for s in
           [socket.socket(socket.AF_INET, socket.SOCK_DGRAM)]][0][1] + ':5280'


def show(sender, app_data, user_data):
    key = user_data

    with window(label='Edit Button ' + str(key), id=ButtonEditor_id, width=400, height=250, no_move=True, no_close=False,
                no_scrollbar=False, no_resize=True, modal=True, on_close=close_cb):
        add_combo(
            items=category, label='Category', callback=category_cb, default_value='Choose a category to continue',
            no_arrow_button=False, id=category_combo
        )
        add_separator()


def category_cb():
    if get_value(category_combo) == category[0]:
        # System
        add_combo(
            items=system, label='System action', callback=system_cb, default_value='Choose an action',
            no_arrow_button=False, id=system_combo, parent=ButtonEditor_id
        )
    elif get_value(category_combo) == category[1]:
        # OBS
        add_combo(
            items=obs, label='OBS', callback=obs_cb, default_value='Choose an action', no_arrow_button=False,
            id=obs_combo, parent=ButtonEditor_id
        )


def system_cb():
    if get_value(system_combo) == system[0]:
        # Run a app
        add_button(label='Select app', id=system_selectapp_button, callback=system_selectapp_cb,
                   parent=ButtonEditor_id)
    elif get_value(system_combo) == system[1]:
        # Open website
        add_input_text(id=system_websiteurl_input, label='URL', hint='https://google.com', uppercase=False,
                       no_spaces=True, parent=ButtonEditor_id)
    elif get_value(system_combo) == system[2]:
        # HotKey
        add_input_text(id=system_hotkey_input, label='HotKey', hint='Ctrl, Alt, Del', parent=ButtonEditor_id)
    elif get_value(system_combo) == system[3]:
        # Run command
        add_input_text(id=system_runcmd_input, label='Command', hint='wsl -d Ubuntu-18.04', parent=ButtonEditor_id)
    elif get_value(system_combo) == system[4]:
        # Open folder
        add_button(id=system_selectfolder_button, label='Select folder', callback=system_selectfolder_cb,
                   parent=ButtonEditor_id)
        add_text(default_value="Chosen Directory:", parent=ButtonEditor_id)
        add_same_line(parent=ButtonEditor_id)
        add_text(id=system_selectfolder_text, default_value="None", parent=ButtonEditor_id)
    elif get_value(system_combo) == system[5]:
        # Open File
        add_button(id=system_selectfile_button, label='Select File', callback=system_selectfile_cb,
                   parent=ButtonEditor_id)
        add_text(default_value="Chosen File:", parent=ButtonEditor_id)
        add_same_line(parent=ButtonEditor_id)
        add_text(id=system_selectfile_text, default_value="None", parent=ButtonEditor_id)


def obs_cb():
    print(get_value(obs_combo))
    if get_value(obs_combo) == obs[0]:
        # Switch scene
        scenes_items = []

        get_scenes = requests.get(url=localip + '/obs/get_scenes')

        for key, value in get_scenes.json():
            print(key, value)
            scenes_items.append(value['name'])

        add_combo(
            items=scenes_items, label='Scene', id=obs_switchscene_combo, default_value='Choose scene',
            no_arrow_button=False
        )
    elif get_value(obs_combo) == obs[1]:
        # Toggle mute
        sources_items = []
        add_combo(
            items=sources_items, label='Source', id=obs_togglemute_combo, default_value='Choose source',
            no_arrow_button=False
        )


def system_selectfolder_cb():
    Tk().withdraw()
    file_path = filedialog.askdirectory()
    print(file_path)
    DirString = file_path
    set_value(system_selectfolder_text, DirString)


def system_selectfile_cb():
    Tk().withdraw()
    file_path = filedialog.askopenfilename()
    print(file_path)
    DirString = file_path
    set_value(system_selectfile_text, DirString)


def system_selectapp_cb():
    Tk().withdraw()
    file_path = filedialog.askopenfilename()
    print(file_path)
    DirString = file_path
    set_value(system_selectfile_text, DirString)


def close_cb():

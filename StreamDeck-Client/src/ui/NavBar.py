from dearpygui.dearpygui import *

import json
import requests

exit_id = generate_uuid()
minimize_id = generate_uuid()

CONNECTION_STATE = generate_uuid()
SPACING = generate_uuid()

with open('StreamDeckPi/resources/client.json') as c:
    client = json.load(c)


def check_connection():
    print('check connection')
    try:
        page = requests.get(f'http://{client["ip"]}:{client["port"]}/test')
        test_data = page.json()
        if test_data['test'] == 'success':
            print('connected')
            set_item_label(CONNECTION_STATE, 'Connected       ')
        else:
            print('disconnected')
            set_item_label(CONNECTION_STATE, 'Disconnected    ')
    except:
        print('disconnected')
        set_item_label(CONNECTION_STATE, 'Disconnected    ')


def show():
    with menu_bar():
        add_text(client['ip'] + ':' + client['port'])
        add_separator()
        add_button(label='CONNECTION_STATE', id=CONNECTION_STATE, callback=check_connection)
        check_connection()

        add_spacing(id=SPACING, count=56)

        add_button(label='_', id=minimize_id, callback=minimize_viewport)
        add_button(label='X', id=exit_id, callback=stop_dearpygui)

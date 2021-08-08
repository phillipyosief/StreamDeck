import requests
import json

with open('StreamDeckPi/resources/client.json', 'r') as c:
    client = json.load(c)

    ip = client['ip'] + ':' + client['port']


def interact(path):
    requests.get('http://' + ip + path)


class start:
    @staticmethod
    def wt():
        interact('/start/wt')

    @staticmethod
    def ds4windows():
        interact('/start/ds4windows')

    @staticmethod
    def bluetooth_settings():
        interact('/start/bluetooth_settings')

    @staticmethod
    def coding_folder():
        interact('/start/coding_folder')

    @staticmethod
    def design_folder():
        interact('/start/design_folder')

    @staticmethod
    def virtualbox():
        interact('/start/virtualbox')

    @staticmethod
    def signal():
        interact('/start/signal')

    @staticmethod
    def whatsapp():
        interact('/start/whatsapp')

    @staticmethod
    def leagueoflegends():
        interact('/start/leagueoflegends')

    @staticmethod
    def kodi():
        interact('/start/kodi')

    @staticmethod
    def netflix():
        interact('/start/netflix')

    @staticmethod
    def reddit():
        interact('/start/reddit')

    @staticmethod
    def _3utools():
        interact('/start/3utools')

    @staticmethod
    def calculator():
        interact('/start/calculator')

class discord:
    @staticmethod
    def mute_mic():
        interact('/discord/mute_mic')

    @staticmethod
    def mute_headset():
        interact('/discord/mute_headset')

    @staticmethod
    def overlay():
        interact('/discord/show_overlay_chat')

    @staticmethod
    def screenshare():
        interact('/discord/screenshare')
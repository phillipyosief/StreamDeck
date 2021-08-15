from flask import Flask, jsonify, request

from routes.discord import discord
from routes.command import command
from routes.hotkey import hotkey
from routes.obs import obs

import tray

import socket
import threading

app = Flask(__name__)

localip = [(s.connect(('8.8.8.8', 53)), s.getsockname()[0], s.close()) for s in
           [socket.socket(socket.AF_INET, socket.SOCK_DGRAM)]][0][1]


@app.route('/')
def index():
    return '<h1>StreamDeck</h1> <h3>Congrats, StreamDeck is working</h3>'


@app.route('/shutdown')
def shutdown():
    shutdown_func = request.environ.get('werkzeug.server.shutdown')
    if shutdown_func is None:
        raise RuntimeError('Not running werkzeug')
    shutdown_func()
    return "Shutting down..."


@app.route('/layout_editor')
def test():
    tray.edit_layout(None)
    return '...'


def init_app():
    app.register_blueprint(discord)
    app.register_blueprint(command)
    app.register_blueprint(hotkey)
    print('obs')
    app.register_blueprint(obs)


def main():
    init_app()

    tray_thread = threading.Thread(target=tray.start_tray)
    tray_thread.start()

    app.run(host=localip, port=52801, debug=False)


if __name__ == '__main__':
    main()

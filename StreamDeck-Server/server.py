from flask import Flask, jsonify, Blueprint

from routes.start import start
from routes.discord import discord
from routes.photoshop import photoshop

import socket

app = Flask(__name__)

localip = [(s.connect(('8.8.8.8', 53)), s.getsockname()[0], s.close()) for s in
           [socket.socket(socket.AF_INET, socket.SOCK_DGRAM)]][0][1]


@app.route('/')
def index():
    return '<h1>StreamDeck</h1> <h3>Congrats, StreamDeck is working</h3>'


@app.route('/test')
def test():
    return jsonify({'test': 'success'})


def init_app():
    app.register_blueprint(discord)
    app.register_blueprint(start)
    app.register_blueprint(photoshop)


def main():
    init_app()
    app.run(host=localip, port=52800, debug=False)


if __name__ == '__main__':
    main()

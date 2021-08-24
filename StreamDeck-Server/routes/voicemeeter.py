from flask import Flask, Blueprint, jsonify

from libs.voicemeeter_remote_python import voicemeeter


vm = Blueprint('voicemeeter', __name__, url_prefix='/voicemeeter')



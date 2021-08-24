from flask import Blueprint, request, jsonify

import os
import time
from obswebsocket import obsws, requests
import threading

obs = Blueprint('obs', __name__, url_prefix='/obs')

host = "localhost"
port = 4444

ws = obsws(host, port)

def connect_thread():
    while True:
        try:
            ws.connect()
        except:
            print('error connecting obs')
        time.sleep(10)


obs_connect_thread = threading.Thread(target=connect_thread)
obs_connect_thread.start()

"""
obs-websocket plugin needed 

repo https://github.com/Palakis/obs-websocket/
windows installer https://github.com/Palakis/obs-websocket/releases/download/4.9.1/obs-websocket-4.9.1-Windows-Installer.exe
"""


@obs.route('/switch_scene')
def switch_scene():
    scene = request.args.get('scene', None)

    try:
        scene = scene.replace('%20', ' ')
    except:
        pass
    try:
        scene = scene.replace('%20', ' ')
    except:
        pass
    try:
        scene = scene.replace('%21', '!')
    except:
        pass
    try:
        scene = scene.replace('%22', '"')
    except:
        pass
    try:
        scene = scene.replace('%23', '#')
    except:
        pass
    try:
        scene = scene.replace('%24', '$')
    except:
        pass
    try:
        scene = scene.replace('%25', '%')
    except:
        pass
    try:
        scene = scene.replace('%26', '&')
    except:
        pass
    try:
        scene = scene.replace('%27', "'")
    except:
        pass
    try:
        scene = scene.replace('%28', '(')
    except:
        pass
    try:
        scene = scene.replace('%29', ')')
    except:
        pass
    try:
        scene = scene.replace('%2A', '*')
    except:
        pass
    try:
        scene = scene.replace('%2B', '+')
    except:
        pass
    try:
        scene = scene.replace('%2C', ',')
    except:
        pass
    try:
        scene = scene.replace('%2D', '-')
    except:
        pass
    try:
        scene = scene.replace('%2E', '.')
    except:
        pass
    try:
        scene = scene.replace('%2F', '/')
    except:
        pass
    try:
        scene = scene.replace('%3A', ':')
    except:
        pass
    try:
        scene = scene.replace('%3B', ';')
    except:
        pass
    try:
        scene = scene.replace('%3C', '<')
    except:
        pass
    try:
        scene = scene.replace('%3D', '=')
    except:
        pass
    try:
        scene = scene.replace('%3E', '>')
    except:
        pass
    try:
        scene = scene.replace('%3F', '?')
    except:
        pass
    try:
        scene = scene.replace('%40', '@')
    except:
        pass
    try:
        scene = scene.replace('%5B', '[')
    except:
        pass
    try:
        scene = scene.replace('%5C', '\\')
    except:
        pass
    try:
        scene = scene.replace('%5D', ']')
    except:
        pass
    try:
        scene = scene.replace('%7B', '{')
    except:
        pass
    try:
        scene = scene.replace('%7C', '|')
    except:
        pass
    try:
        scene = scene.replace('%7D', '}')
    except:
        pass

    ws.call(requests.SetCurrentScene(scene))
    return scene


@obs.route('/toggle_mute')
def mute():
    source = request.args.get('source', None)
    ws.call(requests.ToggleMute(source=source))
    return ws.call(requests.GetMute(source=source))


@obs.route('/stop_recording')
def stop_recording():
    ws.call(requests.StopRecording())
    return '...'


@obs.route('/start_recording')
def start_recording():
    ws.call(requests.StartRecording())
    return '...'


@obs.route('/pause_recording')
def pause_recording():
    ws.call(requests.PauseRecording())
    return '...'


@obs.route('/resume_recording')
def resume_recording():
    ws.call(requests.ResumeRecording)
    return '...'


@obs.route('/start_streaming')
def start_streaming():
    ws.call(requests.StartStreaming())
    return '...'


@obs.route('/stop_streaming')
def stop_streaming():
    ws.call(requests.StopStreaming())
    return '...'


# For simpler customization

@obs.route('/get_scenes')
def get_scenes():
    scenes = ws.call(requests.GetSceneList())
    scenes = scenes.getScenes()
    return jsonify(scenes)


@obs.route('/get_sources')
def get_sources():
    sources = ws.call(requests.GetSourcesList())
    sources = sources.getSources()
    return jsonify(sources)

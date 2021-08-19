from flask import Blueprint
from . import socketio
from flask_socketio import emit

bp = Blueprint("multiplayer", __name__)


@socketio.on('gameLoaded')
def sendLevel(signal):
    if signal == 'ok':
        print("sending level to client")
        return levelInformation

@socketio.on('chat')
def chat_broadcast(json, methods=['GET', 'POST']):
    emit('response', json, broadcast=True, include_self=False)

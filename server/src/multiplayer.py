from flask import Blueprint
from . import socketio
from flask_socketio import emit

bp = Blueprint("multiplayer", __name__)




@socketio.on('gameLoaded')
def sendLevel(signal):
    if signal == 'ok':
        print("sending level to client")
        return levelInformation

@socketio.on('connect')
def send_level():
    emit('levelTransfer', levelInformation)

def messageReceived(methods=['GET', 'POST']):
    print('we got a message!')

@socketio.on('event')
def handle_event(json, methods=['GET', 'POST']):
    print('received an event: '+ str(json))
    socketio.emit('response', json, callback=messageReceived)

@socketio.on('chat')
def chat_broadcast(json, methods=['GET', 'POST']):
    emit('response', json, broadcast=True, include_self=False)


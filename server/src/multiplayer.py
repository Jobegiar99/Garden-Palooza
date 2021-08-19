from flask import Blueprint
from . import socketio
from flask_socketio import emit
from .databaseHelper import createLevel
bp = Blueprint("multiplayer", __name__)


levelInformation = createLevel('guest','guestAA')


@socketio.on('connect')
def send_level():
    emit('levelTransfer', levelInformation)

def messageReceived(methods=['GET', 'POST']):
    print('we got a message!')

@socketio.on('event')
def handle_event(json, methods=['GET', 'POST']):
    print('received an event: '+ str(json))
    socketio.emit('response', json, callback=messageReceived)
from flask import Blueprint
from . import socketio
from flask_socketio import emit
from .game.levelGenerator.levelGenerator import GenerateLevel
from src.models import db, GardenModel, UserModel
bp = Blueprint("multiplayer", __name__)

levelInformation = GenerateLevel()

print("Level generated!")

@socketio.on('gameLoaded')
def sendLevel(signal):
    if signal == 'ok':
        print("sending level to client")
        return levelInformation

@socketio.on('chat')
def chat_broadcast(json, methods=['GET', 'POST']):
    emit('response', json, broadcast=True, include_self=False)

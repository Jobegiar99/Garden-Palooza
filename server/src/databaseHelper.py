from src.game.levelGenerator.levelGenerator import GenerateLevel
from src.models import GardenModel, UserModel, TileInfoModel, db
from . import socketio
from flask_socketio import emit
from flask import Blueprint

bp = Blueprint("dbHelper", __name__)

def createLevel(username, gardenName):
    print("creating level")
    level = GenerateLevel()
    print(level)
    firstLayer = level['firstLayer']
    secondLayer = level['secondLayer']
    spawnRow = level['playerRow']
    spawnColumn = level['playerColumn']

    gardenNameCount = db.session.query(GardenModel).filter_by(ownerName = username).count()
    gardenName = gardenName + "" if gardenNameCount == 0 else str(gardenNameCount + 1)

    db.session.add(GardenModel( gardenName, username, spawnRow, spawnColumn ))

    for row in range(len(firstLayer)):
        for column in range(len(firstLayer)):
            db.session.add(TileInfoModel(1, row, column, firstLayer[row][column], gardenName))
            db.session.add(TileInfoModel(2, row, column, secondLayer[row][column], gardenName))

    db.session.commit()

    return level

def loadLevel( username, gardenName):
    print('loadingLevel')
    garden = db.session.query(GardenModel).filter_by(ownerName = username, gardenName = gardenName)[0]

    spawnRow = garden.spawnRow
    spawnColumn = garden.spawnColumn

    firstLayer = []
    secondLayer = []

    for row in range(39):
        firstLayerRow = []
        secondLayerRow = []
        for column in range(51):

            firstLayerInfo = db.session.query(TileInfoModel).filter_by(row = row, column = column, layer = 1, ownerName = username, gardenName = gardenName)[0]
            secondLayerInfo = db.session.query(TileInfoModel).filter_by(row = row, column = column, layer = 2, ownerName = username, gardenName = gardenName)[0]

            firstLayerRow.append(firstLayerInfo.sprite)
            secondLayerRow.append(secondLayerInfo.sprite)
        firstLayer.append(firstLayerRow)
        secondLayerRow.append(secondLayerRow)

        return {"firstLayer":firstLayer, "secondLayer":secondLayer, "playerRow": spawnRow, "playerColumn": playerColumn}

def updateLevel(username, gardenName, row, column, sprite):
    print('updatingLevel')
    tile = db.session.query(TileInfoModel).filter_by(row = row, column = column, layer = 2, ownerName = username, gardenName = gardenName)[0]

    tile.sprite = sprite
    db.session.commit()

def getAllGardenNames(username):
    gardens = db.session.query(GardenModel).filter_by(ownerName = username)
    gardenNames = []
    for garden in garden:
        gardenNames.append(garden.gardenName)
    return {"gardens": gardenNames}


@socketio.on('updateLevel')
def updateLevelSocket(username, gardenName, row, column, sprite):
    updateLevel(username, gardenName, row, column, sprite)

@socketio.on('createLevel')
def createLevelSocket(username, gardenName):
    emit('createLevelSocket', createLevel(username, gardenName))

@socketio.on('loadLevel')
def loadLevelSocket(username, gardenName):
    emit('loadLevelSocket', loadLevel(username, gardenName))

@socketio.on('gardenNames')
def getAllSocketLevels(username):
    emit('getGardenNames', getAllGardenNames(username))



@socketio.on('gameLoaded')
def sendLevel(signal):
    levelInformation = createLevel('guest','guestAA')
    
    if signal == 'ok':
        print("sending level to client")
        return levelInformation
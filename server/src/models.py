from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.dialects import postgresql
from sqlalchemy.orm import relationship

db = SQLAlchemy()

class UserModel(db.Model):
    __tablename__ = "user"

    username = db.Column(db.String(36), primary_key=True)
    password = db.Column(db.String(30))
 
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def __repr__(self):
        return f"<User {self.username}>"


class GardenModel(db.Model):
    __tablename__ = "garden"

    gardenName = db.Column(db.String(30),primary_key = True)
    ownerName = db.Column(db.String(36), db.ForeignKey('user.username'))
    spawnRow = db.Column(db.Integer())
    spawnColumn = db.Column(db.Integer())

    def __init__(self,gardenName,ownerName, spawnRow, spawnColumn):
        self.gardenName = gardenName
        self.ownerName = ownerName

class TileInfoModel(db.Model):
    __tablename__ ='tileInfo'

    layer = db.Column(db.Integer(), primary_key = True)
    row = db.Column(db.Integer(), primary_key = True)
    column = db.Column(db.Integer(), primary_key = True)
    sprite = db.Column(db.Integer())
    gardenName  = db.Column(db.String(30), db.ForeignKey('garden.gardenName'))
    ownerName = db.Column(db.String(36), db.ForeignKey('user.username'))

    def __init__( self, layer, row, column, sprite, gardenName, ownerName ):
        self.layer = layer
        self.row = row
        self.column = column
        self.sprite = sprite
        self.gardenName = gardenName
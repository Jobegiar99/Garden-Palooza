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

    #will improve this if we have enough time
    firstLayer = db.Column(postgresql.ARRAY(db.Integer()))
    secondLayer = db.Column(postgresql.ARRAY(db.Integer()))

    def __init__(gardenName,ownerName,firstLayer,secondLayer):
        self.gardenName = gardenName
        self.ownerName = ownerName
        self.firstLayer = firstLayer
        self.secondLayer = secondLayer

import asyncio
import random
import threading

class Game_Singleton:
    __instance = None

    @staticmethod 
    def getInstance():
        """ Static access method. """
        if Game_Singleton.__instance == None:
            Game_Singleton()
        return Game_Singleton.__instance

    def __init__(self):
        self.addQueue = []
        self.removeQueue = []
        self.updateStatusQueue = []
        self.finishThread = False

        """ Virtually private constructor. """
        if Game_Singleton.__instance != None:
            raise Exception("This class is a singleton!")
        else:
            Game_Singleton.__instance = self
            threading.Thread(target=self.__update).start()

    def __update(self):
        while True:
            if len(self.addQueue) > 0:
                self.addHelper()

            if len(self.removeQueue) > 0:
                self.removeHelper()

            if len(self.updateStatusQueue) > 0:
                self.updateStatusHelper()
            
            if self.finishThread:
                print("BYE :(")
                break

    def addHelper(self):
        raise Exception("Not implemented Yet")

    def removeHelper(self):
        raise Exception("Not implemented Yet")
    
    def updateStatusHelper(self):
        raise Exception("Not implemented Yet")

    @socketio.on('connect')
    def send_level(levelInformation):
        gardenName, row, column, actionType, actionExtras = levelInformation
        if actionType == "addPlant":
            self.addQueue.append((gardenName, row, column,actionExtras))
            emit('addPlant', addHelper())


#JSON structure for the data given by the client:
# id, row, column, actionType, actionExtras
    
game = Game_Singleton()

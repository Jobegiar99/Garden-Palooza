from .orientationDictionary import OrientationDictionary 
from copy import deepcopy 

class RiverDecorator:

    def updateCells(self,matrix, WATER_SPRITE_INDEX, waterSpot, GROUND_SPRITE_INDEX, waterSprites):

        orientationDictionary = OrientationDictionary(waterSprites)
        spriteDict = orientationDictionary.spriteDict
        cornerDict = orientationDictionary.cornerDict
        tempMatrix = deepcopy(matrix)

        for spot in waterSpot:
            row,column = spot
            self.checkNeighbors(row - 1, column, matrix, tempMatrix, GROUND_SPRITE_INDEX, WATER_SPRITE_INDEX, spriteDict, False)
            self.checkNeighbors(row + 1, column, matrix, tempMatrix, GROUND_SPRITE_INDEX, WATER_SPRITE_INDEX, spriteDict, False)
            self.checkNeighbors(row, column - 1, matrix, tempMatrix, GROUND_SPRITE_INDEX, WATER_SPRITE_INDEX, spriteDict, False)
            self.checkNeighbors(row, column + 1, matrix, tempMatrix, GROUND_SPRITE_INDEX, WATER_SPRITE_INDEX, spriteDict, False)

            self.checkNeighbors(row - 1, column - 1, matrix, tempMatrix, GROUND_SPRITE_INDEX, WATER_SPRITE_INDEX, cornerDict, True)
            self.checkNeighbors(row - 1, column + 1, matrix, tempMatrix, GROUND_SPRITE_INDEX, WATER_SPRITE_INDEX, cornerDict, True)
            self.checkNeighbors(row + 1, column - 1, matrix, tempMatrix, GROUND_SPRITE_INDEX, WATER_SPRITE_INDEX, cornerDict, True)
            self.checkNeighbors(row + 1, column + 1, matrix, tempMatrix, GROUND_SPRITE_INDEX, WATER_SPRITE_INDEX, cornerDict, True)

        return tempMatrix


    def checkNeighbors(self, row, column, matrix, tempMatrix, GROUND_SPRITE_INDEX, WATER_SPRITE_INDEX, spriteDict, corner):
            
        if 0 <= row < len(matrix) and 0 <= column < len(matrix[0]) and matrix[row][column] != WATER_SPRITE_INDEX:

            cellInfo = [
                [0,0,0],
                [0,1,0],
                [0,0,0]
            ]

            self.fillCellInfo(cellInfo, row, column, matrix, WATER_SPRITE_INDEX, corner)
            
            for spriteInfo in spriteDict:
                if not corner:
                    if cellInfo in spriteInfo[0]:
                        tempMatrix[row][column] = spriteInfo[1]
                else:
                    if cellInfo in spriteInfo:
                        tempMatrix[row][column] = spriteInfo[1]
                
            
            


    def fillCellInfo(self,cellInfo,row, col, matrix, spriteToCheck, corner):
        if 0 <= row - 1 < len(matrix) and 0 <= col < len(matrix[0]) and matrix[row-1][col] == spriteToCheck:
            cellInfo[0][1] = 1
                
        if 0 <= row + 1 < len(matrix) and 0 <= col < len(matrix[0]) and matrix[row + 1][col] == spriteToCheck:
            cellInfo[2][1] = 1
            
        if 0 <= row < len(matrix) and 0 <= col + 1 < len(matrix[0]) and matrix[row][col + 1] == spriteToCheck:
            cellInfo[1][2] = 1

        if 0 <= row < len(matrix) and 0 <= col - 1 < len(matrix[0]) and matrix[row][col - 1] == spriteToCheck:
            cellInfo[1][0] = 1


        if corner:

            if 0 <= row - 1 < len(matrix) and 0 <= col - 1 < len(matrix[0]) and matrix[row - 1][col - 1] == spriteToCheck:
                cellInfo[0][0] = 1
                
            if 0 <= row - 1 < len(matrix) and 0 <= col + 1 < len(matrix[0]) and matrix[row - 1][col + 1] == spriteToCheck:
                cellInfo[0][2] = 1
            
            if 0 <= row + 1< len(matrix) and 0 <= col + 1 < len(matrix[0]) and matrix[row + 1][col + 1] == spriteToCheck:
                cellInfo[2][2] = 1

            if 0 <= row + 1 < len(matrix) and 0 <= col - 1 < len(matrix[0]) and matrix[row + 1][col - 1] == spriteToCheck:
                cellInfo[2][0] = 1


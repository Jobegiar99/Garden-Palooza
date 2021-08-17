from .orientationDictionary import OrientationDictionary 
from copy import deepcopy 

class GrassDecorator:
    
    def updateCells(self,
                        matrix,
                        spriteIndexes, 
                        createdPath, 
                        groundList, 
                        GRASS_SPRITE_INDEX,
                        GROUND_SPRITE_INDEX):
        orientationDictionary = OrientationDictionary(spriteIndexes)
        spriteDict = orientationDictionary.spriteDict
        cornerDict = orientationDictionary.cornerDict
        tempMatrix = deepcopy(matrix)
        
        for cell in createdPath:
            cellInfo = [
                [0,0,0],
                [0,1,0],
                [0,0,0]
            ]

            self.fillCellInfo(cellInfo,cell,matrix,GROUND_SPRITE_INDEX)
            self.updateSprite(cellInfo,spriteDict,cell[0],cell[1],tempMatrix,GRASS_SPRITE_INDEX)

            self.groundSpriteUpdate(cell,matrix,cornerDict,tempMatrix, cellInfo, GROUND_SPRITE_INDEX)
            self.checkDiagonals(cellInfo, cell, matrix, GROUND_SPRITE_INDEX)
            
            for info in cornerDict:
                if cellInfo in info:
                    tempMatrix[cell[0]][cell[1]] = info[1]

        return tempMatrix

    def fillCellInfo(self,cellInfo,cell,matrix, spriteToCheck):
        row , col = cell
        if 0 <= row - 1 < len(matrix) and 0 <= col < len(matrix[0]) and matrix[row-1][col] == spriteToCheck:
            cellInfo[0][1] = 1
            
        if 0 <= row + 1 < len(matrix) and 0 <= col < len(matrix[0]) and matrix[row + 1][col] == spriteToCheck:
            cellInfo[2][1] = 1
        
        if 0 <= row < len(matrix) and 0 <= col + 1 < len(matrix[0]) and matrix[row][col + 1] == spriteToCheck:
            cellInfo[1][2] = 1

        if 0 <= row < len(matrix) and 0 <= col - 1 < len(matrix[0]) and matrix[row][col - 1] == spriteToCheck:
            cellInfo[1][0] = 1

    def checkDiagonals(self, cellInfo, cell, matrix, spriteToCheck):
        row,col = cell
        if 0 <= row - 1 < len(matrix) and 0 <= col - 1 < len(matrix[0]) and matrix[row - 1][col - 1] == spriteToCheck:
            cellInfo[0][0] = 1
                
        if 0 <= row - 1 < len(matrix) and 0 <= col + 1 < len(matrix[0]) and matrix[row - 1][col + 1] == spriteToCheck:
            cellInfo[0][2] = 1
            
        if 0 <= row + 1< len(matrix) and 0 <= col + 1 < len(matrix[0]) and matrix[row + 1][col + 1] == spriteToCheck:
            cellInfo[2][2] = 1

        if 0 <= row + 1 < len(matrix) and 0 <= col - 1 < len(matrix[0]) and matrix[row + 1][col - 1] == spriteToCheck:
            cellInfo[2][0] = 1
            
    
    def updateSprite(self,cellInfo,spriteDict,row,column,tempMatrix, defaultSprite):
        found = False
        for spriteInfo in spriteDict:
            if cellInfo in spriteInfo[0]:
                
                tempMatrix[row][column] = spriteInfo[1]
                found = True

        if not found:
            tempMatrix[row][column] = defaultSprite

    def groundSpriteUpdate(self,cell,matrix,cornerDict,tempMatrix,cellInfo,GROUND_SPRITE_INDEX):
        row, column = cell
                
        if cellInfo == cornerDict[0][0]:
            if row + 1 < len(matrix) and column + 1 < len(matrix[0]) and matrix[row +1][column - 1] == GROUND_SPRITE_INDEX:
                if matrix[row][column + 1] == GROUND_SPRITE_INDEX and matrix[row + 1][column + 1] == GROUND_SPRITE_INDEX:
                    tempMatrix[row + 1][column + 1] = cornerDict[0][1]
           

        if cellInfo == cornerDict[1][1]:
            if row + 1 < len(matrix) and 0 <= column - 1 and matrix[row +1][column - 1] == GROUND_SPRITE_INDEX:
                if matrix[row][column - 1] == GROUND_SPRITE_INDEX and matrix[row + 1][column - 1] == GROUND_SPRITE_INDEX:
                    tempMatrix[row + 1][column - 1 ] = cornerDict[1][1]
        

        if cellInfo == cornerDict[2][0]:
            if 0 <= row - 1 < len(matrix) and 0 <= column - 1 and matrix[row - 1][column - 1] == GROUND_SPRITE_INDEX:
                if matrix[row][column - 1] == GROUND_SPRITE_INDEX and matrix[row - 1][column - 1] == GROUND_SPRITE_INDEX:
                    tempMatrix[row - 1][column - 1] = cornerDict[2][1]
            

        if cellInfo == cornerDict[3][0]:
            if 0 <= row - 1 < len(matrix) and column + 1 < len(matrix[0]) and matrix[row - 1][column - 1] == GROUND_SPRITE_INDEX:
                if matrix[row - 1][column + 1] == GROUND_SPRITE_INDEX and matrix[ row ][column + 1] == GROUND_SPRITE_INDEX:
                    tempMatrix[row - 1][column + 1] = cornerDict[3][0]      
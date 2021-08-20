import random
from copy import deepcopy
from collections import deque


class SkeletonGenerator:
    def __init__(self, GROUND_SPRITE_INDEX, GRASS_SPRITE_INDEX):
        self.manhattanDistance = lambda pointA, pointB: abs(
            (pointA[0] - pointB[0])
        ) + abs((pointA[1] - pointB[1]))
        self.between = lambda point, matrix: 0 <= point[0] < len(matrix) and 0 <= point[
            1
        ] < len(matrix[0])
        self.matrix = []
        self.createdPath = []
        self.ground = []
        self.SkeletonGenerator(GROUND_SPRITE_INDEX, GRASS_SPRITE_INDEX)
        self.matrix = self.increaseSize(
            self.matrix, len(self.matrix), len(self.matrix[0]), GRASS_SPRITE_INDEX
        )

    def increaseSize(self, matrix, rows, cols, GRASS_SPRITE_INDEX):
        newMatrix = [[0 for x in range(cols * 3)] for y in range(rows * 3)]
        newRow = 0
        newCol = 0
        for row in matrix:
            for col in row:
                (
                    newMatrix[newRow][newCol],
                    newMatrix[newRow][newCol + 1],
                    newMatrix[newRow][newCol + 2],
                ) = (col, col, col)
                (
                    newMatrix[newRow + 1][newCol],
                    newMatrix[newRow + 1][newCol + 1],
                    newMatrix[newRow + 1][newCol + 2],
                ) = (col, col, col)
                (
                    newMatrix[newRow + 2][newCol],
                    newMatrix[newRow + 2][newCol + 1],
                    newMatrix[newRow + 2][newCol + 2],
                ) = (col, col, col)
                if col == GRASS_SPRITE_INDEX:
                    self.createdPath += [
                        [newRow, newCol],
                        [newRow, newCol + 1],
                        [newRow, newCol + 2],
                    ]
                    self.createdPath += [
                        [newRow + 1, newCol],
                        [newRow + 1, newCol + 1],
                        [newRow + 1, newCol + 2],
                    ]
                    self.createdPath += [
                        [newRow + 2, newCol],
                        [newRow + 2, newCol + 1],
                        [newRow + 2, newCol + 2],
                    ]
                else:
                    self.ground += [
                        [newRow, newCol],
                        [newRow, newCol + 1],
                        [newRow, newCol + 2],
                    ]
                    self.ground += [
                        [newRow + 1, newCol],
                        [newRow + 1, newCol + 1],
                        [newRow + 1, newCol + 2],
                    ]
                    self.ground += [
                        [newRow + 2, newCol],
                        [newRow + 2, newCol + 1],
                        [newRow + 2, newCol + 2],
                    ]

                newCol += 3
            newRow += 3
            newCol = 0
        return newMatrix

    def SkeletonGenerator(self, GROUND_SPRITE_INDEX, GRASS_SPRITE_INDEX):
        rows = 13
        cols = 17
        matrix = [[GROUND_SPRITE_INDEX for x in range(cols)] for y in range(rows)]

        start = [rows - 1, random.randint(0, cols - 1)]
        end = [0, random.randint(0, cols - 1)]
        self.GenerateLevel(matrix, deepcopy(start), deepcopy(end), GRASS_SPRITE_INDEX)
        self.matrix = matrix

    def GenerateLevel(self, matrix, wanderer, seeker, GRASS_SPRITE_INDEX):
        createdPath = []

        while seeker not in createdPath:

            matrix[wanderer[0]][wanderer[1]] = GRASS_SPRITE_INDEX
            matrix[seeker[0]][seeker[1]] = GRASS_SPRITE_INDEX

            createdPath.append(wanderer)
            createdPath.append(seeker)

            wanderer = self.getWandererNextMove(matrix, createdPath, wanderer)
            seeker = self.getSeekerNextMove(matrix, createdPath, wanderer, seeker)

    def getMoveDirections(self, point):
        up = [point[0] - 1, point[1]]
        down = [point[0] + 1, point[1]]
        left = [point[0], point[1] - 1]
        right = [point[0], point[1] + 1]
        return [up, down, left, right]

    def getSeekerNextMove(self, matrix, createdPath, wanderer, seeker):

        moves = self.getMoveDirections(seeker)

        originalDistance = self.manhattanDistance(wanderer, seeker)
        upDistance = self.manhattanDistance(wanderer, moves[0])
        downDistance = self.manhattanDistance(wanderer, moves[1])
        leftDistance = self.manhattanDistance(wanderer, moves[2])
        rightDistance = self.manhattanDistance(wanderer, moves[3])

        distances = [
            originalDistance,
            upDistance,
            downDistance,
            leftDistance,
            rightDistance,
        ]

        return self.createSeekerNextMove(distances, moves, matrix, createdPath)

    def createSeekerNextMove(self, distances, moves, matrix, createdPath):
        validMoves = []
        for i in range(4):
            if (
                self.between(moves[i], matrix)
                and moves[i] not in createdPath
                and distances[0] > distances[i + 1]
            ):
                validMoves.append(moves[i])

        if len(validMoves) > 0:
            return validMoves[random.randint(0, len(validMoves) - 1)]

        return [
            random.randint(0, len(matrix) - 1),
            random.randint(0, len(matrix[0]) - 1),
        ]

    def getWandererNextMove(self, matrix, createdPath, wanderer):
        moves = self.getMoveDirections(wanderer)
        validMoves = []
        for move in moves:
            if self.between(move, matrix):
                validMoves.append(move)

        if len(validMoves) > 0:

            return validMoves[random.randint(0, len(validMoves) - 1)]

        return self.checkWandererPossibleMoves(matrix, wanderer, createdPath)

    def checkWandererPossibleMoves(self, matrix, wanderer, createdPath):
        pathExploration = deque()
        walkablePath = []

        while len(pathExploration) > 0:
            point = pathExploration.pop()
            self.checkWandererPathOptions(walkablePath, pathExploration, matrix, point)

        return walkablePath[random.randint(0, len(walkablePath) - 1)]

    def checkWandererPathOptions(self, walkablePath, pathExploration, matrix, point):
        moves = self.getMoveDirections(point)
        for move in moves:
            if self.between(move, matrix) and matrix[move[0]][move[1]] == 0:
                pathExploration.append(move)
                walkablePath.append(move)

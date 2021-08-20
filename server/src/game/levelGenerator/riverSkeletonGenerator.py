from copy import deepcopy
from collections import deque
import random


class RiverSkeletonGenerator:
    def __init__(self, matrix, WATER_SPRITE_INDEX, GROUND_SPRITE_INDEX):
        self.matrix = []
        self.waterSpot = []
        groundSpots = []

        for row in range(len(matrix)):
            for column in range(len(matrix)):
                if (
                    matrix[row][column] == GROUND_SPRITE_INDEX
                    and [row, column] not in groundSpots
                ):
                    currentArea = []
                    queue = deque()
                    queue.append([row, column])
                    self.BFS(deepcopy(matrix), GROUND_SPRITE_INDEX, currentArea, queue)

                    groundPercentage = (len(currentArea) * 100) / (
                        len(matrix) * len(matrix[0])
                    )

                    if 1 <= groundPercentage:
                        groundSpots.append(currentArea)

        if len(groundSpots) > 0:
            self.waterSpot = groundSpots[random.randint(0, len(groundSpots) - 1)]

            self.createRiver(
                matrix, self.waterSpot, WATER_SPRITE_INDEX, GROUND_SPRITE_INDEX
            )

    def BFS(self, matrix, GROUND_SPRITE_INDEX, currentArea, queue):

        while len(queue) > 0:

            row, column = queue.pop()
            currentArea.append([row, column])

            self.BFSHelper(
                matrix, row - 1, column, GROUND_SPRITE_INDEX, currentArea, queue
            )
            self.BFSHelper(
                matrix, row + 1, column, GROUND_SPRITE_INDEX, currentArea, queue
            )
            self.BFSHelper(
                matrix, row, column - 1, GROUND_SPRITE_INDEX, currentArea, queue
            )
            self.BFSHelper(
                matrix, row, column + 1, GROUND_SPRITE_INDEX, currentArea, queue
            )

    def BFSHelper(self, matrix, row, column, GROUND_SPRITE_INDEX, currentArea, queue):
        if (
            0 <= row < len(matrix)
            and 0 <= column < len(matrix[0])
            and matrix[row][column] == GROUND_SPRITE_INDEX
        ):

            matrix[row][column] = -1
            queue.append([row, column])

    def createRiver(self, matrix, waterSpot, WATER_SPRITE_INDEX, GROUND_SPRITE_INDEX):

        for point in waterSpot:
            row, column = point
            if matrix[row][column] == GROUND_SPRITE_INDEX:
                matrix[row][column] = WATER_SPRITE_INDEX

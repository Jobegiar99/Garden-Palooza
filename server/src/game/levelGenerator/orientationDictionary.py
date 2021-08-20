class OrientationDictionary:
    def __init__(self, spriteIndexes):
        up = [[[0, 1, 0], [0, 1, 0], [0, 0, 0]], [[0, 1, 0], [1, 1, 1], [0, 0, 0]]]

        down = [[[0, 0, 0], [0, 1, 0], [0, 1, 0]], [[0, 0, 0], [1, 1, 1], [0, 1, 0]]]

        left = [[[0, 0, 0], [1, 1, 0], [0, 0, 0]], [[0, 1, 0], [1, 1, 0], [0, 1, 0]]]

        right = [[[0, 0, 0], [0, 1, 1], [0, 0, 0]], [[0, 1, 0], [0, 1, 1], [0, 1, 0]]]

        upperCornerLeft = [[[0, 0, 0], [0, 1, 1], [0, 1, 0]]]

        upperCornerRight = [[[0, 0, 0], [1, 1, 0], [0, 1, 0]]]

        lowerCornerRight = [[[0, 1, 0], [1, 1, 0], [0, 0, 0]]]

        lowerCornerLeft = [[[0, 1, 0], [0, 1, 1], [0, 0, 0]]]

        self.spriteDict = [
            [up, spriteIndexes[0]],
            [down, spriteIndexes[1]],
            [left, spriteIndexes[2]],
            [right, spriteIndexes[3]],
            [upperCornerLeft, spriteIndexes[4]],
            [upperCornerRight, spriteIndexes[5]],
            [lowerCornerLeft, spriteIndexes[6]],
            [lowerCornerRight, spriteIndexes[7]],
        ]

        leftUpperCorner = [[0, 0, 0], [0, 1, 0], [0, 0, 1]]

        rightUpperCorner = [[0, 0, 0], [0, 1, 0], [1, 0, 0]]

        rightLowerCorner = [[1, 0, 0], [0, 1, 0], [0, 0, 0]]

        leftLowerCorner = [[0, 0, 1], [0, 1, 0], [0, 0, 0]]

        self.cornerDict = [
            [leftUpperCorner, spriteIndexes[-4]],
            [rightUpperCorner, spriteIndexes[-3]],
            [rightLowerCorner, spriteIndexes[-2]],
            [leftLowerCorner, spriteIndexes[-1]],
        ]

import random


class WaterExtraDecorator:
    def __init__(self, matrix, waterSpot, WATER_EXTRA_SPRITE_MAP):
        for point in waterSpot:
            row, column = point
            if random.uniform(0, 100) < 0.4:
                matrix[row][column] = WATER_EXTRA_SPRITE_MAP[
                    random.randint(0, len(WATER_EXTRA_SPRITE_MAP) - 1)
                ]

import random


class GroundExtraDecorator:
    def __init__(
        self, secondLayer, GROUND_EXTRA_SPRITE_MAP, groundArea, GROUND_SPRITE_MAP
    ):
        for point in groundArea:
            row, column = point
            if secondLayer[row][column] in GROUND_SPRITE_MAP:
                probability = random.uniform(0, 100)
                if probability < 0.2:
                    secondLayer[row][column] = GROUND_EXTRA_SPRITE_MAP[
                        random.randint(0, len(GROUND_EXTRA_SPRITE_MAP) - 1)
                    ]

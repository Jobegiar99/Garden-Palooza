import random


class GrassExtraDecorator:
    def __init__(
        self,
        secondLayer,
        GRASS_EXTRA_SPRITE_MAP,
        GRASS_EXTRA_SPRITE_MAP2,
        createdPath,
        GRASS_SPRITE_INDEX,
    ):
        for point in createdPath:
            row, column = point
            if secondLayer[row][column] == GRASS_SPRITE_INDEX:
                probability = random.uniform(0, 100)
                if probability < 36:
                    secondLayer[row][column] = GRASS_EXTRA_SPRITE_MAP2[
                        random.randint(0, len(GRASS_EXTRA_SPRITE_MAP2) - 1)
                    ]

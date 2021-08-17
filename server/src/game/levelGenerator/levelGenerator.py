from .skeletonGenerator import SkeletonGenerator
from .grassDecorator import GrassDecorator
from .riverSkeletonGenerator import RiverSkeletonGenerator
from .riverDecorator import RiverDecorator
from .groundDecorator import GroundDecorator
from .waterExtraDecorator import WaterExtraDecorator
from .grassExtraDecorator import GrassExtraDecorator
from .groundExtraDecorator import GroundExtraDecorator
from copy import deepcopy
import random

def GenerateLevel():
    GROUND_SPRITE_INDEX = 2363
    GRASS_SPRITE_INDEX = 2420
    WATER_SPRITE_INDEX = 2717


    #up,down,left,right,upperCornerLeft, upperCornerRight, lowerCornerRight, lowerCornerLeft
    #edge cases sprites:  upperCornerLeft, upperCornerRight, lowerCornerRight, lowerCornerLeft
    GRASS_SPRITE_MAP = [2361, 2479, 2419, 2421, 2480, 2478, 2362, 2360, 2422, 2423,2482,2481]

    #up,down,left,right,upperCornerLeft, upperCornerRight, lowerCornerRight, lowerCornerLeft
    #edge cases sprites:  upperCornerLeft, upperCornerRight, lowerCornerRight, lowerCornerLeft
    WATER_SPRITE_MAP = [2715, 2833, 2773, 2775, 2834, 2832, 2716, 2714,2776,2777,2836,2835]

    GROUND_SPRITE_MAP = [GROUND_SPRITE_INDEX,2483,2484,2485]

    WATER_EXTRA_SPRITE_MAP = [ 2896, 2897, 2898, 2899 ]

    GRASS_EXTRA_SPRITE_MAP = [ 2609, 2610, 2611]

    GRASS_EXTRA_SPRITE_MAP2 = [2186,2187, 2306,2307,2308,2309,2310]

    GROUND_EXTRA_SPRITE_MAP = [2491,2550]

    levelSkeleton = SkeletonGenerator(GROUND_SPRITE_INDEX, GRASS_SPRITE_INDEX)
    firstLayer = levelSkeleton.matrix
    firstLayer = GrassDecorator().updateCells(firstLayer,GRASS_SPRITE_MAP,levelSkeleton.createdPath,levelSkeleton.ground, GRASS_SPRITE_INDEX, GROUND_SPRITE_INDEX)
    waterSkeleton = RiverSkeletonGenerator(firstLayer,WATER_SPRITE_INDEX, GROUND_SPRITE_INDEX)

    if len( waterSkeleton.waterSpot ) > 0:
        firstLayer = RiverDecorator().updateCells(firstLayer,WATER_SPRITE_INDEX,waterSkeleton.waterSpot, GROUND_SPRITE_INDEX, WATER_SPRITE_MAP)
        WaterExtraDecorator(firstLayer, waterSkeleton.waterSpot, WATER_EXTRA_SPRITE_MAP)

    GroundDecorator(firstLayer,GROUND_SPRITE_MAP)

    secondLayer = deepcopy(firstLayer)

    GrassExtraDecorator(secondLayer,GRASS_EXTRA_SPRITE_MAP, GRASS_EXTRA_SPRITE_MAP2, levelSkeleton.createdPath, GRASS_SPRITE_INDEX)
    GroundExtraDecorator(secondLayer, GROUND_EXTRA_SPRITE_MAP, levelSkeleton.ground, GROUND_SPRITE_MAP )

    spawnPoint = levelSkeleton.createdPath[random.randint(0,len(levelSkeleton.createdPath) - 1)]

    return {"firstLayer": firstLayer, "secondLayer": secondLayer, "playerRow": spawnPoint[1] * 16, "playerColumn": spawnPoint[0] * 16}

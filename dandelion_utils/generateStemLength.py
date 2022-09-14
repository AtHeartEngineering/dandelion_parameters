# Generates a random int between stemMin and stemMax, with fallbacks:
# returns zero if dandelion isn't enable
# If stemMin is undefined or invalid it is set to 2
# if stemMax is undefined or invalid it is set to the minimum value between stemMin + 3 and 10

import math
from random import random


def generateStemLength(stemMin: int, stemMax: int) -> int:
    # StemMin should be at minimum 1, but recommend setting it to 2
    if (stemMin is None or stemMin < 1):
        stemMin = 2
    if (stemMax is None or stemMax < stemMin):
        stemMax = min(stemMin + 3, 10)

    # Returns a random whole number between stemMin and stemMax
    return math.floor(random() * (stemMax - stemMin + 1) + stemMin)

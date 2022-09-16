# This function is used when receiving a message that has a stem length, and is used to reduce the stem length for the next hop.
# Reduces the stemLength by a random whole number between stemReductionMin and stemReductionMax. The randomness helps obfuscate the sending source and helps propogate the message via floodsub/classic gossipsub to the network sooner.

import math
from random import random, normalvariate


def reviseStemLength_uniform(stemLength: int, stemReductionMin: float, stemReductionMax: float) -> int:
    if (stemLength > 0):
        # # Highly recommend stemReductionMin be 1, but it could be set to 0
        # if (stemReductionMin is None or stemReductionMin < 0):
        #     stemReductionMin = 1

        # # stemReductionMax could be the same value as stemReductionMin if you want a more deterministic, but recommend it be set to stemReductionMin + 1
        # if (stemReductionMax is None or stemReductionMax < stemReductionMin):
        #     stemReductionMax = stemReductionMin + 1

        delta = math.floor((random()) * (stemReductionMax - stemReductionMin + 1) + stemReductionMin)
        newStemLength = stemLength - delta

        if (newStemLength < 0):
            newStemLength = 0
        return newStemLength
    else:
        return 0


def reviseStemLength_normal_dist(stemLength: int, mean: float, std: float) -> int:
    if (stemLength > 0):
        # # Highly recommend stemReductionMin be 1, but it could be set to 0
        # if (stemReductionMin is None or stemReductionMin < 0):
        #     stemReductionMin = 1

        # # stemReductionMax could be the same value as stemReductionMin if you want a more deterministic, but recommend it be set to stemReductionMin + 1
        # if (stemReductionMax is None or stemReductionMax < stemReductionMin):
        #     stemReductionMax = stemReductionMin + 1

        delta = math.floor(normalvariate(mean, std))

        newStemLength = stemLength - delta

        if (newStemLength < 0):
            newStemLength = 0
        return newStemLength
    else:
        return 0

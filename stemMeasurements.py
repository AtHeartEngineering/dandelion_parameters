from dandelion_utils.constants import GossipsubStemMin, GossipsubStemMax, numberOfStemPeers, StemReductionMin, StemReductionMax

from dandelion_utils.generateStemLength import generateStemLength

from dandelion_utils.reviseStemLength import reviseStemLength

import numpy as np
import pandas as pd


def printConstants():
    print("CONSTANTS:")
    print("  - GossipsubStemMin: {}".format(GossipsubStemMin))
    print("  - GossipsubStemMax: {}".format(GossipsubStemMax))
    print("  - numberOfStemPeers: {}".format(numberOfStemPeers))
    print("  - StemReductionMin: {}".format(StemReductionMin))
    print("  - StemReductionMax: {}".format(StemReductionMax))


def main():
    # Generate a random initial stem length
    stemLength = generateStemLength(GossipsubStemMin, GossipsubStemMax)
    print("stemLength: {}".format(stemLength))
    newStemLength = reviseStemLength(stemLength, StemReductionMin, StemReductionMax)
    print("newStemLength: {}".format(newStemLength))


if __name__ == "__main__":
    printConstants()
    main()

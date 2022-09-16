from dandelion_utils.generateStemLength import generateStemLength
from dandelion_utils.reviseStemLength import reviseStemLength_uniform

from dataclasses import dataclass
import numpy as np
import pandas as pd
from scipy.stats import norm
import matplotlib.pyplot as plt
import random


class Params:
    def __init__(self, stemMin: int, stemMax: int, numberOfStemPeers: int, StemReductionMin: float, StemReductionMax: float) -> None:
        self.stemMin = stemMin
        self.stemMax = stemMax
        self.numberOfStemPeers = numberOfStemPeers
        self.StemReductionMin = StemReductionMin
        self.StemReductionMax = StemReductionMax

    def __repr__(self):
        return self.long_description()

    def long_description(self):
        return f'StemMin: {self.stemMin}, StemMax: {self.stemMax}, StemPeers: {self.numberOfStemPeers}, ReductionMin: {self.StemReductionMin}, ReductionMax: {self.StemReductionMax}'

    def short_description(self):
        return f'{self.stemMin}-{self.stemMax}, {self.numberOfStemPeers}p, {self.StemReductionMin}-{self.StemReductionMax}r'

    def data_description(self):
        return {"Min": self.stemMin,
                "Max": self.stemMax,
                "Peers": self.numberOfStemPeers,
                "ReductionMin": self.StemReductionMin,
                "ReductionMax": self.StemReductionMax}


class Sweep:
    def __init__(self, params: Params, num_runs: int, hops: list[int], startingStemLengths: list[int]) -> None:
        self.params = params.data_description(),
        self.num_runs = num_runs
        self.startingStemLengths = startingStemLengths
        self.hops = hops
        self.hops_mean = np.mean(self.hops)
        self.hops_median = np.median(self.hops)
        self.hops_stdd = np.std(self.hops)
        self.hops_min = np.min(self.hops)
        self.hops_max = np.max(self.hops)
        self.starting_stem_mean = np.mean(self.startingStemLengths)
        self.starting_stem_median = np.median(self.startingStemLengths)
        self.starting_stem_stdd = np.std(self.startingStemLengths)
        self.starting_stem_min = np.min(self.startingStemLengths)
        self.starting_stem_max = np.max(self.startingStemLengths)

    def describe_sweep(self):
        print(f"NUMBER RUNS: {self.num_runs}")
        print(f"HOPS:")
        print(f"  - Mean: {self.hops_mean}")
        print(f"  - Median: {self.hops_median}")
        print(f"  - StdD: {self.hops_stdd}")
        print(f"  - Min: {self.hops_min}")
        print(f"  - Max: {self.hops_max}")

    def plot_sweep(self):
        _title = self.params
        plt.hist(self.hops, bins=[1, 2, 3, 4, 5, 6, 7, 8])
        plt.gca().set(title=_title, ylabel='count')

    def export(self):
        e = {"stemMin": self.params[0]["Min"],
             "stemMax": self.params[0]["Max"],
             "numberOfStemPeers": self.params[0]["Peers"],
             "stemReductionMin": self.params[0]["ReductionMin"],
             "stemReductionMax": self.params[0]["ReductionMax"],
             "hops_mean": self.hops_mean,
             "hops_median": self.hops_median,
             "hops_stdd": self.hops_stdd,
             "hops_min": self.hops_min,
             "hops_max": self.hops_max,
             "starting_stem_mean": self.starting_stem_mean,
             "starting_stem_median": self.starting_stem_median,
             "starting_stem_stdd": self.starting_stem_stdd,
             "starting_stem_min": self.starting_stem_min,
             "starting_stem_max": self.starting_stem_max
             }
        return e


def printConstants(params: Params):
    print("USING CONSTANTS:")
    print(f"  - StemMin: {params.stemMin}")
    print(f"  - StemMax: {params.stemMax}")
    print(f"  - numberOfStemPeers: {params.numberOfStemPeers}")
    print(f"  - StemReductionMin: {params.StemReductionMin}")
    print(f"  - StemReductionMax: {params.StemReductionMax}")


def random_stem_hops(params: Params):
    # Generate a random initial stem length
    # stemLength = generateStemLength(params.stemMin, params.stemMax)
    stemLength = params.stemMin
    startingStemLength = stemLength
    hops = 0
    while stemLength > 0:
        hops += 1
        temp_stems = []
        # This simulates the message being passed to multiple "stem peers",
        # of the multiple paths that the message takes, we are always going
        # to chose the shortest path.
        for x in range(params.numberOfStemPeers):
            temp_stems.append(reviseStemLength_uniform(stemLength, params.StemReductionMin, params.StemReductionMax))
        stemLength = min(temp_stems)
    return hops, startingStemLength


def single_sweep(params: Params, num_runs=10000):
    hops = []
    startingStemLengths = []
    while len(hops) < num_runs:
        num_hops, startingStemLength = random_stem_hops(params)
        hops.append(num_hops)
        startingStemLengths.append(startingStemLength)
    return Sweep(params, num_runs, hops, startingStemLengths)


def generate_data():
    width = 3  # variance
    additional_privacy = 1
    stemlength = range(3 * width, (3 + additional_privacy) * width)
    delta_width = range(0, width)  # stemRevision = 0 to delta_width sampled uniformly

    results = []

    _stemMin = random.choice(stemlength)
    _stemReductionMin = random.choice(delta_width)

    params = Params(stemMin=_stemMin, stemMax=_stemMin, numberOfStemPeers=2, StemReductionMin=_stemReductionMin, StemReductionMax=_stemReductionMin)
    print(params)
    x = single_sweep(params).export()
    results.append(x)

    # params = Params(stemMin = 3, stemMax = 7, numberOfStemPeers = 2, StemReductionMin = 1.25, StemReductionMax = 1.33)
    # x = single_sweep(params)
    # print(params)
    # x.describe_sweep()
    # x.plot_sweep()
    df = pd.DataFrame.from_records(results)
    df.to_csv("results.csv")


if __name__ == "__main__":
    generate_data()

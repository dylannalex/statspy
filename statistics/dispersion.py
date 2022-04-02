import statistics.central_tendency as central_tendency
import math


def range_(x: list[float]):
    x_sorted = sorted(x)
    return x_sorted[-1] - x_sorted[0]


def variance(x: list[float]):
    mean = central_tendency.mean(x)
    variance = 0
    for x_i in x:
        variance += math.pow(mean - x_i, 2)
    variance /= len(x) - 1
    return variance


def standard_deviation(x: list[float]):
    return math.sqrt(variance(x))

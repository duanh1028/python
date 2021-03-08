import numpy as np
import matplotlib.pyplot as plt
from helper import *


def norm_histogram(hist):
    """
    takes a histogram of counts and creates a histogram of probabilities

    :param hist: list
    :return: list
    """
    total = sum(hist)
    
    hist_p = [0] * len(hist)
    for i in range(len(hist)):
        hist_p[i] = (float(hist[i])) / total

    return hist_p
    pass

def computeJ(histo, width):
    """
    calculate computeJ for one bin width

    :param histo: list
    :param width: int
    :return: float
    """
    hist_p = norm_histogram(histo)
    p_square_sum = 0
    for i in range(len(hist_p)):
        p_square_sum += hist_p[i] ** 2
    m = sum(histo)

    J = (2 / ((m - 1) * width)) - (((m + 1) * p_square_sum) / ((m - 1) * width))

    return J
    pass


def sweepN (data, minimum, maximum, min_bins, max_bins):
    """
    find the optimal bin
    calculate computeJ for a full sweep [min_bins to max_bins]

    :param data: list
    :param minimum: int
    :param maximum: int
    :param min_bins: int
    :param max_bins: int
    :return: list
    """
    range_size = maximum - minimum
    js = [0] * (max_bins - min_bins + 1)
    i = 0
    for num_bins in range(min_bins, max_bins + 1):
        width = float(range_size / num_bins)
        histogram = plt.hist(data, bins = num_bins, range = (minimum, maximum))
        histo = histogram[0]
        js[i] = computeJ(histo, width)
        i += 1

    return js
    pass

def findMin (l):
    """
    generic function that takes a list of numbers and returns smallest number in that list its index.
    return optimal value and the index of the optimal value as a tuple.

    :param l: list
    :return: tuple
    """
    min_l = min(l)
    min_index = l.index(min_l)
    return (min_l, min_index)
    pass


if __name__ == '__main__':
    data = getData()  # reads data from inp.txt. This is defined in helper.py
    lo = min(data)
    hi = max(data)
    
    js = sweepN(data, lo, hi, 1, 100)

    # the values 1 and 100 represent the lower and higher bound of the range of bins.
    # They will change when we test your code and you should be mindful of that.
    
    print(findMin(js))

    # Include code here to plot js vs. the bin range


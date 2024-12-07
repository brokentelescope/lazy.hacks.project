import pandas as pd

import csv
import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d
from scipy.spatial.distance import euclidean
from scipy.stats import pearsonr
import dtaidistance

def standardize(graph1, graph2):
    data1 = list(csv.reader(open(graph1)))
    new1 = [[], []]
    for x in data1:
        new1[0].append(x[0])
        new1[1].append(x[1])
    increment = float(100/len(new1[0]))
    m = max(new1[1])
    standard1 = []
    for x in range(len(new1[0])):
        a = increment * x
        b = new1[x] / m * 100
        standard1.append([a, b])
    

    data2 = list(csv.reader(open(graph2)))
    new2 = [[], []]
    for x in data2:
        new2[0].append(x[0])
        new2[1].append(x[1])
    increment = float(100/len(new2[0]))
    m = max(new2[1])
    standard2 = []
    for x in range(len(new2[0])):
        a = increment * x
        b = new2[x] / m * 100
        standard2.append([a, b])
        
    return [standard1, standard2]

def calculate_correlation(file1, file2):
    standard1, standard2 = standardize(file1, file2)
    x1, y1 = standard1[:, 0], standard1[:, 1]
    x2, y2 = standard2[:, 0], standard2[:, 1]

    # Step 1: Interpolation to match the number of points in standard1
    # Interpolating standard2's y-values to standard1's x-values
    interp_func = interp1d(x2, y2, kind='linear', fill_value="extrapolate")
    y2_interp = interp_func(x1)
    distance = euclidean(y1, y2_interp)
    distance_dtw = dtaidistance.dtw.distance(y1, y2_interp)
    return distance + distance_dtw

if __name__ == "__main__":
    file1 = 'first_dataset.csv'
    file2 = 'second_dataset.csv'

    correlation_result = calculate_correlation(file1, file2)

    if isinstance(correlation_result, pd.Series):
        print("Correlation between the datasets:\n", correlation_result)
    else:
        print("Error:", correlation_result)

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
    for x in range(1, len(data1)):
        new1[0].append(data1[x][0])
        new1[1].append(int(data1[x][1]))
    increment = float(100/(len(new1[0])-1))
    m = max(new1[1])
    standard1 = []
    for x in range(1, len(new1[0])):
        a = increment * x
        b = new1[1][x] / m * 100
        standard1.append([a, b])
    

    data2 = list(csv.reader(open(graph2)))
    new2 = [[], []]
    for x in range(1, len(data2)):
        new2[0].append(data2[x][0])
        new2[1].append(int(data2[x][1]))
    increment = float(100/(len(new2[0])-1))
    m = max(new2[1])
    standard2 = []
    for x in range(1, len(new2[0])):
        a = increment * x
        b = new2[1][x] / m * 100
        standard2.append([a, b])
    return [standard1, standard2]

def calculate_correlation(file1, file2):
    standard1, standard2 = standardize(file1, file2)
    standard1, standard2 = np.array(standard1), np.array(standard2)
    # Resample to 200 evenly spaced points in the x-range
    x_common = np.linspace(min(standard1[:, 0].min(), standard2[:, 0].min()),
                            max(standard1[:, 0].max(), standard2[:, 0].max()), 200)

    # Interpolate y-values to the common x-axis
    interp1 = interp1d(standard1[:, 0], standard1[:, 1], kind='linear', fill_value="extrapolate")
    interp2 = interp1d(standard2[:, 0], standard2[:, 1], kind='linear', fill_value="extrapolate")

    y1_resampled = interp1(x_common)
    y2_resampled = interp2(x_common)
    distance = euclidean(y1_resampled, y2_resampled)
    distance_dtw = dtaidistance.dtw.distance(y1_resampled, y2_resampled)
    return distance + distance_dtw

if __name__ == "__main__":

    #test files
    file1 = 'first_dataset.csv'
    file2 = 'second_dataset.csv'

    correlation_result = calculate_correlation(file1, file2)
    #less is better 
    print(correlation_result)

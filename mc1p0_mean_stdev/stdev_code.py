import math as m
import pandas as pd
import numpy as np


# calculate the population standard deviation
def stdev_p(data):
    result = (np.array(data)).std()
    return result


# calculate the sample standard deviation
def stdev_s(data):
    result = (pd.Series(data)).std()
    return result


if __name__ == "__main__":
    test = [2.0, 4.0, 4.0, 4.0, 5.0, 5.0, 7.0, 9.0]
    print ("the population stdev is", stdev_p(test))
    print ("the sample stdev is", stdev_s(test))
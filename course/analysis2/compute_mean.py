# compute-mean.py
import numpy as np

import tstools

timeseries = np.genfromtxt("./data/hotwire.csv", delimiter=",")

mean = tstools.get_mean_and_var(timeseries)

print(f"Hei, bestie! Here is the timeseries mean you were looking for: {mean}")
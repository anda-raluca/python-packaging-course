from os.path import basename
from .moments import get_mean_and_var
from .vis import plot_histogram, plot_trajectory_subset

filename = basename(__file__)
print(f"Hello, bestie! {filename} sends their best regards! :D")

get_mean_and_var = get_mean_and_var
# plot_histogram = plot_histogram
# plot_trajectory_subset = plot_trajectory_subset
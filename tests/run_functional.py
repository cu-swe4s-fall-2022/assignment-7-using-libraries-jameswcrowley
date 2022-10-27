import data_processor as dp
import numpy as np


m = 3
n = 2
util_matrix = dp.get_random_matrix(m, n)
print(np.shape(util_matrix)[0])
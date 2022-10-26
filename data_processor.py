# remember to import your libraries!
import numpy as np
import pandas as pd

def get_random_matrix(num_rows, num_columns):
	return np.random.rand(num_rows, num_columns)

def get_file_dimensions(file_name):
	data_frame = pd.read_csv(file_name, sep=',', header=None)
	data_shape = data_frame.shape
	return data_shape

def write_matrix_to_file(num_rows, num_columns, file_name):
	return None

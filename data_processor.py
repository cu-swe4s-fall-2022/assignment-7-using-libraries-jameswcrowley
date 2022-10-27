import numpy as np
import pandas as pd


def get_random_matrix(num_rows, num_columns):
    """
    get_random_matrix:

    returns a random matrix of floats between 0 and 1, of a given size.

    :param num_rows: the number of rows for the returned matrix.
    :param num_columns: the number of columns for the returned matrix.
    :return: a matrix of random floats of specified size.
    """
    return np.random.rand(num_rows, num_columns)


def get_file_dimensions(file_name):
    """
    get_file_dimensions:

    for a csv file of the proper format, return the size of the data.
    Assumes no header.

    :param file_name: the input file.
    :return: the shape of the input file.
    """
    data_frame = pd.read_csv(file_name, sep=',', header=None)
    data_shape = data_frame.shape
    return data_shape


def write_matrix_to_file(num_rows, num_columns, file_name):
    """
    write matrix to file:

    for a specified size, save a matrix of random numbers as a csv.

    :param num_rows: number of rows for random matrix.
    :param num_columns: number of columns for random matrix.
    :param file_name: file path / file name to save the csv as.
    :return: None.
    """
    random_matrix = get_random_matrix(num_rows, num_columns)
    random_dataframe = pd.DataFrame(random_matrix)

    random_dataframe.to_csv(file_name, header=None, index=None)

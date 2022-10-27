import numpy as np
import sys
import argparse
sys.path.append('../')
import data_processor as dp  # nopep8

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--test_type',
                        dest='test_type',
                        type=str,
                        required=True,
                        help='either random_matrix or read_in')
    arg = parser.parse_args()
    test_type = arg.test_type.lower()

    m = 3
    n = 2

    if test_type == 'random_matrix':
        util_matrix = dp.get_random_matrix(m, n)
        print(np.shape(util_matrix)[0])

    elif test_type == 'read_in':
        dp.write_matrix_to_file(m, n, './test_file.csv')

        read_in = dp.get_file_dimensions('test_file.csv')
        print(read_in[0])


if __name__ == '__main__':
    main()


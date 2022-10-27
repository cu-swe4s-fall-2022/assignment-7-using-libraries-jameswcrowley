import unittest
import numpy as np
from numpy import random
import pandas as pd
import sys
import os

sys.path.append('../')
import data_processor as dp  # nopep8


class TestUtils(unittest.TestCase):
    @classmethod
    def setUp(cls):
        m = 3
        n = 2
        random_matrix = random.rand(3, 2)

    @classmethod
    def tearDown(cls):
        random_matrix = None

    def test_random_matrix(self):
        # 1. Adding tests to raise error when n, m not integers
        m = 3.5
        n = 2
        with self.assertRaises(TypeError):
            dp.get_random_matrix(m, n)

        m = 3
        n = 2
        util_matrix = dp.get_random_matrix(m, n)

        # 2. Testing the shape of the returned matrix
        self.assertEqual(np.shape(util_matrix)[0], m)
        self.assertEqual(np.shape(util_matrix)[1], n)

        # 3. Testing if the matrix is random:
        util_matrix = dp.get_random_matrix(m, n)

        element_0_0 = util_matrix[0, 0]
        element_0_0_list = []
        for i in range(100):
            temp_element_0_0 = dp.get_random_matrix(m, n)[0][0]
            element_0_0_list.append(temp_element_0_0)

        self.assertNotEqual(np.mean(element_0_0_list), element_0_0)

    def test_get_file_dimensions(self):
        test_csv = '../iris.data'
        size = [150, 5]
        function_size = dp.get_file_dimensions(test_csv)

        # 1. Testing that the function returns the right size for a test file:
        self.assertEqual(size[0], function_size[0])
        self.assertEqual(size[1], function_size[1])

        # 2. Testing that it raises an error if passed in the wrong file.
        with self.assertRaises(FileNotFoundError):
            dp.get_file_dimensions('this_file_doesnt_exist.data')

    def test_write_matrix_to_file(self):
        file_name = 'test_write_file.txt'

        # check that we successfully deleted files before testing rest
        with self.assertRaises(FileNotFoundError):
            os.listdir('test_write_file.txt')

        n = 2
        m = 3

        dp.write_matrix_to_file(n, m, file_name)
        self.assertIn(file_name, os.listdir())

        # Test 2: check the shape of the saved datafile.

        test_data_frame = pd.read_csv(file_name,
                                      delimiter=',',
                                      header=None)

        self.assertEqual(test_data_frame.shape[0], n)
        self.assertEqual(test_data_frame.shape[1], m)

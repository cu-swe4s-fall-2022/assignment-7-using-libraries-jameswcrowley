import unittest
import numpy as np
from numpy import random
import sys
sys.path.append('../')
import data_processor as dp # nopep8


class TestUtils(unittest.TestCase):
    @classmethod
    def setUp(self):
        m = 3; n = 2
        random_matrix = random.rand(3, 2)

    @classmethod
    def tearDown(self):
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

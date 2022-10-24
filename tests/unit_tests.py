import unittest
import data_processor as dp
import numpy
from numpy import random

class TestUtils(unittest.TestCase):
    @classmethod
    def setUp(self):
        m = 3; n = 2
        random_matrix = random.rand(3, 2)

    @classmethod
    def tearDown(self):
        random_matrix = None


    def test_random_matrix(self):
        m = 3; n = 2
        util_matrix = dp.get_random_matrix(m, n)

        # 1. Testing the shape of the returned matrix
        self.assertEqual(np.shape(util_matrix)[0], m)
        self.assertEqual(np.shape(util_matrix)[1], n)
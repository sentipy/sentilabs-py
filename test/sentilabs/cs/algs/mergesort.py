import unittest
import random
from sentilabs.cs.algs.sorts import *


class MergeSortTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        r = 1000000
        cls.test6_arr = list()
        for i in range(r):
            cls.test6_arr.append(random.randint(0, 50000))
        random.shuffle(cls.test6_arr)

    def test_1(self):
        arr = list(range(5))
        random.shuffle(arr)
        mergeSort(arr)
        self.assertEqual(arr, list(range(5)))

    def test_2(self):
        arr = list(range(100))
        random.shuffle(arr)
        mergeSort(arr)
        self.assertEqual(arr, list(range(100)))

    def test_3(self):
        arr = list(range(100)) + list(range(100))
        random.shuffle(arr)
        mergeSort(arr)
        self.assertEqual(arr, [x//2 for x in list(range(200))])

    def test_4(self):
        r = random.randint(1000, 10000)
        arr = list()
        for i in range(r):
            arr.append(random.randint(0, 100000))
        random.shuffle(arr)
        mergeSort(arr)
        self.assertEqual(arr, sorted(arr))

    def test_5(self):
        r = random.randint(100000, 1000000)
        arr = list()
        for i in range(r):
            arr.append(random.randint(0, 50000))
        random.shuffle(arr)
        mergeSort(arr)
        self.assertEqual(arr, sorted(arr))

    def test_6(self):
        mergeSort(self.test6_arr)
        self.assertEqual(self.test6_arr, sorted(self.test6_arr))

if __name__ == '__main__':
    unittest.main()
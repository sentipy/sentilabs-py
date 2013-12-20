import unittest
import random
from sentilabs.cs.algs.sorts import *


class MyTestCase(unittest.TestCase):
    def test_1(self):
        arr = list(range(5))
        random.shuffle(arr)
        quick_sort_3way(arr, 0, 4)
        self.assertEqual(arr, list(range(5)))

    def test_2(self):
        arr = list(range(100))
        random.shuffle(arr)
        quick_sort_3way(arr, 0, 99)
        self.assertEqual(arr, list(range(100)))

    def test_3(self):
        arr = list(range(100)) + list(range(100))
        random.shuffle(arr)
        quick_sort_3way(arr, 0, 199)
        self.assertEqual(arr, [x//2 for x in list(range(200))])

    def test_4(self):
        r = random.randint(1000, 10000)
        arr = list()
        for i in range(r):
            arr.append(random.randint(0, 100000))
        random.shuffle(arr)
        quick_sort_3way(arr, 0, r - 1)
        self.assertEqual(arr, sorted(arr))

    def test_5(self):
        r = random.randint(100000, 1000000)
        arr = list()
        for i in range(r):
            arr.append(random.randint(0, 50000))
        random.shuffle(arr)
        quick_sort_3way(arr, 0, r - 1)
        self.assertEqual(arr, sorted(arr))

if __name__ == '__main__':
    unittest.main()

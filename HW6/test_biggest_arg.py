import unittest

from HW6.task_3_1 import biggest_arg


class TestBiggestArgFunc(unittest.TestCase):

    def test_empty_arguments(self):
        result = biggest_arg()
        self.assertEqual(result, float('-inf'))

    def test_single_argument(self):
        result = biggest_arg(5)
        self.assertEqual(result, 5)

    def test_multiple_arguments(self):
        result = biggest_arg(3, 7, 1, 9, 4)
        self.assertEqual(result, 9)

    def test_negative_arguments(self):
        result = biggest_arg(-2, -5, -1)
        self.assertEqual(result, -1)

    def test_mixed_arguments(self):
        result = biggest_arg(0, 2, -3, 5)
        self.assertEqual(result, 5)


if __name__ == '__main__':
    unittest.main()

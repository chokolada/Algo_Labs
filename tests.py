import unittest
from main import zig_zag


class TestZigzagTraversal(unittest.TestCase):
    def test_case_1(self):
        matrix = [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]
        ]
        self.assertEqual(zig_zag(matrix), [1, 2, 4, 7, 5, 3, 6, 8, 9])

    def test_case_2(self):
        matrix = [
            [1, 2, 3, 4],
            [5, 6, 7, 8]
        ]
        self.assertEqual(zig_zag(matrix), [1, 2, 5, 6, 3, 4, 7, 8])

    def test_case_3(self):
        matrix = [[1]]
        self.assertEqual(zig_zag(matrix), [1])

    def test_case_4(self):
        matrix = [[1, 2, 3, 4, 5, 6]]
        self.assertEqual(zig_zag(matrix), [1, 2, 3, 4, 5, 6])

    def test_case_5(self):
        matrix = [[1, 2, 3, 4, 5, 6, 7]]
        self.assertEqual(zig_zag(matrix), [1, 2, 3, 4, 5, 6, 7])


if __name__ == '__main__':
    unittest.main()

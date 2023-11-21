import unittest
from Lab_5.Lab_5 import server_finder

class TestServerFinder(unittest.TestCase):

    def test_server_finder(self):
        # Assuming 'gamsrv.in' is in the parent directory
        result = server_finder("../gamsrv.in")
        self.assertEqual(result, 200)

if __name__ == '__main__':
    unittest.main()

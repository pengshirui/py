import unittest

from Solution import Solution

class SolutionTests(unittest.TestCase):

    def test_stringToDict_1(self):
        r = Solution.stringToDict('hello')
        self.assertEqual(r[0], 'h')
        self.assertEqual(r[1], 'e')
        self.assertEqual(r[2], 'l')
        self.assertEqual(r[3], 'l')
        self.assertEqual(r[4], 'o')


if __name__ == '__main__':
    unittest.main()
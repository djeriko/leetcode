import unittest 
from solution import Solution

class SolutionTest(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()
        

    def test_1(self):
        '''
        Should return 2 if input array is [3, 0, 1].
        '''
        data = [3, 0, 1]
        result = self.solution.missingNumber(data)
        self.assertEqual(result, 2)

    def test_2(self):
        '''
        Should return 8 if input array is [9, 6, 4, 2, 3, 5, 7, 0, 1].
        '''
        data = [9, 6, 4, 2, 3, 5, 7, 0, 1]
        result = self.solution.missingNumber(data)
        self.assertEqual(result, 8)
 
    def test_3(self):
        '''
        Should return 2 if input array is [0, 1].
        '''
        data = [0, 1]
        result = self.solution.missingNumber(data)
        self.assertEqual(result, 2)

        
if __name__ == "__main__":
    unittest.main()

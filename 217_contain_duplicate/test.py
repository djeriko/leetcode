import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()
        
    def test_1(self):
        '''
        Should return true when array values appears twice.
        '''
        data = [1, 2, 3, 1]
        result = self.solution.containsDuplicate(data)
        self.assertEqual(result, True) 

    def test_2(self):
        '''
        Should return False when array values are unique.
        '''
        data = [1, 2, 3, 4, 8, 7]
        result = self.solution.containsDuplicate(data)
        self.assertEqual(result, False) 
 

if __name__ == "__main__":
    unittest.main()
    

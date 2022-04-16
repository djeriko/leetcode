class Solution:
    def fib(self, n: int) -> int:
        """
        Time = O(n)
        Space = O(1)
        """
        if n == 0:
            return 0

        n0 = 0
        n1 = 1

        for i in range(1, n):
            n0, n1 = n1, n1 + n0
        
        return n1

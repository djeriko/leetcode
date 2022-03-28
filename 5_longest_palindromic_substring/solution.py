class Solution:
    def longestPalindrome(self, s: str) -> str:
        pass
    
    def isPalindrome(self, s: str) -> bool:
        if len(s) == 0: 
            return false

        reverse_s = s[::-1]
        
        start = 0
        end = len(s) - 1
        
        
        while(end > start):
            if s[start] != s[end]: 
                return False
            start += 1
            end -= 1

        return True

                

         
  


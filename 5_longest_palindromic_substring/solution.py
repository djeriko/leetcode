class Solution:
    def longestPalindromeBrute(self, s: str) -> str:
        """Complexity is O^3."""
        best_len = 0
        best_s = ""

        for i in range(len(s)):
            for j in range(i, len(s), 1): 
                l = j + 1
                sub_s = s[i:l]
                if l - i > best_len and self.isPalindrome(sub_s):
                    best_len = l
                    best_s = sub_s
              
        return best_s

    def longestPalindromeBrute2(self, s: str) -> str:
        """Complexity is O^3."""
        for length in range(len(s), 0, -1):
            for start_index in range(0, len(s)+1-length):
                if self.isPalindrome(s[start_index:(start_index+length)]):
                    return s[start_index:(start_index+length)]

    def longestPalindrome(self, s: str):
        """Complexity is O^2."""
        biggest = s[0]
        step = 0
        
        # Handle single letter center. Odd case.
        for center in range(1, len(s)-1):
            bounds = [center-(1+step), center+(1+step)]
            while (bounds[0] > -1) and (bounds[1] < len(s)):
                if self.isPalindrome(s[bounds[0]:bounds[1]+1]):
                    biggest = s[bounds[0]:bounds[1]+1]
                    step = len(biggest)//2
                    bounds[0] -= 1
                    bounds[1] += 1
                else:
                    break
        # Handle double letter center. Even case.
        for center in range(step, len(s)-step-1):
            bounds = [center-(step), center+(1+step)]
            while (bounds[0] > -1) and (bounds[1] < len(s)):
                if self.isPalindrome(s[bounds[0]:bounds[1]+1]):
                    biggest = s[bounds[0]:bounds[1]+1]
                    step = len(biggest)//2
                    bounds[0] -= 1
                    bounds[1] += 1
                else:
                    break

        return biggest    
            

                

    def longestPalindrome1(self, s:str) -> str:
        """Complexity is O^2."""
        best_len = 0
        best_s = ""
        for mid in range(len(s)):
            x = 0
            while mid - x >= 0 and mid + x < len(s):
                if s[mid-x] != s[mid+x]:
                    break
                l = 2 * x + 1
                if l > best_len:
                    best_len = l
                    best_s = s[mid-x:mid+x+1]
                x += 1

        for mid in range(len(s) - 1):
            x = 0
            while mid - x >= 0 and mid + x < (len(s) - 1):
                if s[mid-x] != s[mid+x+1]:
                    break
                l = 2 * (1 + x)
                if l > best_len:
                    best_len = l
                    best_s = s[mid-x:mid+x+2]
                x += 1

        return best_s
        


    
    def isPalindrome(self, s: str) -> bool:
        rev = s[::-1]
        return rev == s

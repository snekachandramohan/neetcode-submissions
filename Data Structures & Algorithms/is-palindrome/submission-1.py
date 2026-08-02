import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        s = re.sub(r'[^A-Za-z0-9]','',s)
        i, j = 0, len(s)-1
        while i<j:
            if s[i]!=s[j]: 
                return False
            else:
                i, j = i+1, j-1
        return True

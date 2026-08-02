import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        s = re.sub(r'[^A-Za-z0-9]','',s)
        return True if s[::-1] == s else False
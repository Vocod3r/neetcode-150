class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if(Counter(t) == Counter(s)):
            return True
        else:
            return False
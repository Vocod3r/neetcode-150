class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if(len(s)!= len(t)):
            return False

        else:
            if(Counter(t) == Counter(s)):
                return True
            else:
                return False
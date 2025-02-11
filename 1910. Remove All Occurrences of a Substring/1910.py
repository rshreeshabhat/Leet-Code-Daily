class Solution:
    def removeOccurrences(self, s: str, t: str) -> str:
        while t in s:
            s= s.replace(t,'',1)
        return s
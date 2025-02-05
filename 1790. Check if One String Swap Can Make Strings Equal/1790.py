from typing import Counter
class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        if Counter(s1) != Counter(s2):
            return False
        else:
            c = 0
            for i,j in enumerate(s1):
                if j != s2[i]:
                    c+=1
                if c>2:
                    return False
            return True    
class Solution:
    def clearDigits(self, s: str) -> str:
        c = []
        for i in s:
            if i.isalpha():
                c.append(i)
            else:
                c.pop()  
        return ''.join(c)



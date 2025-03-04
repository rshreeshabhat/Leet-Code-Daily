class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        while n > 1:
            n, reminder = (divmod(n,3))
            if reminder == 2:
                return False
        return True
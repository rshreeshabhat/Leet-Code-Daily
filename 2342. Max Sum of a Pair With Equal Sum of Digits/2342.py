class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        s= {}
        a = -1
        def sod(n):
            r = 0
            while n:
                r, n = r + n % 10, n // 10
            return r
        for n in nums:
            k = sod(n)
            if k in s:
                a = max(a,n+s[k])
                s[k] = max(s[k],n)
            else:
                s[k] = n
        return a
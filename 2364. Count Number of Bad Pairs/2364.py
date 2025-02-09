class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        d = {}
        s = 0
        for i in range(len(nums)):
            k = i - nums[i]
            if k in d:
                s += i - d[k]
            else:
                s += i
            d[k] = d.get(k,0) + 1
        return s
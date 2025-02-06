from typing import Counter


class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        s = 0
        n = []
        for i in range(len(nums)):
            for j in range(i):
                n.append(nums[i]*nums[j])
        p= Counter(n)
        for k in p:
            if p[k] >1:
                s += int((p[k]*(p[k]-1))/2)*8
        return s
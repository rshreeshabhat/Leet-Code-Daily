class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        m = 0
        increasing = 0
        s=0
        if len(nums) == 1:
            return nums[0]
        for i in range(0,len(nums)-1):

            if nums[i]<nums[i+1] and increasing == 1:
                s += nums[i+1]
            if nums[i]<nums[i+1] and increasing == 0:
                s=nums[i]+nums[i+1]
                increasing = 1
            if nums[i]>= nums[i+1] and increasing == 0:
                increasing = 0
                m=max(m,nums[i])
                s=0
            if nums[i]>= nums[i+1] and increasing == 1:
                increasing = 0
                m=max(m,s)
                s=0
            m = max(m,s)

        return m
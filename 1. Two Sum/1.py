class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        i = 0
        while i < len(nums)-1:
            j = 0
            for j in range(i+1,len(nums)):
                if nums[i]+nums[j] == target:
                    return [i,j]
            i+=1
        return []
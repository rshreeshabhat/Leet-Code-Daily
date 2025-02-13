import heapq

class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        s = 0
        heapq.heapify(nums)
        while nums[0] < k and len(nums) > 1:
            x = heapq.heappop(nums)
            y = heapq.heappop(nums)
            heapq.heappush(nums,int(x*2)+int(y))
            s+=1
        return s
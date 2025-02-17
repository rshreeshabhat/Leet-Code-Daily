class Solution:
    def maxArea(self, h: List[int]) -> int:
        a = 0
        l,r = 0,len(h)-1
        while l<r:
            a = max(min(h[l],h[r])*(r-l),a)
            if h[l]<=h[r]:
                l+=1
            else:
                r-=1
        return a
class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        s = ''
        for i in nums:

            if i%2 == 1:
                if s == 'even' or s == '':
                    s = 'odd'
                else:
                    return False
            if i%2 == 0:
                if s == 'odd' or s == '':
                    s = 'even'
                else:
                    return False
        return True
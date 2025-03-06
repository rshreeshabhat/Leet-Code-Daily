class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        s = [n for n in range(1,(len(grid)**2)+1)]
        t = []
        for i in range(0,(len(grid)**2)):
            j = i//len(grid)
            k = i%len(grid)
            if grid[j][k] in s and grid[j][k] not in t:
                s.remove(grid[j][k])
                t.append(grid[j][k])
            else:
                s.append(grid[j][k])
        return s[::-1]
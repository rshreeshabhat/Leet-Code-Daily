class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = {(i, j): set() for i in range(3) for j in range(3)}       
        for i in range(9):
            for j in range(9):
                num = board[i][j]
                if num == '.':
                    continue               
                if num in rows[i] or num in cols[j] or num in boxes[(i // 3, j // 3)]:
                    return False                
                rows[i].add(num)
                cols[j].add(num)
                boxes[(i // 3, j // 3)].add(num)
        return True
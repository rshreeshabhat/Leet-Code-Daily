class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:  # Check if the matrix is empty
            return False

        # Get the number of rows and columns
        rows, cols = len(matrix), len(matrix[0])

        # Use binary search on the 2D matrix treated as a 1D array
        left, right = 0, rows * cols - 1

        while left <= right:
            # Calculate the middle index in the "1D" representation
            mid = (left + right) // 2

            # Map the 1D index back to the 2D matrix
            row, col = divmod(mid, cols)
            mid_val = matrix[row][col]

            # Check if the middle value matches the target
            if mid_val == target:
                return True
            elif mid_val < target:
                left = mid + 1  # Search the right half
            else:
                right = mid - 1  # Search the left half

        return False  # Target not found

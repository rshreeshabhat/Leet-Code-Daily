class Solution:
    def lexicographicallySmallestArray(self, nums: list[int], limit: int) -> list[int]:
        # Initialize the answer array with zeroes, same size as nums.
        ans = [0] * len(nums) 
        # Create a list of tuples with each number and its index, then sort them by the number.
        # Sorting ensures numbers are considered in ascending order for grouping.
        numAndIndexes = sorted([(num, i) for i, num in enumerate(nums)]) 
        # This will hold groups of (num, index) pairs that are close enough based on the `limit`.
        numAndIndexesGroups: list[list[tuple[int, int]]] = []
        # Group the numbers based on the `limit` difference.
        for numAndIndex in numAndIndexes:
            # If the group list is empty or the difference between the current number
            # and the last number in the previous group exceeds the `limit`, start a new group.
            if (not numAndIndexesGroups or
                    numAndIndex[0] - numAndIndexesGroups[-1][-1][0] > limit):
                numAndIndexesGroups.append([numAndIndex])  # Start a new group.
            else:
                # Otherwise, add the current number to the last group.
                numAndIndexesGroups[-1].append(numAndIndex)
        # Reorder numbers within each group to ensure lexicographical smallest order.
        for numAndIndexesGroup in numAndIndexesGroups:
            # Extract numbers and their indices separately.
            sortedNums = [num for num, _ in numAndIndexesGroup]  # Numbers in the group.
            sortedIndices = sorted([index for _, index in numAndIndexesGroup])  # Indices in sorted order.
            # Assign the sorted numbers to their respective sorted indices in the result array.
            for num, index in zip(sortedNums, sortedIndices):
                ans[index] = num
        return ans

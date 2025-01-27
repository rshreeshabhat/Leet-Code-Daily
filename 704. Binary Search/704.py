class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # Initialize pointers for the left (l) and right (r) boundaries of the search range
        l, r = 0, len(nums) - 1

        # Loop until the pointers overlap or cross each other
        while l <= r:
            # Calculate the middle index
            # Using (l + r) // 2 to find the midpoint. This avoids overflow in some languages but isn't an issue in Python.
            mid = (r + l) // 2

            # Check if the target is at the midpoint
            if nums[mid] == target:
                return mid  # Return the index if the target is found
            
            # If the target is greater than the middle element, search in the right half
            if nums[mid] < target:
                l = mid + 1  # Move the left pointer to mid + 1
            
            # If the target is smaller than the middle element, search in the left half
            else:
                r = mid - 1  # Move the right pointer to mid - 1

        # If the loop ends, the target is not in the list
        return -1

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # Helper function to calculate the total hours required for a given eating speed
        def canFinish(speed: int) -> bool:
            total_hours = 0
            for pile in piles:
                # Use ceil division to calculate hours needed for each pile
                total_hours += (pile + speed - 1) // speed
            return total_hours <= h

        # Binary search over the range of possible eating speeds
        left, right = 1, max(piles)  # Minimum speed is 1, maximum is the largest pile

        while left < right:
            mid = (left + right) // 2
            if canFinish(mid):
                right = mid  # Try a smaller speed
            else:
                left = mid + 1  # Increase the speed

        return left  # `left` will be the minimum speed Koko needs
                                
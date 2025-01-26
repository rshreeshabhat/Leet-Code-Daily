class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Filter out non-alphanumeric characters and convert to lowercase in one step
        filtered_s = ''.join([i.lower() for i in s if i.isalnum()])
        
        # Check if the filtered string is equal to its reverse
        return filtered_s == filtered_s[::-1]
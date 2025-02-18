class Solution:
    def smallestNumber(self, pattern: str) -> str:
        stack = []  # Stack to store numbers before popping
        result = "" # Final output string
        num = 1     # Start with the smallest possible digit (1 to n+1)
        # Loop through the pattern and process each character
        for char in pattern:
            stack.append(num)  # Push the current number to stack
            num += 1           # Move to the next number
            # If we encounter an 'I', pop all elements from stack
            if char == 'I':
                while stack:
                    result += str(stack.pop())
        # Push the last remaining number (n+1)
        stack.append(num)
        # Pop and add remaining numbers from stack to result
        while stack:
            result += str(stack.pop())
        return result
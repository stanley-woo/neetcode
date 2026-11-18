class Solution:
    def removeStars(self, s: str) -> str:
        # 1. Initialize a LIFO stack to track surviving characters in left-to-right order
        stack = []
        char_list = list(s)

        # 2. Scan each character: pop the most recent character on '*', otherwise push
        for char in char_list:
            if char == '*':
                stack.pop()
            else:
                stack.append(char)

        # 3. Join the surviving characters into the final string
        return ''.join(stack)
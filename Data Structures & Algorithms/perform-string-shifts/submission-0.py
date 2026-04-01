class Solution:
    def stringShift(self, s: str, shift: List[List[int]]) -> str:
        for direction, amount in shift:
            amount %= len(s)
            if direction == 0:
                # Move necessary amount of characters from start to end
                s = s[amount:] + s[:amount]
            else:
                # Move necessary amount of characters from end to start
                s = s[-amount:] + s[:-amount]
        return s
class Solution:
    def minSwaps(self, s: str) -> int:
        open_counts, close_counts = 0, 0
        res = 0
        for char in s:
            if char == '[':
                open_counts += 1
            else:
                close_counts += 1
            balance = open_counts - close_counts
            res = max(res, -balance)
        
        return math.ceil(res / 2)       
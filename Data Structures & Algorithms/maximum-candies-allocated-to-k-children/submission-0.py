class Solution:
    def maximumCandies(self, candies: list[int], k: int) -> int:
        n = len(candies)
        if sum(candies) < k:
            return 0
            
        low = 1
        high = max(candies)
        res = 0

        while low <= high:
            mid = low + (high - low) // 2
            total_piles = sum(c // mid for c in candies)
            if total_piles >= k:
                res = mid
                low = mid + 1
            else:
                high = mid - 1
        
        return res
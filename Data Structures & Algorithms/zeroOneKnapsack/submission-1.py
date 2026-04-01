class Solution:
    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:
        n = len(profit)
        dp = [[0] * (capacity + 1) for _ in range(n + 1)]

        # Note: You don't actually need to manually set dp[0][j] to 0 
        # because Python already initialized the whole matrix to 0!

        # Loop 'i' from 1 to n (representing "considering the first i items")
        for i in range(1, n + 1):
            for j in range(capacity + 1):
                # The current item's weight and profit are at index i - 1
                curr_weight = weight[i - 1]
                curr_profit = profit[i - 1]
                
                if curr_weight <= j:
                    # Option 1: Skip it (take value from row above)
                    # Option 2: Include it (profit + value from row above minus weight)
                    dp[i][j] = max(dp[i - 1][j], curr_profit + dp[i - 1][j - curr_weight])
                else:
                    # Can't fit it, must skip
                    dp[i][j] = dp[i - 1][j]
                    
        return dp[-1][-1]
class Solution:
    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:
        dp = [[0] * (capacity + 1) for _ in range(len(profit)+1)]
        dp[0][0] = 0

        # No profit no matter how much capacity.
        for j in range(capacity):
            dp[0][j] = 0
        
        for i in range(len(profit)):
            for j in range(capacity + 1):
                if weight[i] <= j:
                    dp[i+1][j] = max(dp[i][j], profit[i] + dp[i][j - weight[i]])
                else:
                    dp[i+1][j] = dp[i][j]
        return dp[-1][-1]
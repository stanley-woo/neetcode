class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        n = len(s)
        dp = [False] * n
        dp[0] = True

        reachable_count = 0

        for i in range(1, n):
            added = i - minJump
            removed = i - maxJump - 1

            if added >= 0 and dp[added]:
                reachable_count += 1
            
            if removed >= 0 and dp[removed]:
                reachable_count -= 1
            
            dp[i] = s[i] == '0' and reachable_count > 0
        
        return dp[n - 1]
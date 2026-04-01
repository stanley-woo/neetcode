class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        dp = [[False] * (len(t) + 1) for _ in range(len(s) + 1)]

        for j in range(len(t)+1):
            dp[-1][j] = True

        for i in range(len(s) - 1, -1, -1):
            for j in range(len(t)-1, -1 , -1):
                if s[i] == t[j]:
                    dp[i][j] = dp[i+1][j+1]
                else:
                    dp[i][j] = dp[i][j+1]
        return dp[0][0]
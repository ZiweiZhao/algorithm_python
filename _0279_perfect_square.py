class Solution:
    def numSquares(self, n):
        dp = [sys.maxsize]*(n+1)
        i = 1
        while i*i <= n:
            dp[i*i] = 1
            i += 1
        for i in range(n+1):
            j = 1
            while i + j*j <= n:
                dp[i+j*j] = min(dp[i]+1, dp[i+j*j])
                j+=1
        return dp[n]

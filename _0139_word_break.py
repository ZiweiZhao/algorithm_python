class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        # DP solution
        if not wordDict:
            return len(s) == 0
        dp = [False]*(len(s)+1)
        dp[0] = True
        for i in range(1, len(s)+1):
            for j in range(i):
                if dp[j] and s[j:i] in wordDict:
                    dp[i] = True
                    break
        return dp[-1]
#DFS WITH MEMO
#Top down DP
class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        if not wordDict:
            return len(s) == 0
        wordDict = set(wordDict)
        return self.dfs(s, wordDict, {})
        
    def dfs(self, s, wordDict, memo):
        if s in memo:
            return memo[s]
        if s in wordDict:
            return True
        value = False
        for i in range(1, len(s)+1):
            if s[:i] in wordDict:
                value = self.dfs(s[i:], wordDict, memo)
                if value:
                    break
        memo[s] = value
        return value
                

        
class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        if not s:
            return []
        res = []
        self.dfs([], s, 0, res)
        return res      
    
    def dfs(self, cur, s, idx, res):
        if idx == len(s):
            res.append(copy.deepcopy(cur))
            return
        for i in range(idx, len(s)+1):
            if not self.isP(s[idx:i+1]):
                continue
            cur.append(s[idx:i+1])
            self.dfs(cur, s, i+1, res)
            cur.pop()

    def isP(self, s):
        return s == s[::-1]

class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        res = []
        self.dfs([], 1, n, k, res)
        return res
        
    def dfs(self, cur, idx, target, k, res):
        if target == 0 and k == 0:
            res.append(copy.deepcopy(cur))
            return
        for i in range(idx, 10):
            if target-i < 0:
                return
            cur.append(i)
            self.dfs(cur, i+1, target-i, k-1, res)
            cur.pop(-1)
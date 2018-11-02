class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        if not candidates:
            return []
        candidates.sort()
        res = []
        self.dfs(candidates, [], 0, target, res)
        return res
    def dfs(self, candidates, cur, idx, target, res):
        if target == 0:
            res.append(list(cur))
            return
        for i in range(idx, len(candidates)):
            if i>idx and candidates[i] == candidates[i-1]:
                continue
            if target - candidates[i] < 0:
                return
            cur.append(candidates[i])
            self.dfs(candidates, cur, i+1, target-candidates[i], res)
            cur.pop(-1)

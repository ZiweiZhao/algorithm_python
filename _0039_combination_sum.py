class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        if not candidates or len(candidates) == 0:
            return []
        candidates = sorted(list(set(candidates)))
        self.result = []
        self.helper(candidates, 0, [], target)
        return self.result
        
        
    def helper(self, candidates, start, cur, target):
        if target == 0:
            self.result.append(list(cur))
        for i in range(start, len(candidates)):
            if target < candidates[i]:
                return
            cur.append(candidates[i])
            self.helper(candidates, i, cur, target-candidates[i])
            cur.pop(-1)
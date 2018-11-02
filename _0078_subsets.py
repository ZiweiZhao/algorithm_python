class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        self.ret = []
        if not nums or len(nums) == 0:
            return [[]]
        nums.sort()
        cur = []
        self.helper(nums, cur, 0)
        return self.ret
    def helper(self, nums, cur, idx):
        if idx >= len(nums):
            self.ret.append(copy.deepcopy(cur))
            return
        cur.append(nums[idx])
        self.helper(nums, cur, idx+1)
        cur.pop(-1)
        self.helper(nums, cur, idx+1)

    def helper(self, nums, cur, idx):
        self.ret.append(copy.deepcopy(cur))
        for i in range(idx,len(nums)):
            cur.append(nums[i])
            self.helper(nums,cur,i+1)
            cur.pop(-1)
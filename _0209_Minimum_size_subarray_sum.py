class Solution:
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        left = curSum = 0
        ret = len(nums) + 1
        for right, cur in enumerate(nums):
            curSum += cur
            while curSum >= s:
                ret = min(ret, right-left+1)
                curSum -= nums[left]
                left += 1
        if ret > len(nums):
            ret = 0
        return ret
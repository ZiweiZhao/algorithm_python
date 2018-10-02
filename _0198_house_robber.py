# easist DP
class Solution:
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0 or not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        dp = [None] * len(nums)
        # init
        dp[0] = nums[0]
        dp[1] = max(nums[0],nums[1])
        # dp equations
        for i in range(2, len(nums)):
            dp[i] = max(dp[i-1], dp[i-2] + nums[i])
        return dp[-1]

# O(1) space
class Solution:
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0 or not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        dp = [None] * 3
        # init
        dp[0] = nums[0]
        dp[1] = max(nums[0],nums[1])
        # dp equations
        for i in range(2, len(nums)):
            dp[i%3] = max(dp[(i-1)%3], dp[(i-2)%3] + nums[i])
        return dp[len(nums)%3-1]
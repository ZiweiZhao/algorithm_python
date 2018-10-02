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
        if len(nums) == 2:
            return max(nums[0], nums[1])
        return max(self.dp(nums[1:]), self.dp(nums[:-1]))
    
    def dp(self, nums):
        dp = [None]*3
        dp[0],dp[1] = nums[0], max(nums[0], nums[1])
        for i in range(2,len(nums)):
            dp[i%3] = max(dp[(i-1)%3], dp[(i-2)%3] + nums[i])
        return dp[(len(nums)-1)%3]
        
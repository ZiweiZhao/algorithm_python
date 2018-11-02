class Solution:
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums:
            return []
        nums.sort()
        ret = sys.maxsize
        val = 0
        for i in range(len(nums)-2):
            left, right = i+1, len(nums)-1
            while left<right:
                if ret > abs(target-nums[i]-nums[left]-nums[right]):
                    ret = abs(target-nums[i]-nums[left]-nums[right])
                    val = nums[i]+nums[left]+nums[right]
                if target-nums[i]-nums[left]-nums[right] < 0:
                    right -= 1
                else:
                    left+=1
        return val
        
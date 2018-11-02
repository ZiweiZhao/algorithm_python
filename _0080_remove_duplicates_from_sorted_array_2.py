class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        i = 0
        for n in nums:
            if i < 2 or nums[i-2] < n:
                nums[i] = n
                i += 1
        return i
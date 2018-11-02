class Solution:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if not nums:
            return []
        nums.sort()
        ret = []
        for i in range(len(nums)-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            target = 0 - nums[i]
            left = i+1
            right = len(nums)-1
            while left < right:
                if nums[left] + nums[right] == target:
                    ret.append([nums[i], nums[left], nums[right]])
                    right-=1
                    left+=1
                    while left<right and nums[left] == nums[left-1]:
                        left += 1
                    while left<right and nums[right] == nums[right+1]:
                        right -= 1
                elif nums[left] + nums[right] < target:
                    left+=1
                else:
                    right-=1
        return ret
                    
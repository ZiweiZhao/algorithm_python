class Solution:
    # need to take care the runtime when using Python
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        if not nums:
            return []
        nums.sort()
        ret = []
        for i in range(len(nums)-3):
            if i>0 and nums[i] == nums[i-1]:
                continue
            if nums[i]*4 > target:
                    break
            for j in range(i+1, len(nums)-2):
                if j!= i+1 and nums[j] == nums[j-1]:
                    continue
                if (nums[i]+nums[j])*2 > target:
                    break
                left,right = j+1, len(nums)-1
                while left < right:
                    if nums[i] + nums[j] + nums[left] + nums[right] == target:
                        ret.append([nums[i], nums[j], nums[left], nums[right]])
                        left += 1
                        right -= 1
                        while left < right and nums[left] == nums[left-1]:
                            left += 1
                        while left < right and nums[right] == nums[right+1]:
                            right -= 1
                    elif nums[i] + nums[j] + nums[left] + nums[right] < target:
                        left += 1
                    else:
                        right -= 1
        return ret
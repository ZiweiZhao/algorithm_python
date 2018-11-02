class Solution:
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if not nums:
            return None
        return self.quickSelect(nums, 0, len(nums)-1, k)
        
    def quickSelect(self, nums, start, end, k):
        if start == end:
            return nums[start]
        left = start
        right = end
        pivot = nums[(start+end)//2]
        while left <= right:
            while left<=right and nums[left] > pivot:
                left += 1
            while left<=right and nums[right] < pivot:
                right -= 1
            if left <= right:
                nums[left], nums[right] = nums[right], nums[left]
                left+=1
                right-=1
        if start+k-1 >= left:
            return self.quickSelect(nums, left, end, k-(left-start))
        elif start+k-1 <= right:
            return self.quickSelect(nums, start, right, k)
        return nums[right+1]
        
class Solution(object):
    def closestValue(self, root, target):
        """
        :type root: TreeNode
        :type target: float
        :rtype: int
        """
        lower = self.lowerBound(root, target)
        upper = self.upperBound(root, target)
        if lower and upper:
            if abs(lower.val - target) < abs(upper.val - target):
                return lower.val
            else:
                return upper.val
        if not lower:
            return upper.val
        else:
            return lower.val
        
    def lowerBound(self, root, target):
        if not root:
            return
        while root.val > target:
            return self.lowerBound(root.left, target)
        # root.val <= target:
        temp = self.lowerBound(root.right, target)
        if temp:
            return temp
        return root
    
    def upperBound(self, root, target):
        if not root:
            return
        while root.val < target:
            return self.upperBound(root.right, target)
        # root.val >= target:
        temp = self.upperBound(root.left, target)
        if temp:
            return temp
        return root
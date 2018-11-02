class Solution:
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        return self.helper(root.left, root.right)
    def helper(self, left, right):
        if not left and not right:
            return True
        if not left or not right:
            return False
        if left.val == right.val:
            return self.helper(left.left, right.right) and self.helper(left.right, right.left)
        else:
            return False
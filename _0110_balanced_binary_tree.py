class Solution:
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        return self.helper(root)[0]
    def helper(self, node):
        if not node:
            return (True, 0)
        height = 0
        left_bool, l_height = self.helper(node.left)
        right_bool, r_height = self.helper(node.right)
        if left_bool and right_bool and abs(l_height-r_height) <= 1:
            height = max(l_height, r_height) + 1
            return (True, height)
        return (False, -1)
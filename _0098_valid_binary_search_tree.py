class Solution:
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.helper(root, sys.maxsize, -sys.maxsize)
    
    def helper(self,node, rightMin, leftMax):
        if not node:
            return True
        if node.val >= rightMin or node.val <= leftMax:
            return False
        return self.helper(node.left, node.val, leftMax) and self.helper(node.right, rightMin, node.val) 
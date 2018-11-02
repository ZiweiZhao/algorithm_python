# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
# Traversal method
class Solution:
    prev = None
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        if not root:
            return
        if self.prev:
            self.prev.left = None
            self.prev.right = root
        self.prev = root
        temp = root.right
        self.flatten(root.left)
        self.flatten(temp)
# divide and conqur method
class Solution:
    prev = None
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        self.helper(root)
        
    def helper(self, node):
        if not node:
            return
        leftN = self.helper(node.left)
        rightN = self.helper(node.right)
        if not leftN:
            return node
        node.left = None
        node.right = leftN
        while leftN.right:
            leftN = leftN.right
        leftN.right = rightN
        return node
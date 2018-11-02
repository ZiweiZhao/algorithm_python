# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        if not root:
            return []
        if not root.right and not root.left:
            return [str(root.val)]
        path = []
        for i in self.binaryTreePaths(root.left):
            path.append(str(root.val) + "->" + i)
        for i in self.binaryTreePaths(root.right):
            path.append(str(root.val) + "->" + i)
        return path
        
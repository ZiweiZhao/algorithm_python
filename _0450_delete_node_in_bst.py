# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def deleteNode(self, root, key):
        if not root:
            return None
        if root.val == key:
            if not root.left and not root.right:
                return None
            elif root.left and not root.right:
                return root.left
            elif root.right and not root.left:
                return root.right
            else:
                successor= self.findNext(root)
                root.val = successor.val
                root.right = self.deleteNode(root.right, root.val)
        if root.val < key:
            root.right = self.deleteNode(root.right, key)
        if root.val > key:
            root.left = self.deleteNode(root.left, key)
        return root
        
    def findNext(self, node):
        node = node.right
        while node.left:
            node = node.left
        return node
            
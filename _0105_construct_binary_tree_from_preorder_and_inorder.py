class Solution:
    def buildTree(self, preorder, inorder):
        """
        :rtype: TreeNode
        """
        if not inorder:
            return
        idx = inorder.index(preorder.pop(0))
        root = TreeNode(inorder[idx])
        root.left = self.buildTree(preorder, inorder[:idx])
        root.right = self.buildTree(preorder, inorder[idx+1:])
        return root
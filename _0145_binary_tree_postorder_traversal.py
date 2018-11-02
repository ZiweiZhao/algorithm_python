class Solution:
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        ret = []
        self.traversal(root,ret)
        return ret
    def traversal(self, root,ret):
        if not root:
            return
        self.traversal(root.left, ret)
        self.traversal(root.right, ret)
        ret.append(root.val)
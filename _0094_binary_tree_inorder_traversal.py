# iteration version
class Solution:
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        ret = []
        stack = []
        while root:
            stack.append(root)
            root = root.left
        while stack:
            node = stack[-1]
            ret.append(node.val)
            if node.right:
                node = node.right
                while node:
                    stack.append(node)
                    node = node.left   
            else:
                node = stack.pop()
                while stack and stack[-1].right == node:
                    node = stack.pop()
        return ret
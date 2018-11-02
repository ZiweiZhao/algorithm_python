# Recursion
# O(n)
class Solution:
    idx = 0
    ret = 0
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        self.helper(root, k)
        return self.ret
    
    def helper(self, node, k):
        if not node:
            return
        self.helper(node.left, k)
        self.idx += 1
        if self.idx == k:
            self.ret = node.val
            return
        self.helper(node.right, k)

#iterative
class Solution:
    idx = 0
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        stack = []
        while root:
            stack.append(root)
            root = root.left
        while stack:
            node = stack[-1]
            # print(node.val)
            self.idx += 1
            if self.idx == k:
                return node.val
            if node.right:
                node = node.right
                while node:
                    stack.append(node)
                    node = node.left
            else:
                node = stack.pop()
                while stack and stack[-1].right == node:
                    node = stack.pop()    

#quickselect:
class Solution:
    _dict = {}
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        self.count(root)
        return self.quickSelectOnBst(root, k)
    
    def count(self, root):
        if not root:
            return 0
        left = self.count(root.left)
        right = self.count(root.right)
        self._dict[root] = left+right+1
        return left+right+1
    
    def quickSelectOnBst(self, root, k):
        if not root:
            return -1
        left = 0
        if root.left:
            left = self._dict[root.left]
        if left == k-1:
            return root.val
        if left>=k:
            return self.quickSelectOnBst(root.left, k)
        else:
            return self.quickSelectOnBst(root.right, k-left-1)
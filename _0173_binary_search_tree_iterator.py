# Definition for a  binary tree node
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class BSTIterator(object):
    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.stack = []
        while root:
            self.stack.append(root)
            root = root.left
        

    def hasNext(self):
        """
        :rtype: bool
        """
        return len(self.stack) != 0

    def next(self):
        """
        :rtype: int
        """
        node = self.stack[-1]
        ret = node
        if node.right:
            node = node.right
            while node:
                self.stack.append(node)
                node = node.left
        else:
            node = self.stack.pop()
            while self.stack and self.stack[-1].right == node:
                node = self.stack.pop()
        return ret.val

# Your BSTIterator will be called like this:
# i, v = BSTIterator(root), []
# while i.hasNext(): v.append(i.next())
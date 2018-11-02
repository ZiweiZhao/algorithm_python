class Solution(object):
    def closestKValues(self, root, target, k):
        if not root:
            return []
        self.ret = []
        self.min = sys.maxsize
        self.traverse = []
        self.traverseNode(root)
        self.helper(self.traverse, target, k)
        return self.ret
        
    def traverseNode(self, node):
        if not node:
            return
        self.traverseNode(node.left)
        self.traverse.append(node)
        self.traverseNode(node.right)
    
    def helper(self, nodes, target, k):
        mid = 0
        for i in range(len(nodes)):
            if abs(nodes[i].val - target) < self.min:
                self.min = abs(nodes[i].val - target)
                mid = i
        left, right = mid-1, mid+1
        count = 1
        self.ret.append(nodes[mid].val)
        while count < k:
            if right >= len(nodes) or abs(target - nodes[left].val) <= abs(target-nodes[right].val):
                self.ret.append(nodes[left].val)
                left -= 1
            else:
                self.ret.append(nodes[right].val)
                right += 1
            count += 1
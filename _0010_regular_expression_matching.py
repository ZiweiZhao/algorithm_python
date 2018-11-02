class Solution(object):
    # TOP DOWN
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        return self.helper(s, 0, p, 0, {})
        
    def helper(self, s, i, p, j, memo):
        if (i,j) in memo:
            return memo[(i,j)]
        if i >= len(s):
            return self.is_empty(p[j:])
        if j >= len(p):
            return False
        if j+1 < len(p) and p[j+1] == '*':
            result = self.helper(s, i, p, j+2, memo) or (self.is_equal(s[i], p[j]) and self.helper(s, i+1, p, j, memo))
        else:
            result = self.is_equal(s[i], p[j]) and self.helper(s, i+1, p, j+1, memo)
        memo[(i,j)] = result
        return result
    def is_equal(self, a, b):
        return a == b or b == '.'
        
    def is_empty(self, p):
        if len(p)%2 != 0:
            return False
        for i in range(0, len(p), 2):
            if p[i] == '*' or p[i+1] != '*':
                return False
        return True
        
        
            
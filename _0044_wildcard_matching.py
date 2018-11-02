class Solution(object):
    # o(m*n)
    # no memo: o(2^n)
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
            for idx in range(j, len(p)):
                if p[idx] != '*':
                    return False
            return True
        if j >= len(p):
            return False
        result = False
        if p[j] == '*':
            result = self.helper(s, i+1, p, j, memo) or self.helper(s, i, p, j+1, memo)
        else:
            result = self.equal(s[i], p[j]) and self.helper(s, i+1, p, j+1, memo)
        memo[(i,j)] = result
        return result
            
    def equal(self, a, b):
        return b == '?' or a==b
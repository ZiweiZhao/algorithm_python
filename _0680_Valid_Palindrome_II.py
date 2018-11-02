class Solution:
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        i,j = 0,len(s)-1
        while i< j:
            if s[i] != s[j]:
                if self.isP(s[i:j]) or self.isP(s[i+1:j+1]):
                    return True
                else:
                    return False
            i+=1
            j-=1
        return True
            
    def isP(self, s):
        i,j = 0,len(s)-1
        while i< j:
            if s[i] != s[j]:
                return False
            i+=1
            j-=1
        return True
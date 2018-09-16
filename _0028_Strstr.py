class Solution:
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if not needle:
            return 0
        base = 10**6
        target = 0
        power = 1
        val = 0
        for i in range(len(needle)):
            power = (power*31)%base
            
        for i in range(len(needle)):
            target = (target*31 + ord(needle[i]))%base
        
        for i in range(len(haystack)):
            val = (val*31+ord(haystack[i]))%base
            if i < len(needle)-1:
                continue
            if i >= len(needle):
                val = val - (ord(haystack[i-len(needle)])*power) % base
                if val < 0:
                    val += base
                val = val%base
            if val == target:
                if haystack[i-len(needle)+1:i+1] == needle:
                    return i-len(needle)+1
        
        return -1
        
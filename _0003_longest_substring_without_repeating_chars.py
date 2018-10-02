# two pointer 同向双指针 sliding window
class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s == None or len(s) == 0:
            return 0
        j = 0
        _set = set()
        ret = 0
        for i in range(len(s)):
            while j < len(s) and s[j] not in _set:
                print("h")
                _set.add(s[j])
                j+=1
            ret = max(ret, j-i)
            _set.remove(s[i])
        return ret
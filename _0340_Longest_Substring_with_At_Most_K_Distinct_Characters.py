class Solution:
    def lengthOfLongestSubstringKDistinct(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        max_len = 0
        ret = j = 0
        cur_len = 0
        _dict = {}
        for i in range(len(s)):
            while j < len(s) and len(_dict) <= k:
                _dict[s[j]] = _dict.get(s[j],0) + 1
                j += 1
            if len(_dict) <= k:
                max_len = max(max_len, j-i)
            else:
                max_len = max(max_len, j-i-1)
            _dict[s[i]] -= 1
            if _dict[s[i]] == 0:
                _dict.pop(s[i])
        return max_len
# two pointer 同向双指针 sliding window
class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s):
        """
        :type s: str
        :rtype: int
        """
        _dicts = {}
        ret = 0
        j = 0
        for i in range(len(s)):
            while j<len(s) and len(_dicts) <= 2:
                if not s[j] in _dicts:
                    _dicts[s[j]] = 1
                else:
                    _dicts[s[j]] += 1
                j += 1
            if len(_dicts) > 2:
                ret = max(ret, j-i-1)
            elif j==len(s):
                ret = max(ret, j-i)
            if _dicts[s[i]] == 1:
                _dicts.pop(s[i])
            elif _dicts[s[i]] > 1:
                _dicts[s[i]] -= 1
        return ret


class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s):
        """
        :type s: str
        :rtype: int
        """
        max_len = 0
        ret = j = 0
        cur_len = 0
        _dict = {}
        for i in range(len(s)):
            while j < len(s) and len(_dict) <= 2:
                _dict[s[j]] = _dict.get(s[j],0) + 1
                j += 1
            if len(_dict) <= 2:
                max_len = max(max_len, j-i)
            else:
                max_len = max(max_len, j-i-1)
            _dict[s[i]] -= 1
            if _dict[s[i]] == 0:
                _dict.pop(s[i])
        return max_len
                
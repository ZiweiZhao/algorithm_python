# two pointers
class Solution:
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        if len(t) > len(s):
            return ""
        j = 0
        min_len = len(s) + 1
        ret = ""
        _dict = {}
        for i in range(len(t)):
            _dict[t[i]] = _dict.get(t[i],0)+1
        temp_dict = {}
        unique = len(_dict)
        cur_char = 0
        for i in range(len(s)):
            while j < len(s) and cur_char < unique:
                if s[j] in _dict:
                    temp_dict[s[j]] = temp_dict.get(s[j],0) + 1
                    if temp_dict[s[j]] == _dict[s[j]]:
                        cur_char += 1
                j += 1
            if cur_char != unique:
                break
            if j-i < min_len:
                ret = s[i:j]
                min_len = len(ret)
            if s[i] in _dict:
                if temp_dict[s[i]] == _dict[s[i]]:
                    cur_char -= 1
                temp_dict[s[i]] -= 1
        return ret
                
                
            
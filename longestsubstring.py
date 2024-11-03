# https://leetcode.com/problems/longest-substring-without-repeating-characters/
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        count_dict = {}
        i = -1
        for j, c in enumerate(s):
            while c in count_dict:
                i += 1
                count_dict[s[i]] -= 1
                if count_dict[s[i]] == 0:
                    del count_dict[s[i]]
            if c not in count_dict:
                count_dict[c] = 1
            else:
                count_dict[c] += 1

            res = max(res, j - i)
        return res

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        cMap = {}
        res = 0
        for right in range(len(s)):
            if s[right] in cMap:
                left = max(left, cMap[s[right]] + 1)
            cMap[s[right]] = right
            res = max(res, right - left + 1)
        return res

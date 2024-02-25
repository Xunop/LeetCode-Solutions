class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need = collections.Counter(t)
        l, r = 0, 0
        ans = ""
        min_length = float('inf')
        while (r < len(s)):
            need[s[r]] -= 1
            r += 1
            while (all(map(lambda x: x <= 0, need.values()))):
                if (r - l + 1 < min_length):
                    ans = s[l:r]
                    min_length = r - l + 1
                need[s[l]] += 1
                l += 1
        return ans if ans else ""

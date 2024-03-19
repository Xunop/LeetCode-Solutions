class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(s) < len(p): return []
        res = []
        p_count = [0] * 26
        s_count = [0] * 26
        # Create the initial count of the first len(p) characters
        for i in range(len(p)):
            p_count[ord(p[i]) - ord('a')] += 1
            s_count[ord(s[i]) - ord('a')] += 1
        if p_count == s_count: res.append(0)
        # Slide the window and compare the count of the characters
        for i in range(len(p), len(s)):
            s_count[ord(s[i]) - ord('a')] += 1
            # Remove the count of the character that is out of the window
            # i-len(p) is the start of the window, since the window is of length len(p)
            s_count[ord(s[i - len(p)]) - ord('a')] -= 1
            if p_count == s_count: res.append(i - len(p) + 1)
        return res

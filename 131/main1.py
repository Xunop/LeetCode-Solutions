class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def is_palindrome(s):
            return s == s[::-1]
            
        res = []
        def backtracking(start, sub_strs):
            if start == len(s):
                res.append(sub_strs)
                return

            for i in range(start, len(s)):
                if is_palindrome(s[start:i + 1]):
                    print(s[start:i + 1])
                    backtracking(i + 1, sub_strs + [s[start:i]])
        backtracking(0, [])
        return res

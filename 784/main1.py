class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        res = []
        def dfs(index, cs):
            if index == len(s):
                res.append(cs)
                return
            if s[index].isalpha():
                dfs(index+1, cs+s[index].upper())
                dfs(index+1, cs+s[index].lower())
            else:
                dfs(index+1, cs+s[index])
        dfs(0, "")
        return res

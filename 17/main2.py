class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        if not digits:
            return res
        digit_map = {
            '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
            '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'
        }
        def dfs(index, path):
            if index == len(digits):
                res.append(path)
                return
            for c in digit_map[digits[index]]:
                dfs(index + 1, path + c)
        dfs(0, '')
        return res

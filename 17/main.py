class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        self.digits = digits
        self.digit_map = {
            '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
            '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'
        }
        self.res = []
        self.dfs(0, '')
        return self.res

    def dfs(self, index, path):
        if index == len(self.digits):
            self.res.append(path)
            return
        for c in self.digit_map[self.digits[index]]:
            self.dfs(index + 1, path + c)

class Solution:
    def punishmentNumber(self, n: int) -> int:
        res = 0
        def dfs(s_num, index, path, sum, res):
            if sum == n:
                res += int(path)
                return
            if sum > n:
                return
            for c in s_num[index:]:
                cur = int(c)
                if cur == n:
                    res += cur
                    return
                if cur > n:
                    return
                if path == "":
                    path = 0
                dfs(s_num, index + 1, str(path) + c, int(path) + cur)
        for i in range(n):
            dfs(str(i * i), 0, "", 0, res)
        return res

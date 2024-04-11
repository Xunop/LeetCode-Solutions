class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        self.ans = self.cur = 0
        def dfs(x, y):
            if x < 0 or x >= n or y < 0 or y >= m or grid[x][y] == 0:
                return
            self.cur += grid[x][y]
            tmp = grid[x][y]
            grid[x][y] = 0
            dfs(x + 1, y)
            dfs(x - 1, y)
            dfs(x, y + 1)
            dfs(x, y - 1)
            grid[x][y] = tmp

            self.ans = max(self.ans, self.cur)
            self.cur -= tmp
        for i in range(n):
            for j in range(m):
                if grid[i][j] != 0:
                    dfs(i, j)
        return self.ans

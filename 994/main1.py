
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    self.dfs(grid, i, j, 2)
        maxTime = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    return -1
                maxTime = max(maxTime, grid[i][j])
        return maxTime - 2 if maxTime > 0 else 0

    def dfs(self, grid, i, j, time):
        if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]):
            return
        # If the cell is not empty and the time is less than the current time, return
        if grid[i][j] != 1 and grid[i][j] < time:
            return
        grid[i][j] = time
        self.dfs(grid, i - 1, j, time + 1)
        self.dfs(grid, i + 1, j, time + 1)
        self.dfs(grid, i, j - 1, time + 1)
        self.dfs(grid, i, j + 1, time + 1)

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # BFS
        queue = deque()
        fresh = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    queue.append((i, j, 0))
                if grid[i][j] == 1:
                    fresh += 1
        if fresh == 0:
            return 0
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        while queue:
            i, j, time = queue.popleft()
            for dx, dy in directions:
                x, y = i + dx, j + dy
                if 0 <= x < len(grid) and 0 <= y < len(grid[0]) and grid[x][y] == 1:
                    fresh -= 1
                    grid[x][y] = 2
                    queue.append((x, y, time + 1))
                    if fresh == 0:
                        return time + 1
        return -1

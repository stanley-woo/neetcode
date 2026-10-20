class Solution:
    def countUnguarded(self, m: int, n: int, guards: list[list[int]], walls: list[list[int]]) -> int:
        grid = [[0] * n for _ in range(m)]

        for r, c in guards:
            grid[r][c] = 1
        for r, c in walls:
            grid[r][c] = 2

        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        for x, y in guards:
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                while (0 <= nx < m) and (0 <= ny < n) and grid[nx][ny] != 1 and grid[nx][ny] != 2:
                    grid[nx][ny] = 3
                    nx += dx
                    ny += dy
        
        res = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    res += 1
        
        return res
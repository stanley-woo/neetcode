class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        q = deque()
        m, n = len(grid), len(grid[0])

        start_node = None
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    q.append((i, j))
                    grid[i][j] = -1
                    break
            if start_node:
                break
        
        res = 0
        directions = [(-1,0), (1, 0), (0, -1), (0, 1)]
        while q:
            r, c = q.popleft()
            for dx, dy in directions:
                nx, ny = r + dx, c + dy

                if 0 <= nx < m and 0 <= ny < n:
                    if grid[nx][ny] == 1:
                        grid[nx][ny] = -1
                        q.append((nx,ny))
                    elif grid[nx][ny] == 0:
                        res += 1
                else:
                    res += 1
        return res    
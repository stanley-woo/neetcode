class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        servers = set()
        for i in range(m):
            row_servers = set()
            for j in range(n):
                if grid[i][j] == 1:
                    row_servers.add((i, j))
            if len(row_servers) > 1:
                servers.update(row_servers)
        
        for j in range(n):
            col_servers = set()
            for i in range(m):
                if grid[i][j] == 1:
                    col_servers.add((i,j))
                if len(col_servers) > 1:
                    servers.update(col_servers)
        
        return len(servers)             
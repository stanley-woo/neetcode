class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:
        directions = [(1,2),(1,-2),(2,-1),(2,1),(-1,-2),(-1,2),(-2,-1),(-2,1)]

        def bfs(x,y):
            visited = set()
            q = deque([(0,0)])
            steps = 0

            while q:
                length = len(q)
                for i in range(length):
                    r, c = q.popleft()
                    if (r,c) == (x,y):
                        return steps
                    
                    for dr, dc in directions:
                        nr, nc = r + dr, c + dc

                        if (nr, nc) not in visited:
                            visited.add((nr,nc))
                            q.append((nr,nc))
                steps += 1
        
        return bfs(x,y)
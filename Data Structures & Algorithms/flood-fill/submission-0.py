class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        original_color = image[sr][sc]

        visited = set()
        m, n = len(image), len(image[0])
        directions = [(-1,0), (1, 0), (0, -1), (0, 1)]
        q = deque([(sr, sc)])
        image[sr][sc] = color

        while q:
            x, y = q.popleft()

            for dx, dy in directions:
                nx, ny = x + dx, y + dy

                if 0 <= nx < m and 0 <= ny < n and image[nx][ny] == original_color and (nx, ny) not in visited:
                    image[nx][ny] = color
                    visited.add((nx, ny))
                    q.append((nx, ny))
        
        return image
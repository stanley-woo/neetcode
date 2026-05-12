class SnakeGame:

    def __init__(self, width: int, height: int, food: List[List[int]]):
        self.height = height
        self.width = width
        self.snake = deque([(0,0)])
        self.body = {(0,0)}
        self.food = food
        self.foodIdx = 0

        self.directions = {"U" : (-1, 0), "D" : (1, 0), "L": (0, -1), "R":  (0, 1)}
    def move(self, direction: str) -> int:
        dx, dy = self.directions[direction]
        nx, ny = self.snake[0][0] + dx, self.snake[0][1] + dy

        cross_boundary1 = nx < 0 or nx >= self.height
        cross_boundary2 = ny < 0 or ny >= self.width

        bites_itself = (nx,ny) in self.body and (nx, ny) != self.snake[-1]

        if cross_boundary1 or cross_boundary2 or bites_itself:
            return -1
        
        next_food = self.food[self.foodIdx] if self.foodIdx < len(self.food) else None

        if self.foodIdx < len(self.food) and next_food[0] == nx and next_food[1] == ny:
            self.foodIdx += 1
        else:
            tail = self.snake.pop()
            self.body.remove(tail)

        self.snake.appendleft((nx, ny))
        self.body.add((nx,ny))

        return len(self.snake) - 1
        


# Your SnakeGame object will be instantiated and called as such:
# obj = SnakeGame(width, height, food)
# param_1 = obj.move(direction)

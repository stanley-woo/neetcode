class TicTacToe:

    def __init__(self, n: int):
        self.n = n
        self.rows = [0] * n
        self.cols = [0] * n
        self.diag = 0
        self.anti = 0

    def move(self, row: int, col: int, player: int) -> int:
        if player == 1:
            self.rows[row] += 1
            self.cols[col] += 1
            if self.rows[row] == self.n or self.cols[col] == self.n:
                return player
        else:
            self.rows[row] -= 1
            self.cols[col] -= 1
            if self.rows[row] == -1 * self.n or self.cols[col] == -1 * self.n:
                return player

        if row == col:
            if player == 1:
                self.diag += 1
            else:
                self.diag -= 1
            
            if self.diag == self.n or self.diag == self.n * -1:
                return player
            
        if col == self.n-1-row:
            if player == 1:
                self.anti += 1
            else:
                self.anti -= 1
            if self.anti == self.n or self.anti == self.n * -1:
                return player
        return 0
        


# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)

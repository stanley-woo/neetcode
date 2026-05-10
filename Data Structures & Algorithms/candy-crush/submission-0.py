class Solution:
    def candyCrush(self, board: List[List[int]]) -> List[List[int]]:
        m, n = len(board), len(board[0])

        def find():
            crushed = set()

            for r in range(1, m-1):
                for c in range(n):
                    if board[r][c] == 0:
                        continue
                    if board[r][c] == board[r - 1][c] == board[r + 1][c]:
                        crushed.add((r,c))
                        crushed.add((r - 1, c))
                        crushed.add((r + 1, c))

            for r in range(m):
                for c in range(1, n - 1):
                    if board[r][c] == 0:
                        continue
                    
                    if board[r][c] == board[r][c - 1] == board[r][c+1]:
                        crushed.add((r,c))
                        crushed.add((r, c-1))
                        crushed.add((r, c+1))
            
            return crushed
        
        def crush(crushed):
            for (r,c) in crushed:
                board[r][c] = 0
        
        def drop():
            for c in range(n):
                lowest_zero = -1

                for r in range(m - 1, -1, -1):
                    if board[r][c] == 0:
                        lowest_zero = max(lowest_zero, r)
                    elif lowest_zero >= 0:
                        board[r][c], board[lowest_zero][c] = board[lowest_zero][c], board[r][c]
                        lowest_zero -= 1
        
        crushed = find()
        while crushed:
            crush(crushed)
            drop()
            crushed = find()
        
        return board

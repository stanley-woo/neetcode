class Leaderboard:

    def __init__(self):
        self.playerTable = {}

    def addScore(self, playerId: int, score: int) -> None:
        if playerId not in self.playerTable:
            self.playerTable[playerId] = 0
        self.playerTable[playerId] += score
        
    def top(self, K: int) -> int:
        heap = []
        for x in self.playerTable.values():
            heapq.heappush(heap, x)
            if len(heap) > K:
                heapq.heappop(heap)
        res = 0
        while heap:
            res += heapq.heappop(heap)
        return res

    def reset(self, playerId: int) -> None:
        self.playerTable[playerId] = 0


# Your Leaderboard object will be instantiated and called as such:
# obj = Leaderboard()
# obj.addScore(playerId,score)
# param_2 = obj.top(K)
# obj.reset(playerId)

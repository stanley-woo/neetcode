class Solution:
    def maxTransactions(self, transactions: List[int]) -> int:
        n = len(transactions)
        res, cur_balance = 0, 0

        for i in range(n):
            if cur_balance + transactions[i] < 0:
                continue
            cur_balance += transactions[i]
            res += 1
        
        return res
        # pq = []

        # for transaction in transactions:
        #     heapq.heappush(pq, -transaction)
        
        # res = 0
        # cur_balance = 0

        # while pq:
        #     transact = heapq.heappop(pq)
        #     transact = -transact

        #     if cur_balance + transact < 0:
        #         break
        #     else:
        #         cur_balance += transact
        #         res += 1
        
        # return res
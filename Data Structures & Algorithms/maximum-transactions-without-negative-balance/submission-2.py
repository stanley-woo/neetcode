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
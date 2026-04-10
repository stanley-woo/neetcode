class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        res = -1
        for i in range(len(prices)):
            for j in range(i + 1, len(prices)):
                if prices[i] + prices[j] <= money:
                    res = max(res, money - prices[i] - prices[j])
        return res if res != -1 else money
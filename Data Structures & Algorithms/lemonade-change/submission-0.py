class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        cash = 0
        cost = 5
        for bill in bills:
            change = bill - cost
            if change > cash:
                return False
            cash += cost
        return True
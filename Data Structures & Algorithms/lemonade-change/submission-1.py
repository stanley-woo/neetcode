class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        cash = 0
        cost = 5
        for bill in bills:
            if bill - cost > cash:
                return False
            else:
                cash += cost
                if bill - cost > 0:
                    cash -= (bill - cost)

        return True
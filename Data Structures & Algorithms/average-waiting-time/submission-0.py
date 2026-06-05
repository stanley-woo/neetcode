class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        n = len(customers)
        total = 0
        ptr = 0

        for arrival, make in customers:
            if arrival > ptr:
                ptr = arrival
            total += (ptr + make - arrival)
            ptr += make
        return total / n
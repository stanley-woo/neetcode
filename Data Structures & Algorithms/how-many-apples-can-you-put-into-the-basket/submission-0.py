class Solution:
    def maxNumberOfApples(self, weight: List[int]) -> int:
        # Sorting from smallest to largerst
        weight.sort()

        cur_weight = 0
        res = 0

        for i in range(len(weight)):
            if cur_weight + weight[i] <= 5000:
                cur_weight += weight[i]
                res += 1
            else:
                break
        
        return res
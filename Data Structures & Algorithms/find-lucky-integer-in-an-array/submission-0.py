class Solution:
    def findLucky(self, arr: List[int]) -> int:
        freq_table = {}

        for num in arr:
            freq_table[num] = freq_table.get(num, 0) + 1
        
        res = -1

        for num in arr:
            if freq_table[num] == num:
                res = max(res, num)
        
        return res
from collections import defaultdict
class Solution:
    def longestCommonSubsequence(self, arrays: list[list[int]]) -> list[int]:
        n = len(arrays)
        counter = defaultdict(int)

        for arr in arrays:
            for val in arr:
                counter[val] += 1
        
        min_arr = arrays[0]
        for arr in arrays:
            if len(arr) < len(min_arr):
                min_arr = arr
        
        res = []
        for num in min_arr:
            if counter[num] == n:
                res.append(num)
        
        return res
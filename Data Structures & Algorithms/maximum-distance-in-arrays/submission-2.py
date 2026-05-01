class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        res = 0
        global_min = arrays[0][0]
        global_max = arrays[0][-1]

        for i in range(1, len(arrays)):
            res = max(res, max(global_max - arrays[i][0], arrays[i][-1] - global_min))
            global_min = min(global_min, arrays[i][0])
            global_max = max(global_max, arrays[i][-1])
        
        return res
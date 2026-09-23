class Solution:
    def removeInterval(self, intervals: list[list[int]], toBeRemoved: list[int]) -> list[list[int]]:
        res = []
        rm_start, rm_end = toBeRemoved[0], toBeRemoved[1]
        for start, end in intervals:
            if end <= rm_start or start >= rm_end:
                res.append((start, end))
            else:
                if start < rm_start:
                    res.append((start, rm_start))
                
                if end > rm_end:
                    res.append((rm_end, end))
        return res
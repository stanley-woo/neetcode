class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        sorted_heights = heights[:]
        sorted_heights.sort()

        res = 0

        for i in range(len(heights)):
            if sorted_heights[i] != heights[i]:
                res += 1
        
        return res
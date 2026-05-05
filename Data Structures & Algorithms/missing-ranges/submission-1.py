class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[List[int]]:
        res = []

        cur = lower
        for i in range(len(nums)):
            if nums[i] > cur:
                res.append([cur, nums[i] - 1])
            cur = nums[i] + 1
        
        if cur <= upper:
            res.append([cur, upper])
        
        return res
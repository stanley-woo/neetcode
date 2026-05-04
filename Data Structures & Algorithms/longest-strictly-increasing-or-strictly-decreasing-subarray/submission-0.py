class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        cur = 0
        res = 1
        increasing = True

        for i in range(1, len(nums)):
            if nums[i-1] < nums[i]:
                if increasing:
                    cur += 1
                else:
                    cur = 2
                    increasing = True
            elif nums[i-1] > nums[i]:
                if not increasing:
                    cur += 1
                else:
                    cur = 2
                    increasing = False
            else:
                cur = 1
                increasing = False
            res = max(res, cur)
        return res
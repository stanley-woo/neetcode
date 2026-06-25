class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        res = float("inf")
        cur_sum = 0
        l = 0
        for r in range(len(nums)):
            cur_sum += nums[r]
            while cur_sum >= target:
                res = min(res, r - l + 1)
                cur_sum -= nums[l]
                l += 1
        if res == float("inf"):
            return 0
        return res
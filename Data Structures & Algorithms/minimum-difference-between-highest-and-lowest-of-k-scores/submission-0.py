class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums.sort()
        res = 100000

        l, r = 0, k - 1

        while r < len(nums):
            cur_diff = nums[r] - nums[l]
            res = min(res, cur_diff)
            l += 1
            r += 1
            
        return res
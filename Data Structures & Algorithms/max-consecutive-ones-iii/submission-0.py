class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        n = len(nums)
        l = res = 0

        for r in range(n):
            if nums[r] == 0:
                k -= 1
            while k < 0:
                k += (1 if nums[l] == 0 else 0)
                l += 1
            res = max(res, r - l + 1)
        return res
class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        curTotal = 1
        res = 0
        l = 0

        for r in range(len(nums)):
            curTotal *= nums[r]
            
            while l <= r and curTotal >= k:
                curTotal //= nums[l]
                l += 1
            res += (r - l + 1)
        return res
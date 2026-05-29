class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort() # O(n log n) time
        res, curSum = 0, 0
        l = 0

        for r in range(len(nums)):
            curSum += nums[r]

            while (r - l + 1) * nums[r] - curSum > k:
                curSum -= nums[l]
                l += 1
            
            res = max(res, r - l + 1)
        return res
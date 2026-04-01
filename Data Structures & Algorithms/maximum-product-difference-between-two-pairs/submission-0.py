class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        nums.sort()

        left, right = 0, len(nums) - 1
        res = 0
        while left < right:
            left_pair = nums[left] * nums[left + 1]
            right_pair = nums[right] * nums[right - 1]

            res = max(res, right_pair - left_pair)

            left += 2
            right + 2
        return res
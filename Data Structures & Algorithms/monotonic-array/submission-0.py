class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        if len(nums) == 1 or len(nums) == 2:
            return True
        monotonic = nums[0] <= nums[1]

        for i in range(2, len(nums)):
            if monotonic:
                if nums[i] < nums[i-1]:
                    return False
            else:
                if nums[i] > nums[i-1]:
                    return False
        return True
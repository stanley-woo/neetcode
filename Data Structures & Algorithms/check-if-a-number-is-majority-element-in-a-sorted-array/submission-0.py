class Solution:
    def isMajorityElement(self, nums: List[int], target: int) -> bool:
        n = len(nums) - 1

        if nums[n // 2] == target:
            return True
        
        return False
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total = sum(nums)
        prefix = 0
        for i, x in enumerate(nums):
            suffix = total - prefix - x
            if prefix == suffix:
                return i
            prefix += x
            
        return -1
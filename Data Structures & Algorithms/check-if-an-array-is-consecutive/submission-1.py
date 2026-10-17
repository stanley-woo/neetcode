class Solution:
    def isConsecutive(self, nums: List[int]) -> bool:
        num_set = set(nums)
        min_val = min(nums)
        n = len(nums)

        for val in range(min_val, min_val + n):
            if val not in num_set:
                return False
        
        return True
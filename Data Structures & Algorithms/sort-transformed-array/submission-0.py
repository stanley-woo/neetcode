class Solution:
    def sortTransformedArray(self, nums: List[int], a: int, b: int, c: int) -> List[int]:
        def fx(x, a, b, c):
            res = a * (x**2) + b * x + c
            return res
        
        for i in range(len(nums)):
            nums[i] = fx(nums[i], a, b, c)
        
        nums.sort()
        return nums
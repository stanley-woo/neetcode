class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        l, r = 0 ,0
        ans = 0
        num_zeros = 0

        while r < len(nums):
            if nums[r] == 0:
                num_zeros += 1
            
            while num_zeros == 2:
                if nums[l] == 0:
                    num_zeros -= 1
                l += 1
            ans = max(ans, r - l + 1)
            r += 1
        return ans
            
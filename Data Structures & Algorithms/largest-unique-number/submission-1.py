class Solution:
    def largestUniqueNumber(self, nums: List[int]) -> int:
        counter = Counter(nums)

        ans = -1
        for num in nums:
            if counter[num] == 1 and num > ans:
                ans = num
        return ans
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix = {0: 1}

        total_sum = 0
        res = 0
        for i in range(len(nums)):
            total_sum += nums[i]
            target = total_sum - k
            if target in prefix:
                res += prefix[target]
            prefix[total_sum] = prefix.get(total_sum, 0) + 1
        return res

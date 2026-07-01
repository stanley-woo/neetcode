class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        prefixSum = 0
        prefixMap = {0 : 1}

        res = 0
        for num in nums:
            prefixSum += num
            if prefixSum - goal in prefixMap:
                res += prefixMap[prefixSum - goal]
            prefixMap[prefixSum] = prefixMap.get(prefixSum, 0) + 1
        
        return res
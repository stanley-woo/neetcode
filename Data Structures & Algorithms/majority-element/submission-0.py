class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hash_map = {}

        for num in nums:
            hash_map[num] = hash_map.get(num, 0) + 1
            if hash_map[num] >= len(nums) / 2:
                return num
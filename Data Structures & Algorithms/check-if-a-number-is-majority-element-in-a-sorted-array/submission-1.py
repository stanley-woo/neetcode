class Solution:
    def isMajorityElement(self, nums: List[int], target: int) -> bool:
        hash_map = {}
        n = len(nums)
        for num in nums:
            hash_map[num] = hash_map.get(num, 0) + 1
        
        for key, count in hash_map.items():
            if count > n // 2:
                return True
        
        return False

        
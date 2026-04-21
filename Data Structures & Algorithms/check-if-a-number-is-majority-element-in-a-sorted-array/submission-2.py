class Solution:
    def isMajorityElement(self, nums: List[int], target: int) -> bool:
        hash_map = {}
        n = len(nums)
        for num in nums:
            hash_map[num] = hash_map.get(num, 0) + 1
        
        if target not in hash_map:
            return False
        else:
            if hash_map[target] > n // 2:
                return True
        
        return False

        
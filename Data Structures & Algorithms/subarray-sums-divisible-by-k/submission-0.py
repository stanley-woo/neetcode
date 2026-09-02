class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        prefix_sum = 0
        res = 0
        prefix = defaultdict(int)
        prefix[0] = 1

        for num in nums:
            prefix_sum += num
            remain = prefix_sum % k

            res += prefix[remain]
            prefix[remain] += 1
        
        return res
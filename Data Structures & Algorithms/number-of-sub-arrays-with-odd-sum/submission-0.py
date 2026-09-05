class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        n, mod = len(arr), 10**9 + 7
        res = prefix_sum = 0
        odd, even = 0, 1

        for n in arr:
            prefix_sum += n
            if prefix_sum % 2:
                res += even
                odd += 1
            else:
                res += odd
                even += 1
        
        return res % mod
class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        res = 0
        l, cur = 0 , 0

        for r in range(len(arr)):
            if r - l + 1 > k:
                cur -= arr[l]
                l += 1
            cur += arr[r]
            if (r - l + 1) == k and cur / k >= threshold:
                res += 1
        

        return res
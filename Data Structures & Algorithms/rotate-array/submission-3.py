class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k %= n
        count = start = 0

        while count < n:
            cur = start
            prev = nums[start]
            while True:
                next_idx = (cur + k) % n
                nums[next_idx], prev = prev, nums[next_idx]
                cur = next_idx
                count += 1

                if start == cur:
                    break
            start += 1
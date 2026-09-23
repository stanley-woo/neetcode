class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)

        def lower_bound(value):
            lo, hi = 0, n

            while lo < hi:
                mid = lo + (hi - lo) // 2

                if nums[mid] < value:
                    lo = mid + 1
                else:
                    hi = mid

            return lo

        start = lower_bound(target)

        if start == n or nums[start] != target:
            return [-1, -1]

        end = lower_bound(target + 1) - 1

        return [start, end]
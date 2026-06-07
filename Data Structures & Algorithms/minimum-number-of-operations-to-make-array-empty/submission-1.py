class Solution:
    def minOperations(self, nums: List[int]) -> int:
        cache = {}

        def dfs(num):
            if num < 0:
                return float("inf")
            if num in [2, 3]:
                return 1
            if num in cache:
                return cache[num]

            res = min(dfs(num - 2), dfs(num - 3))
            cache[num] = res + 1
            return cache[num]

        count = Counter(nums)
        res = 0
        for num, cnt in count.items():
            op = dfs(cnt)
            if op == float("inf"):
                return -1
            res += op

        return res
class Solution:
    def maximumSumScore(self, nums: List[int]) -> int:
        total = sum(nums)
        prefix = 0
        answer = total
        for value in nums:
            answer = max(answer, total - prefix)
            prefix += value
            answer = max(answer, prefix)
        return answer

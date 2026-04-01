class Solution:
    def maxDifference(self, s: str) -> int:
        odd_max, even_min = 0, len(s)
        counter = Counter(s)

        for count in counter.values():
            if count & 1:
                odd_max = max(odd_max, count)
            else:
                even_min = min(even_min, count)
        return odd_max - even_min
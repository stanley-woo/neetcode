class Solution:
    def maxDifference(self, s: str) -> int:
        odd_max, even_max = 0, 0
        counter = Counter(s)

        for char in s:
            if counter[char] % 2 != 0 and counter[char] > odd_max:
                odd_max = counter[char]
            if counter[char] % 2 == 0 and counter[char] > even_max:
                even_max = counter[char]
        return abs(odd_max - even_max)
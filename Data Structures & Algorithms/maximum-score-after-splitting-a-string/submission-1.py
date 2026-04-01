class Solution:
    def maxScore(self, s: str) -> int:
        # res = Max of all (left_zeros + right_ones)
        # res = Max of all (left_zeros + (total_ones - left_ones))
        # res = total_ones (constant) + Max of all (left_zeros - left_ones)

        zeros = 0
        ones = 0

        if s[0] == '0':
            zeros += 1
        else:
            ones += 1

        res = float('-inf')
        for i in range(1, len(s)):
            res = max(res, zeros - ones)
            if s[i] == '0':
                zeros += 1
            else:
                ones += 1

        return res + ones
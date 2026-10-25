class Solution:
    def equalDigitFrequency(self, s: str) -> int:
        suffixes = sorted(s[i:] for i in range(len(s)))
        previous = ""
        answer = 0
        for suffix in suffixes:
            shared = 0
            while shared < min(len(previous), len(suffix)) and previous[shared] == suffix[shared]:
                shared += 1
            counts = [0] * 10
            distinct = largest = 0
            for length, ch in enumerate(suffix, 1):
                digit = ord(ch) - 48
                if counts[digit] == 0:
                    distinct += 1
                counts[digit] += 1
                largest = max(largest, counts[digit])
                if length > shared and distinct * largest == length:
                    answer += 1
            previous = suffix
        return answer

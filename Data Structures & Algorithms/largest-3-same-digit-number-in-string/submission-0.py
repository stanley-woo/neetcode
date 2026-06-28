class Solution:
    def largestGoodInteger(self, num: str) -> str:
        res = ""
        for i in range(len(num)-2):
            count = Counter(num[i:i+3])
            if len(count) == 1:
                val = num[i:i+3]
                res = max(res, val)
        return res
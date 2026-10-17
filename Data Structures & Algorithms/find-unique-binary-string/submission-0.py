class Solution:
    def findDifferentBinaryString(self, nums: list[str]) -> str:
        n = len(nums[0])
        num_strs = set(nums)
        res = ''
        def backtrack(cur_s):
            nonlocal res
            if len(cur_s) == n:
                if cur_s in num_strs:
                    return False
                res = cur_s
                return True
            
            for char in ['0', '1']:
                cur_s += char
                if backtrack(cur_s):
                    return True
                cur_s = cur_s[:-1]
            return False
            
        backtrack('')
        return res
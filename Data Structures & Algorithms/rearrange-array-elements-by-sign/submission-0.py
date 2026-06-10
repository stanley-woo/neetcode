class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        pos, nev = [], []

        for i in range(n):
            if nums[i] >= 0:
                pos.append(nums[i])
            else:
                nev.append(nums[i])
        
        p1, p2, cur = 0, 0, 0
        while p1 < len(pos) and p2 < len(nev):
            nums[cur] = pos[p1]
            nums[cur+1] = nev[p2]
            p1 += 1
            p2 += 1
            cur += 2
        return nums
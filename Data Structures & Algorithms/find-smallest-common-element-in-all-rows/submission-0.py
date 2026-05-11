import bisect
class Solution:
    def smallestCommonElement(self, mat: List[List[int]]) -> int:
        m, n = len(mat), len(mat[0])

        for target in mat[0]:
            found_in_all = True

            for r in range(1, m):
                idx = bisect.bisect_left(mat[r], target)

                if idx == n or mat[r][idx] != target:
                    found_in_all = False
                    break
        
            if found_in_all:
                return target
        return -1
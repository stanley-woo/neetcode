class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        res = []
        hash_set = set()

        for g in grid:
            for num in g:
                if num in hash_set:
                    res.append(num)
                else:
                    hash_set.add(num)
        
        for num in range(1, (len(grid) * len(grid)) + 1):
            if num not in hash_set:
                res.append(num)
                break
        return res
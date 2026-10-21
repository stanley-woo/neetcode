class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        in_degree = [0] * n

        for _, v in edges:
            in_degree[v] += 1
        
        potential = False
        res = -1
        for i in range(n):
            if in_degree[i] == 0:
                if not potential:
                    potential = True
                    res = i
                else:
                    return -1
        
        return res
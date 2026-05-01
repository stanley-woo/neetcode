class Solution:
    def multiply(self, mat1: List[List[int]], mat2: List[List[int]]) -> List[List[int]]:
        m1, n1 = len(mat1), len(mat1[0])
        m2, n2 = len(mat2), len(mat2[0])

        res = [[0] * n2 for _ in range(m1)]

        for i in range(m1):
            for j in range(n2):
                cur_sum = 0
                for k in range(n1):
                    if mat1[i][k] == 0 or mat2[k][j] == 0:
                        continue
                    cur_sum += mat1[i][k] * mat2[k][j]
                res[i][j] = cur_sum
        
        return res
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ans = [[1]]
        if numRows == 1:
            return ans
        for i in range(1, numRows):
            new_row = [0] * (i+1)
            new_row[0] = 1
            new_row[-1] = 1
            for j in range(1, i):
                new_row[j] = ans[i-1][j-1] + ans[i-1][j]
            ans.append(new_row)
        return ans

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]
        
        if rowIndex == 1:
            return [1, 1]

        pascal = [[1], [1,1]]
        for r in range(2, rowIndex+1):
            prev_row = pascal[r-1]
            cur_row = [0] * (r+1)
            cur_row[0], cur_row[-1] = 1, 1
            for c in range(1, len(cur_row)-1):
                cur_row[c] = prev_row[c-1] + prev_row[c]
            pascal.append(cur_row)
        return pascal[-1]
class Solution:
    def findLonelyPixel(self, picture: List[List[str]]) -> int:
        colTable = defaultdict(int)
        rowTable = defaultdict(int)

        rows, cols = len(picture), len(picture[0])

        for r in range(rows):
            for c in range(cols):
                if picture[r][c] == "B":
                    rowTable[r] += 1
                    colTable[c] += 1
        
        res = 0

        for r in range(rows):
            for c in range(cols):
                if picture[r][c] == "B":
                    if rowTable[r] == 1 and colTable[c] == 1:
                        res += 1
        
        return res
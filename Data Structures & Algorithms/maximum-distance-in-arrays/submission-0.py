class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        res = 0

        for i in range(len(arrays)-1):
            for j in range(i+1, len(arrays)):
                arr1 = arrays[i]
                arr2 = arrays[j]

                res = max(res, abs(arr1[0])-arr2[-1])
                res = max(res, abs(arr1[-1]-arr2[0]))
        
        return res
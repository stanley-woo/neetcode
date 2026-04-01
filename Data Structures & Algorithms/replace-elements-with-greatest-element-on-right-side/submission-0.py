class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        for i in range(len(arr)):
            right_max = -1
            for j in range(i+1, len(arr)):
                if arr[j] > right_max:
                    right_max = arr[j]
            arr[i] = right_max
        arr[-1] = -1
        return arr
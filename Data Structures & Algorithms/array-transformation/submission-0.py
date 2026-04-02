class Solution:
    def transformArray(self, arr: List[int]) -> List[int]:
        changed = True
        while changed:
            changed = False
            new_arr = list(arr)
            for j in range(1, len(arr) - 1):
                if arr[j] > arr[j-1] and arr[j] > arr[j+1]:
                    new_arr[j] -= 1
                    changed = True
                if arr[j] < arr[j-1] and arr[j] < arr[j+1]:
                    new_arr[j] += 1
                    changed = True
            arr = new_arr
        return new_arr
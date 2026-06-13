class Solution:
    def minAvailableDuration(self, slots1: List[List[int]], slots2: List[List[int]], duration: int) -> List[int]:
        i, j = 0, 0
        m, n = len(slots1), len(slots2)
        slots1.sort(), slots2.sort() # O(nlogn)
        while i < m and j < n: # O(min(n_1, n_2))
            start_int = max(slots1[i][0], slots2[j][0])
            end_int = min(slots1[i][1], slots2[j][1])
            if start_int < end_int and end_int - start_int >= duration:
                return [start_int, min(end_int, start_int + duration)]
            if slots1[i][1] <= slots2[j][1]:
                i += 1
            else:
                j += 1
        return []
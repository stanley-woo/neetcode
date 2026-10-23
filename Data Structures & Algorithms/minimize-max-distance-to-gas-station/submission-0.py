class Solution:
    def minmaxGasDist(self, stations: List[int], k: int) -> float:
        # binary search penalty value
        # greedy logic -> can i achieve this max gap?
        # 
        ans = self.binary_search(stations, k)
        return ans
    

    def binary_search(self, arr, k):
        # if no two stations more than x apart
        # can i make that happen with <= k many new stations
        lo = 0
        hi = max([arr[i+1]-arr[i] for i in range(len(arr)-1)])# max gap between cons stations
        while (hi - lo) >= 1e-6:
            # mid & check
            mid = lo + (hi-lo)/2
            if self.can_make(mid, arr, k):
                hi = mid
            else:
                lo = mid
        return lo
    
    def can_make(self, mid, arr, k):
        total_add = 0
        for i in range(len(arr)-1):
            gap = arr[i+1]-arr[i]
            add = math.ceil(gap/mid)-1
            total_add += add
        return total_add <= k   
class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        trips.sort(key = lambda x: x[1])

        pq = []
        curr_cap = capacity
        for pas, start, end in trips:
            while pq and pq[0][0] <= start:
                _, num_pass = heapq.heappop(pq)
                curr_cap += num_pass
            
            curr_cap -= pas

            if curr_cap < 0:
                return False
            heapq.heappush(pq, (end, pas))
        
        return True
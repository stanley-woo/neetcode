import heapq
from typing import List

class Solution:
    def assignBikes(self, workers: List[List[int]], bikes: List[List[int]]) -> List[int]:
        distances = []

        # 1. Generate all possible worker-bike pairs
        for w, worker in enumerate(workers):
            for b, bike in enumerate(bikes):
                dist = abs(worker[0] - bike[0]) + abs(worker[1] - bike[1])
                distances.append((dist, w, b))

        # 2. Transform the list into a min-heap in O(N) time
        heapq.heapify(distances)

        res = [-1] * len(workers)
        assigned_bikes = set()
        assigned_count = 0

        # 3. Process the pairs from shortest distance to longest
        while distances and assigned_count < len(workers):
            dist, w, b = heapq.heappop(distances)

            # If both the worker and the bike are completely free
            if res[w] == -1 and b not in assigned_bikes:
                res[w] = b
                assigned_bikes.add(b)
                assigned_count += 1

        return res      